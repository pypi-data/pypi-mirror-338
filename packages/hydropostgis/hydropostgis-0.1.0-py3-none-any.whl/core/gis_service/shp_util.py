# -*- coding: utf-8 -*-
# @Author  : gaoyu
# @Time    : 2025/4/2 10:30
# @Function: SHP文件处理工具
# 本模块提供SHP文件的导入、处理和管理功能
# 主要功能包括：将SHP文件导入到PostGIS数据库、记录导入信息、更新GeoServer预览链接等

import os
import sys
import tempfile
import geopandas as gpd
from loguru import logger
import pandas as pd
from sqlalchemy import text  # 在文件顶部添加text导入
# 添加项目根目录到系统路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# 修正导入语句，确保函数名一致
from utils.postgres_util import get_waterpostgres_data
from utils.postgres_util import get_waterpostgres_engine, get_qgispostgres_engine


def import_shp(gdf, source_info, table_name, data_type):
    """
    导入SHP文件到PostGIS数据库并记录导入信息
    
    该函数是导入SHP文件的主入口，它将GeoDataFrame导入到PostGIS数据库，
    并在导入成功后记录导入信息到shp_import_records表中
    
    Args:
        gdf (GeoDataFrame): 要导入的GeoDataFrame对象，通常由gpd.read_file()读取SHP文件得到
        source_info (str): 数据来源信息，用于记录数据的来源说明，如"某机构2023年流域数据"
        table_name (str): 要导入到的目标表名，如"basins_2023"
        data_type (str): 数据类型，可选值：
            - admin: 行政区划数据
            - station: 测站数据
            - basin: 流域数据
    
    Returns:
        dict: 导入结果，包含以下字段：
            - success (bool): 是否导入成功
            - message (str): 结果说明
            - record_count (int): 导入的记录数（仅当success为True时）
            - table_name (str): 完整表名（仅当success为True时）
            - columns (list): 导入的字段列表（仅当success为True时）
            - table_exists (bool): 表是否已存在
    """
    logger.info(f"开始处理SHP文件导入，表名: {table_name}, 数据类型: {data_type}")

    # 规范化数据类型（转为小写），确保数据类型一致性
    data_type = data_type.lower()
    logger.debug(f"规范化数据类型: {data_type}")

    # 调用内部函数导入数据到数据库
    import_result = import_shp_to_postgis(
        table_name=table_name,
        schema="public",
        if_exists="append",  # 如果表已存在，则追加数据
        gdf=gdf
    )

    # 如果导入成功，记录导入信息
    if import_result["success"]:
        logger.info(f"数据导入成功，开始添加导入记录")
        add_shp_import_record(source_info, table_name, data_type)
    else:
        logger.error(f"数据导入失败: {import_result['message']}")

    return import_result


