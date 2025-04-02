# -*- coding: utf-8 -*-
# @Author  : gaoyu
# @Time    : 2024/4/2 14:45
# @Function: 流域与站点关系服务
# 本模块提供流域与水文站点之间的空间关系计算功能
# 主要功能包括：获取流域几何数据、获取多个水库的合并几何数据等

import pandas as pd
from loguru import logger
import os
import sys
import functools
from datetime import datetime, timedelta

# 添加项目根目录到系统路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from utils.postgres_util import get_qgispostgres_data, get_data
from utils.json_util import df_to_post_json_data
from utils.cache_util import cache_result


@cache_result(seconds=3600)  # 缓存1小时
def get_basin_by_code(basin_code):
    """
    根据流域编码查询流域几何数据
    
    该函数查询指定流域编码的流域信息和几何数据，返回GeoJSON格式的几何数据
    几何数据经过简化处理，减少数据量，适用于前端地图展示
    
    Args:
        basin_code (str): 流域编码，如"NM000001"
        
    Returns:
        dict: 包含流域信息和几何数据(GeoJSON格式)的字典，格式如下：
            {
                "success": True/False,
                "data": {
                    "basin_id": "NM000001",
                    "basin_name": "某流域",
                    "area": 1234.56,  # 流域面积，单位平方公里
                    "geometry": "GeoJSON格式的几何数据"
                },
                "message": "错误信息（仅在失败时返回）"
            }
    """
    try:
        # 获取数据库连接
        conn = get_qgispostgres_data()
        
        # 查询流域信息和几何数据
        # ST_Simplify函数用于简化几何体，减少数据量，参数0.001表示简化的精度
        # ST_AsGeoJSON函数将PostGIS几何对象转换为GeoJSON格式
        query = f"""
        SELECT 
            basin_id, 
            basin_name,
            CASE WHEN area IS NOT NULL THEN area ELSE 0 END as area,
            ST_AsGeoJSON(ST_Simplify(geom, 0.001)) as geometry
        FROM 
            basins_shp
        WHERE 
            basin_id = '{basin_code}'
        """
        
        df = pd.read_sql(query, con=conn)
        
        # 如果查询结果为空，返回相应的提示信息
        if df.empty:
            return {
                "success": True,
                "data": None,
                "message": f"未找到编码为 {basin_code} 的流域"
            }
        
        # 转换为JSON格式，df_to_post_json_data函数将DataFrame转换为JSON格式
        basin_data = df_to_post_json_data(df)[0]
        
        # 格式化返回数据，提取需要的字段
        formatted_basin = {
            "basin_id": basin_data["basin_id"],
            "basin_name": basin_data["basin_name"],
            "area": basin_data["area"],
            "geometry": basin_data["geometry"]
        }
        
        return {
            "success": True,
            "data": formatted_basin
        }
        
    except Exception as e:
        # 记录错误日志并返回错误信息
        logger.error(f"获取流域几何数据失败: {str(e)}")
        return {
            "success": False,
            "message": f"获取流域几何数据失败: {str(e)}"
        }


@cache_result(seconds=3600)  # 缓存1小时
def get_reservoirs_geometry(reservoir_codes):
    """
    根据多个水库编码查询水库几何数据，返回合并后的MultiPolygon
    
    该函数查询多个水库的几何数据，并将它们合并为一个几何体
    合并后的几何体经过缓冲区处理，使水库边界更加平滑
    
    Args:
        reservoir_codes (list): 水库编码列表，如["6300899", "6121599"]
        
    Returns:
        dict: 包含合并后的水库几何数据(GeoJSON格式)的字典，格式如下：
            {
                "success": True/False,
                "data": {
                    "geometry": "GeoJSON格式的几何数据",
                    "count": 3,  # 水库数量
                    "reservoir_ids": ["6300899", "6121599", "9235299"],  # 水库编码列表
                    "reservoir_names": ["水库1", "水库2", "水库3"]  # 水库名称列表
                },
                "message": "错误信息（仅在失败时返回）"
            }
    """
    try:
        # 参数验证，确保传入的是非空列表
        if not reservoir_codes or not isinstance(reservoir_codes, list):
            return {
                "success": False,
                "message": "请提供有效的水库编码列表"
            }
        
        # 获取数据库连接
        conn = get_qgispostgres_data()
        
        # 构建IN查询条件，将列表转换为SQL中的IN子句格式
        codes_str = "', '".join(reservoir_codes)
        
        # 查询水库信息和几何数据
        # ST_Union函数将多个几何体合并为一个
        # ST_Buffer函数创建缓冲区，使几何体边界更平滑，参数0.01表示缓冲区大小
        # array_agg函数将多行数据聚合为数组
        query = f"""
        SELECT 
            ST_AsGeoJSON(ST_Buffer(ST_Union(geom), 0.01)) as geometry,
            COUNT(*) as count,
            array_agg(stcd) as reservoir_ids,
            array_agg(rname) as reservoir_names
        FROM 
            st_stbprp_b
        WHERE 
            stcd IN ('{codes_str}')
        """
        
        df = pd.read_sql(query, con=conn)
        
        # 如果查询结果为空或没有找到水库，返回相应的提示信息
        if df.empty or df.iloc[0]['count'] == 0:
            return {
                "success": True,
                "data": None,
                "message": f"未找到指定编码的水库"
            }
        
        # 转换为JSON格式
        result_data = df_to_post_json_data(df)[0]
        
        # 格式化返回数据，提取需要的字段
        formatted_result = {
            "geometry": result_data["geometry"],
            "count": result_data["count"],
            "reservoir_ids": result_data["reservoir_ids"],
            "reservoir_names": result_data["reservoir_names"]
        }
        
        return {
            "success": True,
            "data": formatted_result
        }
        
    except Exception as e:
        # 记录错误日志并返回错误信息
        logger.error(f"获取水库几何数据失败: {str(e)}")
        return {
            "success": False,
            "message": f"获取水库几何数据失败: {str(e)}"
        }


# 测试代码部分添加测试
if __name__ == "__main__":
    # 设置日志，指定日志文件路径和轮转大小
    logger.add("logs/basin_station_relation.log", rotation="10 MB")
    
    try:
        # 测试获取流域几何数据（默认被注释）
        # 取消注释以测试get_basin_by_code函数
        # basin_code = "NM000001"  # 示例流域编码，请替换为实际存在的编码
        # basin_result = get_basin_by_code(basin_code)
        # print(f"流域 {basin_code} 的几何数据:")
        # print(basin_result)
        
        # 测试获取多个水库的几何数据
        # 这里使用了三个示例水库编码，实际使用时应替换为数据库中存在的编码
        reservoir_codes = ["6300899", "6121599", "9235299"]  # 示例水库编码，请替换为实际存在的编码
        reservoirs_result = get_reservoirs_geometry(reservoir_codes)
        print(f"水库 {reservoir_codes} 的合并几何数据:")
        print(reservoirs_result)
        
    except Exception as e:
        # 捕获并记录测试过程中的任何错误
        logger.error(f"测试过程中发生错误: {str(e)}")