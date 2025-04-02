# -*- coding: utf-8 -*-
# @Author  : gaoyu
# @Time    : 2025/4/15 10:30
# @Function: HydroPostGIS安装配置

from setuptools import setup, find_packages
import os

# 读取README文件作为长描�?
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="hydropostgis",
    version="0.1.1",
    author="denghaozhe",
    author_email="22d2h2z@gmal.com",
    description="水文地理信息服务平台",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitcode.com/dlut-water/HydroPostGIS.git",
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: GIS",
    ],
    python_requires=">=3.8",
    install_requires=[
        "geopandas==1.0.1",
        "Shapely==2.0.7",
        "pandas==2.2.3",
        "psycopg2==2.9.9",
        "SQLAlchemy==2.0.40",
        "loguru==0.7.2",
        "python-dotenv==1.1.0",
        "Requests==2.32.3",
        "urllib3==2.3.0",
    ],
    include_package_data=True,
    package_data={
        "": ["*.json", "*.yaml", "*.yml"],
    },
)
