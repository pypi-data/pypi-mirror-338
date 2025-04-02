# -*- coding: utf-8 -*-
# @Author  : gaoyu
# @Time    : 2025/3/28 14:45
# @Function: 行政区划服务
# 本模块提供行政区划数据的查询和处理功能，支持省级、市级和区县级行政区划的查询
# 主要功能包括：获取所有省份、获取省份下的城市、获取城市下的区县、获取行政区划几何数据等

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
from sqlalchemy import create_engine
import re


# 移除原有的缓存装饰器代码，改为从utils.cache_util导入

@cache_result(seconds=3600)  # 缓存1小时
def get_all_provinces():
    """
    获取所有省级行政区划（不包含几何数据）
    
    该函数查询数据库中的所有省级行政区划信息，但不包含几何数据
    适用于需要展示省份列表的场景，减少数据传输量
    
    Returns:
        dict: 包含所有省级行政区划信息（不含几何数据）的字典，格式如下：
            {
                "success": True/False,
                "data": {
                    "provinces": [
                        {
                            "code": "110000",
                            "name": "北京市",
                            "country_code": "100000",
                            "country_name": "中国"
                        },
                        ...
                    ]
                }
            }
    """
    try:
        # 获取数据库连接
        conn = get_qgispostgres_data()

        # 查询所有省级行政区划，不包含几何数据
        query = """
        SELECT 
            pr_adcode as code, 
            pr_name as name,
            cn_adcode as country_code,
            cn_name as country_name
        FROM 
            admin_regions_province
        ORDER BY 
            code
        """

        df = pd.read_sql(query, con=conn)

        if df.empty:
            return {
                "success": True,
                "data": {
                    "provinces": []
                }
            }

        # 转换为JSON格式
        provinces_data = df_to_post_json_data(df)

        return {
            "success": True,
            "data": {
                "provinces": provinces_data
            }
        }

    except Exception as e:
        logger.error(f"获取所有省级行政区划失败: {str(e)}")
        return {
            "success": False,
            "message": f"获取所有省级行政区划失败: {str(e)}"
        }


@cache_result(seconds=3600)  # 缓存1小时
def get_cities_by_province(province_code):
    """
    获取指定省份下的所有城市
    
    该函数根据省份代码查询该省份下的所有城市信息
    适用于省市级联选择的场景
    
    Args:
        province_code (str): 省份代码，如110000表示北京市
        
    Returns:
        dict: 包含指定省份下所有城市信息的字典，格式如下：
            {
                "success": True/False,
                "data": {
                    "province_code": "110000",
                    "cities": [
                        {
                            "code": "110100",
                            "name": "北京城区",
                            "province_code": "110000",
                            "province_name": "北京市"
                        },
                        ...
                    ]
                }
            }
    """
    try:
        # 获取数据库连接
        conn = get_qgispostgres_data()

        # 查询指定省份下的所有城市
        query = f"""
        SELECT 
            ct_adcode as code, 
            ct_name as name,
            pr_adcode as province_code,
            pr_name as province_name
        FROM 
            admin_regions_city
        WHERE 
            pr_adcode = '{province_code}'
        ORDER BY 
            code
        """

        df = pd.read_sql(query, con=conn)

        if df.empty:
            return {
                "success": True,
                "data": {
                    "province_code": province_code,
                    "cities": []
                }
            }

        # 转换为JSON格式
        cities_data = df_to_post_json_data(df)
        return {
            "success": True,
            "data": {
                "province_code": province_code,
                "cities": cities_data
            }
        }

    except Exception as e:
        logger.error(f"获取省份下的城市失败: {str(e)}")
        return {
            "success": False,
            "message": f"获取省份下的城市失败: {str(e)}"
        }


