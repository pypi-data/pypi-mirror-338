# -*- coding: utf-8 -*-
# @Author  : gaoyu
# @Time    : 2024/3/28 15:00
# @Function: 流域与行政区划相交服务
# 本模块提供流域与行政区划之间的空间关系计算功能
# 主要功能包括：获取流域覆盖的行政区划、获取省份内的流域、获取城市内的流域等

import pandas as pd
import geopandas as gpd
from loguru import logger
import os
import sys
import functools
from datetime import datetime, timedelta
from utils.cache_util import cache_result

# 添加项目根目录到系统路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from utils.postgres_util import get_qgispostgres_data
from utils.json_util import df_to_post_json_data
from sqlalchemy import create_engine


# 删除get_db_connection函数

@cache_result(seconds=3600)  # 缓存1小时
def get_regions_by_basin(basin_id):
    """
    获取指定流域覆盖的行政区划
    
    该函数计算指定流域与行政区划的空间交叉关系，返回被流域覆盖的所有行政区划
    并计算每个行政区划被流域覆盖的比例
    
    Args:
        basin_id (str): 流域ID，如"NM000001"
        
    Returns:
        dict: 包含流域覆盖的行政区划信息，格式如下：
            {
                "success": True/False,
                "data": {
                    "basin_id": "NM000001",
                    "regions": [
                        {
                            "region_code": "210200",
                            "region_name": "大连市",
                            "province_code": "210000",
                            "province_name": "辽宁省",
                            "coverage_ratio": 0.75  # 流域覆盖行政区划的比例
                        },
                        ...
                    ]
                }
            }
    """
    try:
        # 获取数据库连接
        conn = get_qgispostgres_data()
        logger.debug(f"获取数据库连接成功，开始查询流域 {basin_id} 覆盖的行政区划")

        # 查询流域覆盖的行政区划 - 使用空间索引优化
        # ST_Area(ST_Intersection(b.geom, r.geom))/ST_Area(r.geom) 计算流域覆盖行政区划的面积比例
        query = f"""
        SELECT 
            r.ct_adcode, r.ct_name, r.pr_adcode, r.pr_name,
            ST_Area(ST_Intersection(b.geom, r.geom))/ST_Area(r.geom) as coverage_ratio
        FROM 
            admin_regions_city r,
            basins_shp b 
        WHERE 
            b.basin_id = '{basin_id}'
            AND b.geom && r.geom  -- 使用边界框预过滤，提高效率
            AND ST_Intersects(b.geom, r.geom)
        ORDER BY 
            coverage_ratio DESC
        """
        
        logger.debug(f"执行SQL查询: {query}")
        df = pd.read_sql(query, con=conn)
        logger.debug(f"查询结果行数: {len(df)}")

        if df.empty:
            logger.info(f"流域 {basin_id} 未覆盖任何行政区划")
            return {
                "success": True,
                "data": {
                    "basin_id": basin_id,
                    "regions": []
                }
            }

        # 转换为JSON格式
        regions_data = df_to_post_json_data(df)
        logger.debug(f"转换后的数据: {regions_data}")

        # 修改返回格式，将每个行政区域作为单独的项目
        formatted_regions = []
        for region in regions_data:
            formatted_regions.append({
                "region_code": region["ct_adcode"],
                "region_name": region["ct_name"],
                "province_code": region["pr_adcode"],
                "province_name": region["pr_name"],
                "coverage_ratio": region["coverage_ratio"]
            })

        return {
            "success": True,
            "data": {
                "basin_id": basin_id,
                "regions": formatted_regions
            }
        }

    except Exception as e:
        logger.error(f"获取流域覆盖的行政区划失败: {str(e)}")
        import traceback
        logger.error(traceback.format_exc())
        return {
            "success": False,
            "message": f"获取流域覆盖的行政区划失败: {str(e)}"
        }


