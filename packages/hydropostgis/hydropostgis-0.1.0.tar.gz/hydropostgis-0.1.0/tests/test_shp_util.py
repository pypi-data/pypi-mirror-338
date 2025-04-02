# -*- coding: utf-8 -*-
# @Author  : gaoyu
# @Time    : 2025/4/5 15:30
# @Function: SHP文件处理工具单元测试

import unittest
import os
import sys
import pandas as pd
import geopandas as gpd
from unittest.mock import patch, MagicMock
from shapely.geometry import Polygon

# 添加项目根目录到系统路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 导入被测试的模块
from core.gis_service.shp_util import (
    import_shp, 
    add_shp_import_record, 
    import_shp_to_postgis,
    update_geoserver_preview_urls
)


class TestShpUtil(unittest.TestCase):
    """测试SHP文件处理工具的单元测试类"""

    def setUp(self):
        """测试前的准备工作"""
        # 创建一个简单的GeoDataFrame用于测试
        geometry = [Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])]
        data = {
            'BASIN_ID': ['TEST001'],
            'NAME': ['测试流域'],
            'geometry': geometry
        }
        self.test_gdf = gpd.GeoDataFrame(data, geometry='geometry', crs="EPSG:4326")
        
        # 模拟数据库查询结果
        self.mock_exists_df = pd.DataFrame([{'exists': False}])
        
    @patch('core.gis_service.shp_util.import_shp_to_postgis')
    @patch('core.gis_service.shp_util.add_shp_import_record')
    def test_import_shp_success(self, mock_add_record, mock_import):
        """测试成功导入SHP文件的情况"""
        # 设置模拟函数的返回值
        mock_import.return_value = {
            "success": True,
            "message": "成功导入 1 条记录到表 public.test_table",
            "record_count": 1,
            "table_name": "public.test_table",
            "columns": ["BASIN_ID", "NAME", "geometry"],
            "table_exists": False
        }
        mock_add_record.return_value = True
        
        # 调用被测试的函数
        result = import_shp(
            gdf=self.test_gdf,
            source_info="测试数据",
            table_name="test_table",
            data_type="basin"
        )
        
        # 验证结果
        self.assertTrue(result["success"])
        self.assertEqual(result["record_count"], 1)
        self.assertEqual(result["table_name"], "public.test_table")
        
        # 验证模拟函数是否被正确调用
        mock_import.assert_called_once()
        mock_add_record.assert_called_once_with("测试数据", "test_table", "basin")
    
    @patch('core.gis_service.shp_util.import_shp_to_postgis')
    @patch('core.gis_service.shp_util.add_shp_import_record')
    def test_import_shp_failure(self, mock_add_record, mock_import):
        """测试导入SHP文件失败的情况"""
        # 设置模拟函数的返回值
        mock_import.return_value = {
            "success": False,
            "message": "导入SHP文件失败: 表已存在"
        }
        
        # 调用被测试的函数
        result = import_shp(
            gdf=self.test_gdf,
            source_info="测试数据",
            table_name="test_table",
            data_type="basin"
        )
        
        # 验证结果
        self.assertFalse(result["success"])
        self.assertIn("导入SHP文件失败", result["message"])
        
        # 验证add_shp_import_record没有被调用
        mock_add_record.assert_not_called()
    
    @patch('core.gis_service.shp_util.get_waterpostgres_data')
    def test_add_shp_import_record_new(self, mock_get_conn):
        """测试添加新的导入记录"""
        # 设置模拟对象
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_get_conn.return_value = mock_conn
        
        # 设置模拟查询结果
        mock_cursor.fetchone.side_effect = [(True,), (False,)]  # 表存在，记录不存在
        
        # 调用被测试的函数
        result = add_shp_import_record(
            source_info="测试数据",
            target_table="test_table",
            data_type="basin"
        )
        
        # 验证结果
        self.assertTrue(result)
        
        # 验证SQL执行
        self.assertEqual(mock_cursor.execute.call_count, 3)  # 检查表、检查记录、插入记录
        
        # 验证最后一次execute是插入操作
        args, kwargs = mock_cursor.execute.call_args_list[-1]
        self.assertIn("INSERT INTO", args[0])
    
    @patch('core.gis_service.shp_util.get_waterpostgres_data')
    def test_add_shp_import_record_update(self, mock_get_conn):
        """测试更新现有的导入记录"""
        # 设置模拟对象
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_get_conn.return_value = mock_conn
        
        # 设置模拟查询结果
        mock_cursor.fetchone.side_effect = [(True,), (True,)]  # 表存在，记录存在
        
        # 调用被测试的函数
        result = add_shp_import_record(
            source_info="更新的测试数据",
            target_table="test_table",
            data_type="basin"
        )
        
        # 验证结果
        self.assertTrue(result)
        
        # 验证SQL执行
        self.assertEqual(mock_cursor.execute.call_count, 3)  # 检查表、检查记录、更新记录
        
        # 验证最后一次execute是更新操作
        args, kwargs = mock_cursor.execute.call_args_list[-1]
        self.assertIn("UPDATE", args[0])
    
    @patch('core.gis_service.shp_util.get_waterpostgres_engine')
    @patch('core.gis_service.shp_util.get_qgispostgres_engine')
    @patch('core.gis_service.shp_util.pd.read_sql')
    def test_import_shp_to_postgis_success(self, mock_read_sql, mock_qgis_engine, mock_water_engine):
        """测试成功将GeoDataFrame导入到PostGIS"""
        # 设置模拟对象
        mock_water_engine_obj = MagicMock()
        mock_qgis_engine_obj = MagicMock()
        mock_water_engine.return_value = mock_water_engine_obj
        mock_qgis_engine.return_value = mock_qgis_engine_obj
        
        # 模拟表不存在的查询结果
        mock_read_sql.return_value = pd.DataFrame([{'exists': False}])
        
        # 模拟连接和执行
        mock_connection = MagicMock()
        mock_qgis_engine_obj.connect.return_value.__enter__.return_value = mock_connection
        
        # 调用被测试的函数
        with patch.object(self.test_gdf, 'to_postgis') as mock_to_postgis:
            result = import_shp_to_postgis(
                table_name="test_table",
                schema="public",
                if_exists="append",
                gdf=self.test_gdf
            )
        
        # 验证结果
        self.assertTrue(result["success"])
        self.assertEqual(result["record_count"], 1)
        self.assertEqual(result["table_name"], "public.test_table")
        
        # 验证to_postgis被调用
        mock_to_postgis.assert_called_once()
        
        # 验证空间索引创建
        mock_connection.execute.assert_called()
    
    @patch('core.gis_service.shp_util.get_qgispostgres_engine')
    def test_update_geoserver_preview_urls(self, mock_engine):
        """测试更新GeoServer预览链接"""
        # 设置模拟对象
        mock_engine_obj = MagicMock()
        mock_engine.return_value = mock_engine_obj
        
        # 模拟连接和执行
        mock_connection = MagicMock()
        mock_engine_obj.connect.return_value.__enter__.return_value = mock_connection
        
        # 模拟字段存在的查询结果
        mock_result = MagicMock()
        mock_result.fetchone.return_value = (True,)
        mock_connection.execute.return_value = mock_result
        
        # 调用被测试的函数
        result = update_geoserver_preview_urls(
            table_name="test_table",
            workspace="test_workspace",
            geoserver_url="http://172.20.7.86:8181/geoserver"
        )
        
        # 验证结果
        self.assertTrue(result)
        
        # 验证SQL执行
        self.assertEqual(mock_connection.execute.call_count, 3)  # 检查字段、修改字段长度、更新URL
        
        # 验证最后一次execute是更新URL操作
        args, kwargs = mock_connection.execute.call_args_list[-1]
        self.assertIn("UPDATE", args[0].text)
        self.assertIn("geoserver_preview_url", args[0].text)


if __name__ == '__main__':
    unittest.main()