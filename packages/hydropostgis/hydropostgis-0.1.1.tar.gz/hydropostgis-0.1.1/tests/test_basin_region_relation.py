# -*- coding: utf-8 -*-
# @Author  : gaoyu
# @Time    : 2025/4/5 17:30
# @Function: 流域与行政区划相交服务单元测试

import unittest
import os
import sys
import pandas as pd
import json
from unittest.mock import patch, MagicMock

# 添加项目根目录到系统路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 导入被测试的模块
from core.gis_service.basin_region_relation import (
    get_regions_by_basin,
    get_basins_by_province,
    get_basins_by_city
)


class TestBasinRegionRelation(unittest.TestCase):
    """测试流域与行政区划相交服务的单元测试类"""

    def setUp(self):
        """测试前的准备工作"""
        # 模拟流域覆盖的行政区划数据
        self.mock_regions_data = pd.DataFrame({
            'ct_adcode': ['210200', '210300', '210400'],
            'ct_name': ['大连市', '鞍山市', '抚顺市'],
            'pr_adcode': ['210000', '210000', '210000'],
            'pr_name': ['辽宁省', '辽宁省', '辽宁省'],
            'coverage_ratio': [0.75, 0.45, 0.30]
        })
        
        # 模拟省份内的流域数据
        self.mock_province_basins_data = pd.DataFrame({
            'basin_id': ['NM000001', 'NM000002', 'NM000003'],
            'basin_name': ['某流域1', '某流域2', '某流域3'],
            'area': [1234.56, 2345.67, 3456.78],
            'coverage_ratio': [0.85, 0.65, 0.40]
        })
        
        # 模拟城市内的流域数据
        self.mock_city_basins_data = pd.DataFrame({
            'basin_id': ['NM000001', 'NM000004', 'NM000005'],
            'basin_name': ['某流域1', '某流域4', '某流域5'],
            'area': [1234.56, 456.78, 789.01],
            'coverage_ratio': [0.95, 0.75, 0.55]
        })
    
    @patch('core.gis_service.basin_region_relation.get_qgispostgres_data')
    @patch('core.gis_service.basin_region_relation.pd.read_sql')
    def test_get_regions_by_basin(self, mock_read_sql, mock_get_conn):
        """测试获取流域覆盖的行政区划"""
        # 设置模拟对象
        mock_conn = MagicMock()
        mock_get_conn.return_value = mock_conn  # 不再抛出异常
        
        # 设置模拟查询结果
        mock_read_sql.return_value = self.mock_regions_data
        
        # 调用被测试的函数
        result = get_regions_by_basin("NM000001")
        
        # 打印调试信息
        print(f"Result: {result}")
        
        # 验证结果
        self.assertTrue(result["success"])
        self.assertEqual(result["data"]["basin_id"], "NM000001")
        self.assertEqual(len(result["data"]["regions"]), 3)
        self.assertEqual(result["data"]["regions"][0]["region_code"], "210200")
        self.assertEqual(result["data"]["regions"][0]["region_name"], "大连市")
        self.assertEqual(result["data"]["regions"][0]["province_code"], "210000")
        self.assertEqual(result["data"]["regions"][0]["province_name"], "辽宁省")
        self.assertEqual(result["data"]["regions"][0]["coverage_ratio"], 0.75)
        
        # 验证SQL查询
        mock_read_sql.assert_called_once()
        args, kwargs = mock_read_sql.call_args
        self.assertIn("basins_shp", args[0])
        self.assertIn("admin_regions_city", args[0])
        self.assertIn("NM000001", args[0])
    
    @patch('core.gis_service.basin_region_relation.get_qgispostgres_data')
    @patch('core.gis_service.basin_region_relation.pd.read_sql')
    def test_get_regions_by_basin_empty(self, mock_read_sql, mock_get_conn):
        """测试获取流域覆盖的行政区划 - 空结果"""
        # 设置模拟对象
        mock_conn = MagicMock()
        mock_get_conn.return_value = mock_conn
        
        # 设置模拟查询结果 - 空DataFrame
        mock_read_sql.return_value = pd.DataFrame()
        
        # 调用被测试的函数
        result = get_regions_by_basin("NM999999")  # 不存在的流域ID
        
        # 验证结果
        self.assertTrue(result["success"])
        self.assertEqual(result["data"]["basin_id"], "NM999999")
        self.assertEqual(len(result["data"]["regions"]), 0)
        
        # 验证SQL查询
        mock_read_sql.assert_called_once()
    
    @patch('core.gis_service.basin_region_relation.get_qgispostgres_data')
    @patch('core.gis_service.basin_region_relation.pd.read_sql')
    def test_get_basins_by_province(self, mock_read_sql, mock_get_conn):
        """测试获取省份内的流域"""
        # 设置模拟对象
        mock_conn = MagicMock()
        mock_get_conn.return_value = mock_conn
        
        # 设置模拟查询结果
        mock_read_sql.return_value = self.mock_province_basins_data
        
        # 调用被测试的函数
        result = get_basins_by_province("210000")
        
        # 验证结果
        self.assertTrue(result["success"])
        self.assertEqual(result["data"]["province_code"], "210000")
        self.assertEqual(len(result["data"]["basins"]), 3)
        self.assertEqual(result["data"]["basins"][0]["basin_id"], "NM000001")
        self.assertEqual(result["data"]["basins"][0]["basin_name"], "某流域1")
        self.assertEqual(result["data"]["basins"][0]["area"], 1234.56)
        self.assertEqual(result["data"]["basins"][0]["coverage_ratio"], 0.85)
        
        # 验证SQL查询
        mock_read_sql.assert_called_once()
        args, kwargs = mock_read_sql.call_args
        self.assertIn("basins_shp", args[0])
        self.assertIn("admin_regions_province", args[0])
        self.assertIn("210000", args[0])
    
    @patch('core.gis_service.basin_region_relation.get_qgispostgres_data')
    @patch('core.gis_service.basin_region_relation.pd.read_sql')
    def test_get_basins_by_province_empty(self, mock_read_sql, mock_get_conn):
        """测试获取省份内的流域 - 空结果"""
        # 设置模拟对象
        mock_conn = MagicMock()
        mock_get_conn.return_value = mock_conn
        
        # 设置模拟查询结果 - 空DataFrame
        mock_read_sql.return_value = pd.DataFrame()
        
        # 调用被测试的函数
        result = get_basins_by_province("999999")  # 不存在的省份代码
        
        # 验证结果
        self.assertTrue(result["success"])
        self.assertEqual(result["data"]["province_code"], "999999")
        self.assertEqual(len(result["data"]["basins"]), 0)
        
        # 验证SQL查询
        mock_read_sql.assert_called_once()
    
    @patch('core.gis_service.basin_region_relation.get_qgispostgres_data')
    @patch('core.gis_service.basin_region_relation.pd.read_sql')
    def test_get_basins_by_city(self, mock_read_sql, mock_get_conn):
        """测试获取城市内的流域"""
        # 设置模拟对象
        mock_conn = MagicMock()
        mock_get_conn.return_value = mock_conn
        
        # 设置模拟查询结果
        mock_read_sql.return_value = self.mock_city_basins_data
        
        # 调用被测试的函数
        result = get_basins_by_city("210200")
        
        # 验证结果
        self.assertTrue(result["success"])
        self.assertEqual(result["data"]["city_code"], "210200")
        self.assertEqual(len(result["data"]["basins"]), 3)
        self.assertEqual(result["data"]["basins"][0]["basin_id"], "NM000001")
        self.assertEqual(result["data"]["basins"][0]["basin_name"], "某流域1")
        self.assertEqual(result["data"]["basins"][0]["area"], 1234.56)
        self.assertEqual(result["data"]["basins"][0]["coverage_ratio"], 0.95)
        
        # 验证SQL查询
        mock_read_sql.assert_called_once()
        args, kwargs = mock_read_sql.call_args
        self.assertIn("basins_shp", args[0])
        self.assertIn("admin_regions_city", args[0])
        self.assertIn("210200", args[0])
    
    @patch('core.gis_service.basin_region_relation.get_qgispostgres_data')
    @patch('core.gis_service.basin_region_relation.pd.read_sql')
    def test_get_basins_by_city_empty(self, mock_read_sql, mock_get_conn):
        """测试获取城市内的流域 - 空结果"""
        # 设置模拟对象
        mock_conn = MagicMock()
        mock_get_conn.return_value = mock_conn
        
        # 设置模拟查询结果 - 空DataFrame
        mock_read_sql.return_value = pd.DataFrame()
        
        # 调用被测试的函数
        result = get_basins_by_city("999999")  # 不存在的城市代码
        
        # 验证结果
        self.assertTrue(result["success"])
        self.assertEqual(result["data"]["city_code"], "999999")
        self.assertEqual(len(result["data"]["basins"]), 0)
        
        # 验证SQL查询
        mock_read_sql.assert_called_once()
    
    @patch('core.gis_service.basin_region_relation.get_qgispostgres_data')
    def test_get_regions_by_basin_exception(self, mock_get_conn):
        """测试获取流域覆盖的行政区划 - 异常情况"""
        # 设置模拟对象抛出异常
        mock_get_conn.side_effect = Exception("测试异常")
        
        # 调用被测试的函数
        result = get_regions_by_basin("NM000001")
        
        # 验证结果
        self.assertFalse(result["success"])
        self.assertIn("获取流域覆盖的行政区划失败", result["message"])
        self.assertIn("测试异常", result["message"])


if __name__ == '__main__':
    unittest.main()