def add_shp_import_record(source_info, target_table, data_type):
    """
    添加或更新SHP文件导入记录
    
    该函数将导入信息记录到shp_import_records表中，如果记录已存在则更新，否则新增
    记录表使用target_table作为唯一键，确保每个表只有一条导入记录
    
    Args:
        source_info (str): 数据来源信息，如"某机构2023年流域数据"
        target_table (str): 导入的目标表名，作为唯一标识，如"basins_2023"
        data_type (str): 数据类型，可选值：admin/station/basin
    
    Returns:
        bool: 是否成功添加/更新记录
    """
    conn = None
    try:
        # 获取water数据库连接（记录表存储在water数据库中）
        conn = get_waterpostgres_data()
        logger.debug("数据库连接成功")

        # 检查记录表是否存在，如果不存在则创建
        check_query = """
        SELECT EXISTS (
            SELECT FROM information_schema.tables 
            WHERE table_schema = 'public' AND table_name = 'shp_import_records'
        );
        """
        with conn.cursor() as cursor:
            cursor.execute(check_query)
            table_exists = cursor.fetchone()[0]
            logger.debug(f"记录表是否存在: {table_exists}")

            if not table_exists:
                # 创建记录表，使target_table作为唯一键
                # 表结构：id(自增主键)、source_info(来源信息)、target_table(目标表名，唯一)、data_type(数据类型)
                create_table_sql = """
                CREATE TABLE IF NOT EXISTS public.shp_import_records (
                    id SERIAL PRIMARY KEY,
                    source_info TEXT NOT NULL,
                    target_table TEXT NOT NULL UNIQUE,
                    data_type TEXT NOT NULL
                );
                """
                cursor.execute(create_table_sql)
                conn.commit()
                logger.info("创建导入记录表成功")

        # 检查记录是否已存在（根据target_table判断）
        check_table_query = """
        SELECT EXISTS (
            SELECT FROM public.shp_import_records 
            WHERE target_table = %s
        );
        """
        with conn.cursor() as cursor:
            cursor.execute(check_table_query, (target_table,))
            record_exists = cursor.fetchone()[0]
            logger.debug(f"记录是否已存在: {record_exists}")

        # 根据记录是否存在，执行更新或插入操作
        if record_exists:
            # 更新现有记录
            logger.info(f"更新现有记录: {target_table}")
            update_sql = """
            UPDATE public.shp_import_records 
            SET source_info = %s, data_type = %s
            WHERE target_table = %s;
            """
            with conn.cursor() as cursor:
                cursor.execute(update_sql, (source_info, data_type, target_table))
                conn.commit()
            logger.info(f"更新SHP文件导入记录: {source_info} -> {target_table}")
        else:
            # 插入新记录
            logger.info(f"插入新记录: {target_table}")
            insert_sql = """
            INSERT INTO public.shp_import_records (source_info, target_table, data_type)
            VALUES (%s, %s, %s);
            """
            with conn.cursor() as cursor:
                cursor.execute(insert_sql, (source_info, data_type, target_table))
                conn.commit()
            logger.info(f"添加SHP文件导入记录: {source_info} -> {target_table}")

        return True

    except Exception as e:
        # 记录错误并返回失败
        logger.error(f"添加导入记录失败: {str(e)}", exc_info=True)
        return False
    finally:
        # 确保连接被关闭，防止连接泄漏
        if conn:
            conn.close()
            logger.debug("数据库连接已关闭")


