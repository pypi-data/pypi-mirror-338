# -*- coding: utf-8 -*-
# @Author  : gaoyu
# @Time    : 2024/3/2 3:52 PM
# @Function:
# 加载必要的python库

import pandas as pd
import psycopg2
from loguru import logger
from sqlalchemy import create_engine

# 直接使用新的数据库连接信息，不再从config导入
# from config import WATER_DATABASE_URL
QGIS_DATABASE_URL = "postgresql://postgres:water@10.48.0.85:5432/qgis"
WATER_DATABASE_URL ="postgresql://postgres:water@172.20.7.85:5432/water"


def get_qgispostgres_data():
    """
    获取postgres数据库连接
    Returns:
    """
    _conn = psycopg2.connect(QGIS_DATABASE_URL)
    return _conn


def get_waterpostgres_data():
    """
    获取water数据库连接
    Returns:
    """
    _conn = psycopg2.connect(WATER_DATABASE_URL)
    return _conn


def get_data(sql_command: str, _conn):
    """"
    取数据
    """
    try:
        chunks = pd.read_sql(sql_command, _conn, chunksize=10000)
        # 将每个数据块拼接成一个DataFrame
        df = pd.concat(chunks, ignore_index=True)
        return df
    except Exception as e:
        logger.error(e)
        return pd.DataFrame()
    finally:
        if _conn:
            _conn.close()
            logger.debug("数据库连接已释放")


def get_qgispostgres_engine():
    """获取PostgreSQL数据库的SQLAlchemy引擎"""
    return create_engine(QGIS_DATABASE_URL)

def get_waterpostgres_engine():
    """获取PostgreSQL数据库的SQLAlchemy引擎"""
    return create_engine(WATER_DATABASE_URL)
