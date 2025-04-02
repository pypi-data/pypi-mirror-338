# -*- coding: utf-8 -*-
# @Author  : gaoyu
# @Time    : 2025/4/5 16:30
# @Function: 行政区划服务单元测试

import unittest
import os
import sys
import pandas as pd
import json
from unittest.mock import patch, MagicMock

# 添加项目根目录到系统路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 导入被测试的模块
from core.gis_service.admin_region_service import (
    get_all_provinces,
    get_cities_by_province,
    get_region_by_code,
    get_districts_by_city,
    get_region_geometry_by_code
)


class TestAdminRegionService(unittest.TestCase):
    """测试行政区划服务的单元测试类"""

    def setUp(self):
        """测试前的准备工作"""
        # 模拟省份数据
        self.mock_provinces_data = pd.DataFrame({
            'code': ['110000', '120000', '130000'],
            'name': ['北京市', '天津市', '河北省'],
            'country_code': ['100000', '100000', '100000'],
            'country_name': ['中国', '中国', '中国']
        })
        
        # 模拟城市数据
        self.mock_cities_data = pd.DataFrame({
            'code': ['130100', '130200', '130300'],
            'name': ['石家庄市', '唐山市', '秦皇岛市'],
            'province_code': ['130000', '130000', '130000'],
            'province_name': ['河北省', '河北省', '河北省']
        })
        
        # 模拟区县数据
        self.mock_districts_data = pd.DataFrame({
            'dt_adcode': ['130102', '130103', '130104'],
            'dt_name': ['长安区', '桥西区', '桥东区'],
            'ct_adcode': ['130100', '130100', '130100'],
            'ct_name': ['石家庄市', '石家庄市', '石家庄市'],
            'pr_adcode': ['130000', '130000', '130000'],
            'pr_name': ['河北省', '河北省', '河北省']
        })
        
        # 模拟区域几何数据
        self.mock_geometry_data = pd.DataFrame({
            'code': ['130000'],
            'name': ['河北省'],
            'geometry': ['{"type":"Polygon","coordinates":[[[0,0],[1,0],[1,1],[0,1],[0,0]]]}'],
            'area_km2': [188000.25]
        })
    
    @patch('core.gis_service.admin_region_service.get_qgispostgres_data')
    @patch('core.gis_service.admin_region_service.pd.read_sql')
    def test_get_all_provinces(self, mock_read_sql, mock_get_conn):
        """测试获取所有省份"""
        # 设置模拟对象
        mock_conn = MagicMock()
        mock_get_conn.return_value = mock_conn
        
        # 设置模拟查询结果
        mock_read_sql.return_value = self.mock_provinces_data
        
        # 调用被测试的函数
        result = get_all_provinces()
        
        # 验证结果
        self.assertTrue(result["success"])
        self.assertEqual(len(result["data"]["provinces"]), 3)
        self.assertEqual(result["data"]["provinces"][0]["code"], "110000")
        self.assertEqual(result["data"]["provinces"][0]["name"], "北京市")
        
        # 验证SQL查询
        mock_read_sql.assert_called_once()
        args, kwargs = mock_read_sql.call_args
        self.assertIn("admin_regions_province", args[0])
    
    @patch('core.gis_service.admin_region_service.get_qgispostgres_data')
    @patch('core.gis_service.admin_region_service.pd.read_sql')
    def test_get_cities_by_province(self, mock_read_sql, mock_get_conn):
        """测试获取省份下的城市"""
        # 设置模拟对象
        mock_conn = MagicMock()
        mock_get_conn.return_value = mock_conn
        
        # 设置模拟查询结果
        mock_read_sql.return_value = self.mock_cities_data
        
        # 调用被测试的函数
        result = get_cities_by_province("130000")
        
        # 验证结果
        self.assertTrue(result["success"])
        self.assertEqual(result["data"]["province_code"], "130000")
        self.assertEqual(len(result["data"]["cities"]), 3)
        self.assertEqual(result["data"]["cities"][0]["code"], "130100")
        self.assertEqual(result["data"]["cities"][0]["name"], "石家庄市")
        
        # 验证SQL查询
        mock_read_sql.assert_called_once()
        args, kwargs = mock_read_sql.call_args
        self.assertIn("admin_regions_city", args[0])
        self.assertIn("130000", args[0])
    
    @patch('core.gis_service.admin_region_service.get_qgispostgres_data')
    @patch('core.gis_service.admin_region_service.pd.read_sql')
    def test_get_region_by_code_province(self, mock_read_sql, mock_get_conn):
        """测试获取省级行政区划信息"""
        # 设置模拟对象
        mock_conn = MagicMock()
        mock_get_conn.return_value = mock_conn
        
        # 设置模拟查询结果
        mock_read_sql.return_value = self.mock_geometry_data
        
        # 调用被测试的函数
        result = get_region_by_code("130000")
        
        # 验证结果
        self.assertTrue(result["success"])
        self.assertEqual(result["data"]["code"], "130000")
        self.assertEqual(result["data"]["name"], "河北省")
        self.assertIn("geometry", result["data"])
        self.assertIn("area_km2", result["data"])
        
        # 验证SQL查询
        mock_read_sql.assert_called_once()
        args, kwargs = mock_read_sql.call_args
        self.assertIn("admin_regions_province", args[0])
        self.assertIn("pr_adcode", args[0])
    
    @patch('core.gis_service.admin_region_service.get_qgispostgres_data')
    @patch('core.gis_service.admin_region_service.pd.read_sql')
    def test_get_districts_by_city(self, mock_read_sql, mock_get_conn):
        """测试获取城市下的区县"""
        # 设置模拟对象
        mock_conn = MagicMock()
        mock_get_conn.return_value = mock_conn
        
        # 设置模拟查询结果
        mock_read_sql.return_value = self.mock_districts_data
        
        # 调用被测试的函数
        result = get_districts_by_city("130100")
        
        # 验证结果
        self.assertTrue(result["success"])
        self.assertEqual(result["data"]["city_code"], "130100")
        self.assertEqual(len(result["data"]["districts"]), 3)
        self.assertEqual(result["data"]["districts"][0]["district_code"], "130102")
        self.assertEqual(result["data"]["districts"][0]["district_name"], "长安区")
        self.assertEqual(result["data"]["districts"][0]["city_code"], "130100")
        self.assertEqual(result["data"]["districts"][0]["city_name"], "石家庄市")
        
        # 验证SQL查询
        mock_read_sql.assert_called_once()
        args, kwargs = mock_read_sql.call_args
        self.assertIn("admin_regions_district", args[0])
        self.assertIn("130100", args[0])
    
    @patch('core.gis_service.admin_region_service.get_qgispostgres_data')
    @patch('core.gis_service.admin_region_service.pd.read_sql')
    def test_get_region_geometry_by_code_province(self, mock_read_sql, mock_get_conn):
        """测试获取省级行政区划几何数据"""
        # 设置模拟对象
        mock_conn = MagicMock()
        mock_get_conn.return_value = mock_conn
        
        # 设置模拟查询结果 - 确保字段名称与函数中预期的一致
        province_geometry_data = pd.DataFrame({
            'code': ['130000'],
            'name': ['河北省'],
            'geometry': ['{"type":"Polygon","coordinates":[[[0,0],[1,0],[1,1],[0,1],[0,0]]]}'],
            'area_km2': [188000.25]
        })
        
        # 关键修改：确保mock_read_sql返回我们设置的数据
        mock_read_sql.return_value = province_geometry_data
        
        # 调用被测试的函数
        result = get_region_geometry_by_code("130000")
        
        # 打印调试信息
        print(f"Mock read_sql called with: {mock_read_sql.call_args}")
        print(f"Result: {result}")
        
        # 验证结果
        self.assertTrue(result["success"])
        self.assertIsNotNone(result["data"], "返回的data不应为None")
        
        # 只有当data不为None时才验证其内容
        if result["data"] is not None:
            self.assertEqual(result["data"]["code"], "130000")
            self.assertEqual(result["data"]["name"], "河北省")
            self.assertEqual(result["data"]["level"], "province")
            self.assertIn("geometry", result["data"])
            self.assertIn("area_km2", result["data"])
        
        # 验证SQL查询
        mock_read_sql.assert_called_once()
        args, kwargs = mock_read_sql.call_args
        self.assertIn("admin_regions_province", args[0])
    
    @patch('core.gis_service.admin_region_service.get_qgispostgres_data')
    @patch('core.gis_service.admin_region_service.pd.read_sql')
    def test_get_region_geometry_by_code_city(self, mock_read_sql, mock_get_conn):
        """测试获取市级行政区划几何数据"""
        # 设置模拟对象
        mock_conn = MagicMock()
        mock_get_conn.return_value = mock_conn
        
        # 设置模拟查询结果 - 修改code为市级代码
        city_geometry_data = self.mock_geometry_data.copy()
        city_geometry_data['code'] = ['130100']
        city_geometry_data['name'] = ['石家庄市']
        mock_read_sql.return_value = city_geometry_data
        
        # 调用被测试的函数
        result = get_region_geometry_by_code("130100")
        
        # 验证结果
        self.assertTrue(result["success"])
        self.assertEqual(result["data"]["code"], "130100")
        self.assertEqual(result["data"]["name"], "石家庄市")
        self.assertEqual(result["data"]["level"], "city")
        
        # 验证SQL查询
        mock_read_sql.assert_called_once()
        args, kwargs = mock_read_sql.call_args
        self.assertIn("admin_regions_city", args[0])
    
    @patch('core.gis_service.admin_region_service.get_qgispostgres_data')
    @patch('core.gis_service.admin_region_service.pd.read_sql')
    def test_get_region_geometry_by_code_district(self, mock_read_sql, mock_get_conn):
        """测试获取区县级行政区划几何数据"""
        # 设置模拟对象
        mock_conn = MagicMock()
        mock_get_conn.return_value = mock_conn
        
        # 设置模拟查询结果 - 修改code为区县级代码
        district_geometry_data = self.mock_geometry_data.copy()
        district_geometry_data['code'] = ['130102']
        district_geometry_data['name'] = ['长安区']
        mock_read_sql.return_value = district_geometry_data
        
        # 调用被测试的函数
        result = get_region_geometry_by_code("130102")
        
        # 验证结果
        self.assertTrue(result["success"])
        self.assertEqual(result["data"]["code"], "130102")
        self.assertEqual(result["data"]["name"], "长安区")
        self.assertEqual(result["data"]["level"], "district")
        
        # 验证SQL查询
        mock_read_sql.assert_called_once()
        args, kwargs = mock_read_sql.call_args
        self.assertIn("admin_regions_district", args[0])
    
    @patch('core.gis_service.admin_region_service.get_qgispostgres_data')
    @patch('core.gis_service.admin_region_service.pd.read_sql')
    def test_get_region_geometry_by_code_invalid(self, mock_read_sql, mock_get_conn):
        """测试获取无效行政区划代码的几何数据"""
        # 设置模拟对象
        mock_conn = MagicMock()
        mock_get_conn.return_value = mock_conn
        
        # 调用被测试的函数 - 使用无效代码
        result = get_region_geometry_by_code("12345")
        
        # 验证结果
        self.assertFalse(result["success"])
        self.assertIn("无效的行政区划代码", result["message"])
        
        # 验证SQL查询未执行
        mock_read_sql.assert_not_called()
    
    @patch('core.gis_service.admin_region_service.get_qgispostgres_data')
    @patch('core.gis_service.admin_region_service.pd.read_sql')
    def test_get_region_geometry_by_code_empty_result(self, mock_read_sql, mock_get_conn):
        """测试获取不存在的行政区划几何数据"""
        # 设置模拟对象
        mock_conn = MagicMock()
        mock_get_conn.return_value = mock_conn
        
        # 设置模拟查询结果 - 空结果
        mock_read_sql.return_value = pd.DataFrame()
        
        # 调用被测试的函数
        result = get_region_geometry_by_code("130000")
        
        # 验证结果
        self.assertTrue(result["success"])
        self.assertIsNone(result["data"])
        
        # 验证SQL查询
        mock_read_sql.assert_called_once()


if __name__ == '__main__':
    unittest.main()