def import_shp_to_postgis(table_name=None, schema="public", if_exists="fail", gdf=None):
    """
    将GeoDataFrame导入到PostGIS数据库
    
    该函数是实际执行导入操作的核心函数，它将GeoDataFrame导入到PostGIS数据库，
    并处理坐标系转换、字段添加、主键设置和空间索引创建等操作
    
    Args:
        table_name (str): 要导入到的目标表名，如"basins_2023"
        schema (str): 数据库模式名，默认为"public"
        if_exists (str): 当表已存在时的处理方式，可选值：
            - fail: 如果表存在则失败（默认）
            - replace: 如果表存在则替换
            - append: 如果表存在则追加数据
        gdf (GeoDataFrame): 要导入的GeoDataFrame对象
    
    Returns:
        dict: 导入结果，包含成功/失败信息和相关数据
    """
    engine = None
    conn = None
    try:
        # 验证输入数据是否有效
        if gdf is None or len(gdf) == 0:
            return {
                "success": False,
                "message": "没有提供有效的GeoDataFrame数据"
            }

        # 检查是否有流域名称字段，如果没有则尝试添加
        # 支持多种可能的流域名称字段命名
        basin_name_field = None
        for col in gdf.columns:
            if col.upper() in ['NAME', 'BASIN_NAME', 'BASINNAME', 'BASIN', 'RIVER', 'RIVER_NAME', 'RIVERNAME']:
                basin_name_field = col
                break

        # 如果没有找到流域名称字段，但有BASIN_ID字段，则使用BASIN_ID作为名称基础
        # 创建新的basin_name字段，值为"流域_" + BASIN_ID
        if basin_name_field is None:
            logger.warning("未找到流域名称字段，将尝试使用BASIN_ID生成名称")
            for col in gdf.columns:
                if col.upper() == 'BASIN_ID':
                    gdf['basin_name'] = '流域_' + gdf[col].astype(str)
                    basin_name_field = 'basin_name'
                    logger.info(f"已创建流域名称字段: {basin_name_field}")
                    break

        # 记录使用的流域名称字段
        if basin_name_field:
            logger.info(f"使用字段 {basin_name_field} 作为流域名称")
        else:
            logger.warning("未找到合适的流域名称字段，也未找到BASIN_ID字段，将不添加流域名称")

        # 添加geoserver_preview_url字段，初始值为空字符串
        # 该字段用于存储GeoServer预览链接
        if 'geoserver_preview_url' not in gdf.columns:
            logger.info("添加geoserver_preview_url字段，初始值为空")
            gdf['geoserver_preview_url'] = ''

        # 使用SQLAlchemy引擎连接water数据库
        engine = get_waterpostgres_engine()  # 这是water数据库连接

        # 检查表是否已存在
        check_query = f"""
        SELECT EXISTS (
            SELECT FROM information_schema.tables 
            WHERE table_schema = '{schema}' AND table_name = '{table_name}'
        );
        """
        exists_df = pd.read_sql(check_query, engine)
        table_exists = exists_df.iloc[0, 0]

        # 如果表已存在且if_exists设置为fail，则取消导入
        if table_exists and if_exists == 'fail':
            return {
                "success": False,
                "message": f"表 {schema}.{table_name} 已存在，导入操作已取消以保护现有数据",
                "table_exists": True
            }

        # 确保GeoDataFrame使用EPSG:4326坐标系（WGS84）
        # 如果没有指定坐标系，则默认设置为EPSG:4326
        # 如果坐标系不是EPSG:4326，则进行转换
        if gdf.crs is None:
            logger.warning("GeoDataFrame没有指定坐标系，默认设置为EPSG:4326")
            gdf.crs = "EPSG:4326"
        elif str(gdf.crs).upper() != "EPSG:4326":
            logger.info(f"转换坐标系: 从 {gdf.crs} 到 EPSG:4326")
            gdf = gdf.to_crs(epsg=4326)
            logger.info("坐标系转换完成")

        # 获取qgis数据库连接（空间数据存储在qgis数据库中）
        conn = get_qgispostgres_engine()  # 这是qgis数据库连接

        # 使用to_postgis方法将GeoDataFrame导入到PostGIS数据库
        logger.info(f"正在导入数据到表 {schema}.{table_name}")
        gdf.to_postgis(
            name=table_name,
            con=conn,  # 使用qgis数据库连接
            schema=schema,
            if_exists=if_exists,
            index=False  # 不导入DataFrame的索引列
        )

        # 获取导入的记录数
        record_count = len(gdf)

        # 创建空间索引和设置主键，提高查询性能
        try:
            # 使用qgis数据库连接
            with conn.connect() as connection:  # 使用qgis数据库连接
                # 检查BASIN_ID字段是否存在，用于设置主键
                id_field = None
                for col in gdf.columns:
                    if col.upper() == 'BASIN_ID':
                        id_field = col
                        break

                # 如果找到BASIN_ID字段，则设置为主键
                if id_field:
                    # 设置主键
                    logger.info(f"正在设置主键: {id_field}")
                    pk_sql = f'ALTER TABLE {schema}.{table_name} ADD PRIMARY KEY ("{id_field}");'
                    connection.execute(text(pk_sql))
                    logger.info(f"主键设置成功: {id_field}")
                else:
                    logger.warning("未找到BASIN_ID字段，跳过主键设置")

                # 创建空间索引，提高空间查询性能
                logger.info("正在创建空间索引")
                idx_sql = f'CREATE INDEX idx_{table_name}_geom ON {schema}.{table_name} USING GIST (geometry);'
                connection.execute(text(idx_sql))
                logger.info("空间索引创建成功")

                # 提交事务
                connection.commit()
        except Exception as e:
            # 记录警告但不中断流程，因为数据已经导入成功
            logger.warning(f"创建索引或主键时出错: {str(e)}")
            # 继续执行，不因为索引创建失败而中断整个导入过程

        # 返回成功结果
        return {
            "success": True,
            "message": f"成功导入 {record_count} 条记录到表 {schema}.{table_name}",
            "record_count": record_count,
            "table_name": f"{schema}.{table_name}",
            "columns": list(gdf.columns),
            "table_exists": table_exists
        }

    except Exception as e:
        # 记录错误并返回失败
        logger.error(f"导入SHP文件失败: {str(e)}")
        return {
            "success": False,
            "message": f"导入SHP文件失败: {str(e)}"
        }
    finally:
        # 确保连接和引擎被正确释放，防止资源泄漏
        if engine and hasattr(engine, 'dispose'):
            engine.dispose()
            logger.debug("water数据库引擎已释放")
        if conn and hasattr(conn, 'dispose'):
            conn.dispose()
            logger.debug("qgis数据库引擎已释放")