@cache_result(seconds=3600)  # 缓存1小时
def get_region_by_code(region_code):
    """
    根据行政区划代码获取行政区划信息
    
    该函数根据行政区划代码查询行政区划信息，包含几何数据
    适用于需要展示行政区划边界的场景
    
    Args:
        region_code (str): 行政区划代码，可以是省级或市级代码
        
    Returns:
        dict: 包含行政区划信息的字典，格式如下：
            {
                "success": True/False,
                "data": {
                    "code": "110000",
                    "name": "北京市",
                    "geometry": "GeoJSON格式的几何数据",
                    "area_km2": 16410.54
                }
            }
    """
    try:
        # 获取数据库连接
        conn = get_qgispostgres_data()

        # 判断代码长度，确定是省级还是市级
        if len(region_code) == 2 or len(region_code) == 6:  # 省级代码通常是2位或6位
            table = "admin_regions_province"
            code_field = "pr_adcode"
            name_field = "pr_name"
        else:  # 市级代码
            table = "admin_regions_city"
            code_field = "ct_adcode"
            name_field = "ct_name"

        # 查询行政区划信息
        query = f"""
        SELECT 
            {code_field} as code, 
            {name_field} as name,
            ST_AsGeoJSON(ST_Simplify(geom, 0.001)) as geometry,
            ST_Area(ST_Transform(geom, 3857))/1000000 as area_km2
        FROM 
            {table}
        WHERE 
            {code_field} = '{region_code}'
        """

        df = pd.read_sql(query, con=conn)

        if df.empty:
            return {
                "success": True,
                "data": None
            }

        # 转换为JSON格式
        region_data = df_to_post_json_data(df)[0]

        # 格式化返回数据
        formatted_region = {
            "code": region_data["code"],
            "name": region_data["name"],
            "geometry": region_data["geometry"],
            "area_km2": round(region_data["area_km2"], 2)
        }

        return {
            "success": True,
            "data": formatted_region
        }

    except Exception as e:
        logger.error(f"获取行政区划信息失败: {str(e)}")
        return {
            "success": False,
            "message": f"获取行政区划信息失败: {str(e)}"
        }


@cache_result(seconds=3600)  # 缓存1小时
def get_districts_by_city(city_code):
    """
    获取指定城市下的所有区县
    
    该函数根据城市代码查询该城市下的所有区县信息
    适用于市区级联选择的场景
    
    Args:
        city_code (str): 城市代码，如210200表示大连市
    
    Returns:
        dict: 包含城市下所有区县信息的字典，格式如下：
            {
                "success": True/False,
                "data": {
                    "city_code": "210200",
                    "districts": [
                        {
                            "district_code": "210202",
                            "district_name": "中山区",
                            "city_code": "210200",
                            "city_name": "大连市",
                            "province_code": "210000",
                            "province_name": "辽宁省"
                        },
                        ...
                    ]
                }
            }
    """
    try:
        # 获取数据库连接
        conn = get_qgispostgres_data()

        # 查询城市下的所有区县
        query = f"""
        SELECT 
            dt_adcode, dt_name, ct_adcode, ct_name, pr_adcode, pr_name
        FROM 
            admin_regions_district
        WHERE 
            ct_adcode = '{city_code}'
        ORDER BY 
            dt_adcode
        """

        df = pd.read_sql(query, con=conn)

        if df.empty:
            return {
                "success": True,
                "data": {
                    "city_code": city_code,
                    "districts": []
                }
            }

        # 转换为JSON格式
        districts_data = df_to_post_json_data(df)

        # 修改返回格式，将每个区县作为单独的项目
        formatted_districts = []
        for district in districts_data:
            formatted_districts.append({
                "district_code": district["dt_adcode"],
                "district_name": district["dt_name"],
                "city_code": district["ct_adcode"],
                "city_name": district["ct_name"],
                "province_code": district["pr_adcode"],
                "province_name": district["pr_name"]
            })

        return {
            "success": True,
            "data": {
                "city_code": city_code,
                "districts": formatted_districts
            }
        }

    except Exception as e:
        logger.error(f"获取城市下区县信息失败: {str(e)}")
        return {
            "success": False,
            "message": f"获取城市下区县信息失败: {str(e)}"
        }


