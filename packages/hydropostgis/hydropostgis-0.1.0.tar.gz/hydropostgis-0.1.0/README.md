# HydroPostGIS - 水文地理信息服务平台

## 项目简介

HydroPostGIS是一个基于PostGIS的水文地理信息服务平台，旨在提供行政区、流域面、测站点等地理信息的存储、维护和服务化能力。本项目是知汛平台的基础服务之一，提供地理信息的服务化解决方案。

## 技术栈

- **数据存储**：PostgreSQL + PostGIS
- **空间数据格式**：GeoPackage, Shapefile, GeoJSON
- **服务发布**：GeoServer
- **开发工具**：Python, GDAL
- **客户端支持**：QGIS, ArcGIS

## 功能模块

### 1. 行政区管理

- 行政区数据的PostGIS存储
- 通过QGIS、ArcGIS进行维护
- 页面展示
- GeoServer同步
- 面平均雨量计算

### 2. 流域面管理

- 流域面数据的PostGIS存储
- 通过QGIS、ArcGIS进行维护
- 页面展示
- GeoServer同步
- 流域DEM的CDN缓存
- 面平均雨量计算

### 3. 测站点管理

- 测站点数据的PostGIS存储
- 与流域面的空间关系计算
- 基于权重的面平均雨量计算
- 数据异常检验

## 项目结构
HydroPostGIS/
├── api/                    # API接口层，提供RESTful服务
├── config.py               # 全局配置文件
├── core/                   # 核心业务逻辑
│   └── gis_service/        # GIS服务相关功能
│       ├── basin_region_relation.py    # 流域与行政区关系
│       ├── basin_station_relation.py   # 流域与测站关系
│       └── region_station_relation.py  # 行政区与测站关系
├── docs/                   # 项目文档
├── service/                # 服务层，连接API和核心层
├── utils/                  # 工具函数
│   ├── format_transform/   # 格式转换工具
│   │   └── geojson_to_gpkg.py  # GeoJSON转GeoPackage
│   ├── id_generator.py     # ID生成器
│   ├── json_util.py        # JSON处理工具
│   ├── minio/              # MinIO对象存储工具
│   │   ├── hres.py         # 高分辨率文件处理
│   │   └── minio_util_with_cert.py  # MinIO工具(带证书)
│   └── postgres_util.py    # PostgreSQL数据库工具
├── .env                    # 环境变量配置
└── requirements.txt        # 项目依赖

## 安装与配置

### 环境要求
- Python 3.8+
- PostgreSQL 12+ with PostGIS 3.0+
- GeoServer 2.19+