#
# 以下是被注释掉的get_basins_by_region函数
# 该函数用于获取指定行政区划内的流域，但目前未启用
# 可能是因为功能重复或者存在性能问题
# @cache_result(seconds=3600)  # 缓存1小时
# def get_basins_by_region(region_code):
#     """
#     获取指定行政区划内的流域
#
#     Args:
#         region_code (str): 行政区划代码，如110100表示北京城区
#
#     Returns:
#         dict: 包含行政区划内流域信息
#     """
#     try:
#         # 获取数据库连接
#         conn = get_qgispostgres_data()
#
#         # 查询行政区划内的流域 - 使用空间索引优化和几何体简化
#         query = f"""
#         SELECT
#             b.basin_id,
#             b.basin_id as basin_name,  -- 使用basin_id作为名称的替代
#             CASE WHEN b.area IS NOT NULL THEN b.area ELSE 0 END as area,
#             ST_Area(ST_Intersection(ST_Simplify(b.geom, 0.001), ST_Simplify(r.geom, 0.001)))/ST_Area(b.geom) as coverage_ratio
#         FROM
#             basins_shp b,
#             admin_regions_city r
#         WHERE
#             (r.ct_adcode = '{region_code}' OR r.pr_adcode = '{region_code}')
#             AND b.geom && r.geom  -- 使用边界框预过滤，提高效率
#             AND ST_Intersects(b.geom, r.geom)
#         ORDER BY
#             coverage_ratio DESC
#         LIMIT 100  -- 限制返回数量
#         """
#
#         df = pd.read_sql(query, con=conn)
#
#         if df.empty:
#             return {
#                 "success": True,
#                 "data": {
#                     "region_code": region_code,
#                     "basins": []
#                 }
#             }
#
#         # 转换为JSON格式
#         basins_data = df_to_post_json_data(df)
#
#         # 修改返回格式，将每个流域作为单独的项目
#         formatted_basins = []
#         for basin in basins_data:
#             formatted_basins.append({
#                 "basin_id": basin["basin_id"],
#                 "basin_name": basin["basin_name"],
#                 "area": basin["area"],
#                 "coverage_ratio": basin["coverage_ratio"]
#             })
#
#         return {
#             "success": True,
#             "data": {
#                 "region_code": region_code,
#                 "basins": formatted_basins
#             }
#         }
#
#     except Exception as e:
#         logger.error(f"获取行政区划内流域信息失败: {str(e)}")
#         return {
#             "success": False,
#             "message": f"获取行政区划内流域信息失败: {str(e)}"
#         }


@cache_result(seconds=3600)  # 缓存1小时
def get_basins_by_province(province_code):
    """
    获取指定省份内的流域
    
    该函数计算指定省份与流域的空间交叉关系，返回与省份相交的所有流域
    并计算每个流域被省份覆盖的比例
    
    Args:
        province_code (str): 省份代码，如110000表示北京市
        
    Returns:
        dict: 包含省份内流域信息，格式如下：
            {
                "success": True/False,
                "data": {
                    "province_code": "110000",
                    "basins": [
                        {
                            "basin_id": "NM000001",
                            "basin_name": "某流域",
                            "area": 1234.56,  # 流域面积，单位平方公里
                            "coverage_ratio": 0.75  # 流域被省份覆盖的比例
                        },
                        ...
                    ]
                }
            }
    """
    try:
        # 获取数据库连接
        conn = get_qgispostgres_data()

        # 查询省份内的流域 - 使用空间索引优化和几何体简化
        # ST_Simplify函数用于简化几何体，减少计算复杂度
        # ST_Area(ST_Intersection(...))/ST_Area(b.geom) 计算流域被省份覆盖的面积比例
        query = f"""
        SELECT 
            b.basin_id, 
            b.basin_name,
            CASE WHEN b.area IS NOT NULL THEN b.area ELSE 0 END as area,
            ST_Area(ST_Intersection(ST_Simplify(b.geom, 0.001), ST_Simplify(r.geom, 0.001)))/ST_Area(b.geom) as coverage_ratio
        FROM 
            basins_shp b,
            admin_regions_province r
        WHERE 
            r.pr_adcode = '{province_code}'
            AND b.geom && r.geom  -- 使用边界框预过滤，提高效率
            AND ST_Intersects(b.geom, r.geom)
        ORDER BY 
            coverage_ratio DESC
        LIMIT 100  -- 限制返回数量
        """

        df = pd.read_sql(query, con=conn)

        if df.empty:
            return {
                "success": True,
                "data": {
                    "province_code": province_code,
                    "basins": []
                }
            }

        # 转换为JSON格式
        basins_data = df_to_post_json_data(df)

        # 修改返回格式，将每个流域作为单独的项目
        formatted_basins = []
        for basin in basins_data:
            formatted_basins.append({
                "basin_id": basin["basin_id"],
                "basin_name": basin["basin_name"],
                "area": basin["area"],
                "coverage_ratio": basin["coverage_ratio"]
            })

        return {
            "success": True,
            "data": {
                "province_code": province_code,
                "basins": formatted_basins
            }
        }

    except Exception as e:
        logger.error(f"获取省份内流域信息失败: {str(e)}")
        return {
            "success": False,
            "message": f"获取省份内流域信息失败: {str(e)}"
        }