@cache_result(seconds=3600)  # 缓存1小时
def get_region_geometry_by_code(region_code):
    """
    根据行政区划代码查询行政区面，返回GeoJSON格式
    
    该函数使用正则表达式判断行政区划代码类型，并查询相应的表
    支持省级、市级和区县级行政区划的查询
    返回的几何数据经过简化处理，减少数据量
    
    Args:
        region_code (str): 行政区划代码，可以是省级、市级或区县级代码
        
    Returns:
        dict: 包含行政区划信息和几何数据(GeoJSON格式)的字典
    """
    try:
        # 获取数据库连接
        conn = get_qgispostgres_data()

        # 确保region_code是字符串类型
        region_code = str(region_code)

        # 使用正则表达式判断编码类型
        # 省级编码：6位数，后4位为0，如110000
        # 市级编码：6位数，后2位为0，如110100
        # 区县级编码：6位数，后2位不为0，如110101
        if len(region_code) != 6:
            logger.warning(f"无效的行政区划代码: {region_code}")
            return {
                "success": False,
                "message": f"无效的行政区划代码: {region_code}"
            }

        if region_code.endswith('0000'):
            # 省级
            table = "admin_regions_province"
            code_field = "pr_adcode"
            name_field = "pr_name"
            level = "province"
        elif region_code.endswith('00') and not region_code.endswith('0000'):
            # 市级
            table = "admin_regions_city"
            code_field = "ct_adcode"
            name_field = "ct_name"
            level = "city"
        else:
            # 区县级
            table = "admin_regions_district"
            code_field = "dt_adcode"
            name_field = "dt_name"
            level = "district"

        # 查询行政区划信息和几何数据
        query = f"""
        SELECT 
            {code_field} as code, 
            {name_field} as name,
            ST_AsGeoJSON(ST_Simplify(geom, 0.001)) as geometry,
            ST_Area(ST_Transform(geom, 3857))/1000000 as area_km2
        FROM 
            {table}
        WHERE 
            {code_field} = '{region_code}'
        """

        logger.debug(f"执行查询: {query}")
        df = pd.read_sql(query, con=conn)

        if df.empty:
            logger.warning(f"未找到行政区划代码 {region_code} 的数据")
            return {
                "success": True,
                "data": None,
                "message": f"未找到行政区划代码 {region_code} 的数据"
            }

        # 转换为JSON格式
        region_data = df_to_post_json_data(df)[0]

        # 格式化返回数据
        formatted_region = {
            "code": region_data["code"],
            "name": region_data["name"],
            "level": level,
            "geometry": region_data["geometry"],
            "area_km2": round(float(region_data["area_km2"]), 2) if isinstance(region_data["area_km2"],
                                                                               (int, float, str)) else 0
        }

        return {
            "success": True,
            "data": formatted_region
        }

    except Exception as e:
        logger.error(f"获取行政区划几何数据失败: {str(e)}")
        import traceback
        logger.error(traceback.format_exc())
        return {
            "success": False,
            "message": f"获取行政区划几何数据失败: {str(e)}"
        }


# 在测试代码部分添加测试
if __name__ == "__main__":
    # 设置日志
    logger.add("logs/admin_region_service.log", rotation="10 MB")

    provinces_result = get_all_provinces()
    print("所有省份:")
    print(provinces_result)

# 测试获取省份下的城市
# province_code = "220000"  # 吉林省
# cities_result = get_cities_by_province(province_code)
# print(f"省份 {province_code} 下的城市:")
# print(cities_result)

# 测试获取行政区划信息
# region_code = "110100"  # 北京城区
# region_result = get_region_by_code(region_code)
# print(f"行政区划 {region_code} 的信息:")
# print(region_result)

# 测试获取城市内区县
# result = get_districts_by_city("210200")
# print(result)

# 测试获取行政区划几何数据
# 测试省级
# province_code = "210000"  # 辽宁省
# province_result = get_region_geometry_by_code(province_code)
# print(f"省级行政区划 {province_code} 的几何数据:")
# print(province_result)

# 测试市级
# city_code = "210200"  # 大连市
# city_result = get_region_geometry_by_code(city_code)
# print(f"市级行政区划 {city_code} 的几何数据:")
# print(city_result)

# 测试区县级
# district_code = "210202"  # 中山区
# district_result = get_region_geometry_by_code(district_code)
# print(f"区县级行政区划 {district_code} 的几何数据:")
# print(district_result)