def update_geoserver_preview_urls(table_name, workspace, geoserver_url):
    """
    更新指定表中的GeoServer预览链接
    
    该函数为表中的每条记录生成GeoServer预览链接，并更新到geoserver_preview_url字段
    预览链接格式为WMS GetMap请求，可直接在浏览器中打开查看地图
    
    Args:
        table_name (str): 要更新的表名，如"basins_2023"
        workspace (str): GeoServer工作空间名称，如"hydro"
        geoserver_url (str): GeoServer服务器URL，如"http://localhost:8080/geoserver"
    
    Returns:
        bool: 是否成功更新预览链接
    """
    engine = None
    try:
        logger.info(f"开始更新表 {table_name} 的GeoServer预览链接")

        # 获取qgis数据库连接
        engine = get_qgispostgres_engine()
        with engine.connect() as connection:
            # 检查geoserver_preview_url字段是否存在
            check_column_sql = f"""
            SELECT EXISTS (
                SELECT FROM information_schema.columns 
                WHERE table_schema = 'public' 
                AND table_name = '{table_name}' 
                AND column_name = 'geoserver_preview_url'
            );
            """
            result = connection.execute(text(check_column_sql))
            column_exists = result.fetchone()[0]

            # 如果字段不存在，则添加
            if not column_exists:
                logger.info(f"表 {table_name} 中不存在geoserver_preview_url字段，正在添加")
                add_column_sql = f"""
                ALTER TABLE public.{table_name} 
                ADD COLUMN geoserver_preview_url VARCHAR(1000);
                """
                connection.execute(text(add_column_sql))
                logger.info("字段添加成功")
            else:
                # 如果字段已存在，修改其长度为1000，确保能存储完整URL
                logger.info(f"表 {table_name} 中已存在geoserver_preview_url字段，正在修改其长度")
                alter_column_sql = f"""
                ALTER TABLE public.{table_name} 
                ALTER COLUMN geoserver_preview_url TYPE VARCHAR(1000);
                """
                connection.execute(text(alter_column_sql))
                logger.info("字段长度修改成功")

            # 更新预览链接
            # 使用PostGIS函数ST_XMin、ST_YMin、ST_XMax、ST_YMax获取每个几何体的边界框
            # 将边界框坐标拼接到URL中，生成完整的WMS GetMap请求URL
            update_sql = f"""
            UPDATE public.{table_name} 
            SET geoserver_preview_url = '{geoserver_url}/{workspace}/wms?service=WMS&version=1.1.0&request=GetMap&layers={workspace}:{table_name}&styles=&bbox=' 
              || ST_XMin(geometry) || ',' || ST_YMin(geometry) || ',' || ST_XMax(geometry) || ',' || ST_YMax(geometry) 
              || '&width=768&height=576&srs=EPSG:4326&format=application/openlayers';
            """
            connection.execute(text(update_sql))
            connection.commit()
            logger.info(f"成功更新 {table_name} 表的GeoServer预览链接")

            return True

    except Exception as e:
        # 记录错误并返回失败
        logger.error(f"更新GeoServer预览链接失败: {str(e)}", exc_info=True)
        return False


# 测试代码部分
if __name__ == "__main__":
    # 设置日志，指定日志文件路径和轮转大小
    logger.add("logs/shp_util.log", rotation="10 MB")
    
    # 测试导入SHP文件
    # 读取示例SHP文件
    shp_path = r"D:\source pro\HydroPostGIS\data\basins_shp.shp"
    gdf = gpd.read_file(shp_path)
    # 导入到数据库，表名为zxx_basin_table，数据类型为basin
    import_shp(gdf, '测试', 'zxx_basin_table', 'basin')

    # 更新GeoServer预览链接（默认被注释）
    # 取消注释以测试update_geoserver_preview_urls函数
    # update_geoserver_preview_urls("zx_basin_table","zhixun_basin","http://172.20.7.86:8181/geoserver")