@cache_result(seconds=3600)  # 缓存1小时
def get_basins_by_city(city_code):
    """
    获取指定城市内的流域
    
    该函数计算指定城市与流域的空间交叉关系，返回与城市相交的所有流域
    并计算每个流域被城市覆盖的比例
    
    Args:
        city_code (str): 城市代码，如110100表示北京城区
        
    Returns:
        dict: 包含城市内流域信息，格式如下：
            {
                "success": True/False,
                "data": {
                    "city_code": "110100",
                    "basins": [
                        {
                            "basin_id": "NM000001",
                            "basin_name": "某流域",
                            "area": 1234.56,  # 流域面积，单位平方公里
                            "coverage_ratio": 0.75  # 流域被城市覆盖的比例
                        },
                        ...
                    ]
                }
            }
    """
    try:
        # 获取数据库连接
        conn = get_qgispostgres_data()

        # 查询城市内的流域 - 使用空间索引优化和几何体简化
        # 与get_basins_by_province函数类似，但查询的是城市级别的行政区划
        query = f"""
        SELECT 
            b.basin_id, 
            b.basin_name,
            CASE WHEN b.area IS NOT NULL THEN b.area ELSE 0 END as area,
            ST_Area(ST_Intersection(ST_Simplify(b.geom, 0.001), ST_Simplify(r.geom, 0.001)))/ST_Area(b.geom) as coverage_ratio
        FROM 
            basins_shp b,
            admin_regions_city r
        WHERE 
            r.ct_adcode = '{city_code}'
            AND b.geom && r.geom  -- 使用边界框预过滤，提高效率
            AND ST_Intersects(b.geom, r.geom)
        ORDER BY 
            coverage_ratio DESC
        LIMIT 100  -- 限制返回数量
        """

        df = pd.read_sql(query, con=conn)

        if df.empty:
            return {
                "success": True,
                "data": {
                    "city_code": city_code,
                    "basins": []
                }
            }

        # 转换为JSON格式
        basins_data = df_to_post_json_data(df)

        # 修改返回格式，将每个流域作为单独的项目
        formatted_basins = []
        for basin in basins_data:
            formatted_basins.append({
                "basin_id": basin["basin_id"],
                "basin_name": basin["basin_name"],
                "area": basin["area"],
                "coverage_ratio": basin["coverage_ratio"]
            })

        return {
            "success": True,
            "data": {
                "city_code": city_code,
                "basins": formatted_basins
            }
        }

    except Exception as e:
        logger.error(f"获取城市内流域信息失败: {str(e)}")
        return {
            "success": False,
            "message": f"获取城市内流域信息失败: {str(e)}"
        }

# 测试代码
if __name__ == "__main__":
    # 设置日志
    logger.add("logs/basin_region_relation.log", rotation="10 MB")

    # 测试获取流域覆盖的行政区划
    # basin_id = "NM000001"  # 示例流域ID，请替换为实际存在的ID
    # result = get_regions_by_basin(basin_id)
    # print(f"流域 {basin_id} 覆盖的行政区划:")
    # print(result)

    # 测试获取省份内的流域
    # province_code = "220000"  # 吉林省
    # result = get_basins_by_province(province_code)
    # print(f"省份 {province_code} 内的流域:")
    # print(result)
    
    # 测试获取城市内的流域
    # city_code = "210200"  # 大连市
    # result = get_basins_by_city(city_code)
    # print(f"城市 {city_code} 内的流域:")
    # print(result)


