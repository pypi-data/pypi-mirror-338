# -*- coding: utf-8 -*-
# @Author  : gaoyu
# @Time    : 2025/3/28 14:45
# @Function: 行政区划与站点相交服务
# 本模块提供行政区划与水文站点之间的空间关系计算功能
# 主要功能包括：获取指定行政区划内的所有水文站点

import pandas as pd
from loguru import logger
import os
import sys
import functools
from datetime import datetime, timedelta

# 添加项目根目录到系统路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from utils.postgres_util import get_qgispostgres_data
from utils.json_util import df_to_post_json_data
from sqlalchemy import create_engine
from utils.cache_util import cache_result

# 添加一个函数来获取带密码的数据库连接
def get_db_connection():
    """获取带密码的数据库连接
    
    该函数尝试使用两种方式获取数据库连接：
    1. 首先尝试使用默认方式（无需密码）获取连接
    2. 如果默认方式失败，则使用硬编码的连接字符串创建连接
    
    Returns:
        connection: 数据库连接对象，可以是psycopg2连接或SQLAlchemy引擎
        
    Note:
        在生产环境中，应避免硬编码数据库凭据，建议使用环境变量或配置文件
    """
    try:
        # 尝试使用默认方式获取连接
        conn = get_qgispostgres_data()
        return conn
    except Exception as e:
        # 如果默认方式失败，尝试使用SQLAlchemy创建连接
        # 注意：这里硬编码了数据库凭据，生产环境中应避免这种做法
        engine = create_engine('postgresql://postgres:water@172.20.7.85:5432/qgis')
        return engine

@cache_result(seconds=3600)  # 缓存1小时
def get_stations_by_region(region_code):
    """
    获取指定行政区划内的所有站点
    
    该函数使用空间查询找出指定行政区划边界内的所有水文站点
    支持省级和市级行政区划代码，通过OR条件同时查询
    
    Args:
        region_code (str): 行政区划代码，如110000表示北京市，110100表示北京城区
        
    Returns:
        dict: 包含行政区划内站点信息的字典，格式如下：
            {
                "success": True/False,
                "data": {
                    "region_code": "110100",
                    "stations": [
                        {
                            "station_code": "10000001",
                            "station_name": "某水文站",
                            "longitude": 116.123,
                            "latitude": 39.456
                        },
                        ...
                    ]
                },
                "message": "错误信息（仅在失败时返回）"
            }
    """
    try:
        # 获取数据库连接
        conn = get_db_connection()
        
        # 查询行政区划内的站点 - 使用空间索引优化
        # 使用ST_SetSRID和ST_MakePoint将经纬度转换为空间点
        # 使用ST_Contains判断点是否在多边形内部
        query = f"""
        SELECT 
            s.stcd, s.rname as station_name, s.lon, s.lat
        FROM 
            st_stbprp_b s,
            admin_regions_city r
        WHERE 
            (r.ct_adcode = '{region_code}' OR r.pr_adcode = '{region_code}')
            AND r.geom && ST_SetSRID(ST_MakePoint(s.lon, s.lat), 4326)  -- 使用边界框预过滤，提高效率
            AND ST_Contains(r.geom, ST_SetSRID(ST_MakePoint(s.lon, s.lat), 4326))
        """

        # 执行SQL查询，获取结果集
        df = pd.read_sql(query, con=conn)

        # 如果查询结果为空，返回空列表
        if df.empty:
            return {
                "success": True,
                "data": {
                    "region_code": region_code,
                    "stations": []
                }
            }

        # 转换为JSON格式，df_to_post_json_data函数将DataFrame转换为JSON格式
        stations_data = df_to_post_json_data(df)
        
        # 修改返回格式，将每个站点作为单独的项目
        # 重命名字段，使其更符合API规范
        formatted_stations = []
        for station in stations_data:
            formatted_stations.append({
                "station_code": station["stcd"],
                "station_name": station["station_name"],
                "longitude": station["lon"],
                "latitude": station["lat"]
            })

        # 返回成功结果
        return {
            "success": True,
            "data": {
                "region_code": region_code,
                "stations": formatted_stations
            }
        }

    except Exception as e:
        # 记录错误日志并返回错误信息
        logger.error(f"获取行政区划内站点信息失败: {str(e)}")
        return {
            "success": False,
            "message": f"获取行政区划内站点信息失败: {str(e)}"
        }

# 测试代码
if __name__ == "__main__":
    # 设置日志，指定日志文件路径和轮转大小
    logger.add("logs/region_station_relation.log", rotation="10 MB")
    
    try:
        # 测试获取行政区划内的站点
        # 这里使用大连市的行政区划代码作为示例
        region_code = "210200"  # 大连市的行政区划代码
        result = get_stations_by_region(region_code)
        print(f"行政区划 {region_code} 内的站点:")
        print(result)
        
    except Exception as e:
        # 捕获并记录测试过程中的任何错误
        logger.error(f"测试过程中发生错误: {str(e)}")