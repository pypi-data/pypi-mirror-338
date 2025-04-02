# -*- coding: utf-8 -*-
# @Author  : gaoyu
# @Time    : 2024/4/2 15:30
# @Function: 流域与站点关系服务测试

import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import sys
import os

# 添加项目根目录到系统路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.gis_service.basin_station_relation import get_basin_by_code, get_reservoirs_geometry


class TestBasinStationRelation(unittest.TestCase):
    """测试流域与站点关系服务"""

    def setUp(self):
        """测试前的准备工作"""
        # 模拟流域数据
        self.mock_basin_data = pd.DataFrame({
            'basin_id': ['NM000001'],
            'basin_name': ['测试流域'],
            'area': [1234.56],
            'geometry': ['{"type":"Polygon","coordinates":[[[120.0,30.0],[121.0,30.0],[121.0,31.0],[120.0,31.0],[120.0,30.0]]]}']
        })

        # 模拟水库数据
        self.mock_reservoirs_data = pd.DataFrame({
            'geometry': ['{"type":"MultiPolygon","coordinates":[[[[120.0,30.0],[121.0,30.0],[121.0,31.0],[120.0,31.0],[120.0,30.0]]]]}'],
            'count': [3],
            'reservoir_ids': [['6300899', '6121599', '9235299']],
            'reservoir_names': [['水库1', '水库2', '水库3']]
        })

        # 模拟空数据
        self.mock_empty_data = pd.DataFrame()

    @patch('core.gis_service.basin_station_relation.get_qgispostgres_data')
    @patch('core.gis_service.basin_station_relation.pd.read_sql')
    def test_get_basin_by_code(self, mock_read_sql, mock_get_conn):
        """测试获取流域几何数据"""
        # 设置模拟对象
        mock_conn = MagicMock()
        mock_get_conn.return_value = mock_conn
        
        # 设置模拟查询结果
        mock_read_sql.return_value = self.mock_basin_data
        
        # 调用被测试的函数
        result = get_basin_by_code("NM000001")
        
        # 验证结果
        self.assertTrue(result["success"])
        self.assertEqual(result["data"]["basin_id"], "NM000001")
        self.assertEqual(result["data"]["basin_name"], "测试流域")
        self.assertEqual(result["data"]["area"], 1234.56)
        self.assertIn("Polygon", result["data"]["geometry"])
        
        # 验证SQL查询
        mock_read_sql.assert_called_once()
        args, kwargs = mock_read_sql.call_args
        self.assertIn("basins_shp", args[0])
        self.assertIn("NM000001", args[0])
        self.assertIn("ST_AsGeoJSON", args[0])

    @patch('core.gis_service.basin_station_relation.get_qgispostgres_data')
    @patch('core.gis_service.basin_station_relation.pd.read_sql')
    def test_get_basin_by_code_empty(self, mock_read_sql, mock_get_conn):
        """测试获取流域几何数据 - 空结果"""
        # 设置模拟对象
        mock_conn = MagicMock()
        mock_get_conn.return_value = mock_conn
        
        # 设置模拟查询结果 - 空DataFrame
        mock_read_sql.return_value = self.mock_empty_data
        
        # 调用被测试的函数
        result = get_basin_by_code("NM999999")  # 不存在的流域ID
        
        # 验证结果
        self.assertTrue(result["success"])
        self.assertIsNone(result["data"])
        self.assertIn("未找到编码为", result["message"])
        
        # 验证SQL查询
        mock_read_sql.assert_called_once()

    @patch('core.gis_service.basin_station_relation.get_qgispostgres_data')
    def test_get_basin_by_code_exception(self, mock_get_conn):
        """测试获取流域几何数据 - 异常情况"""
        # 设置模拟对象抛出异常
        mock_get_conn.side_effect = Exception("测试异常")
        
        # 调用被测试的函数
        result = get_basin_by_code("NM000001")
        
        # 验证结果
        self.assertFalse(result["success"])
        self.assertIn("获取流域几何数据失败", result["message"])
        self.assertIn("测试异常", result["message"])

    @patch('core.gis_service.basin_station_relation.get_qgispostgres_data')
    @patch('core.gis_service.basin_station_relation.pd.read_sql')
    def test_get_reservoirs_geometry(self, mock_read_sql, mock_get_conn):
        """测试获取水库几何数据"""
        # 设置模拟对象
        mock_conn = MagicMock()
        mock_get_conn.return_value = mock_conn
        
        # 设置模拟查询结果
        mock_read_sql.return_value = self.mock_reservoirs_data
        
        # 调用被测试的函数
        result = get_reservoirs_geometry(["6300899", "6121599", "9235299"])
        
        # 验证结果
        self.assertTrue(result["success"])
        self.assertEqual(result["data"]["count"], 3)
        self.assertEqual(result["data"]["reservoir_ids"], ["6300899", "6121599", "9235299"])
        self.assertEqual(result["data"]["reservoir_names"], ["水库1", "水库2", "水库3"])
        self.assertIn("MultiPolygon", result["data"]["geometry"])
        
        # 验证SQL查询
        mock_read_sql.assert_called_once()
        args, kwargs = mock_read_sql.call_args
        self.assertIn("st_stbprp_b", args[0])
        self.assertIn("6300899", args[0])
        self.assertIn("ST_Union", args[0])

    @patch('core.gis_service.basin_station_relation.get_qgispostgres_data')
    @patch('core.gis_service.basin_station_relation.pd.read_sql')
    def test_get_reservoirs_geometry_empty(self, mock_read_sql, mock_get_conn):
        """测试获取水库几何数据 - 空结果"""
        # 设置模拟对象
        mock_conn = MagicMock()
        mock_get_conn.return_value = mock_conn
        
        # 设置模拟查询结果 - 空DataFrame
        mock_read_sql.return_value = self.mock_empty_data
        
        # 调用被测试的函数
        result = get_reservoirs_geometry(["9999999"])  # 不存在的水库ID
        
        # 验证结果
        self.assertTrue(result["success"])
        self.assertIsNone(result["data"])
        self.assertIn("未找到指定编码的水库", result["message"])
        
        # 验证SQL查询
        mock_read_sql.assert_called_once()

    @patch('core.gis_service.basin_station_relation.get_qgispostgres_data')
    def test_get_reservoirs_geometry_exception(self, mock_get_conn):
        """测试获取水库几何数据 - 异常情况"""
        # 设置模拟对象抛出异常
        mock_get_conn.side_effect = Exception("测试异常")
        
        # 调用被测试的函数
        result = get_reservoirs_geometry(["6300899"])
        
        # 验证结果
        self.assertFalse(result["success"])
        self.assertIn("获取水库几何数据失败", result["message"])
        self.assertIn("测试异常", result["message"])

    def test_get_reservoirs_geometry_invalid_params(self):
        """测试获取水库几何数据 - 无效参数"""
        # 测试空列表
        result = get_reservoirs_geometry([])
        self.assertFalse(result["success"])
        self.assertIn("请提供有效的水库编码列表", result["message"])
        
        # 测试非列表参数
        result = get_reservoirs_geometry("6300899")
        self.assertFalse(result["success"])
        self.assertIn("请提供有效的水库编码列表", result["message"])


if __name__ == '__main__':
    unittest.main()