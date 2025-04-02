import os
import json
import argparse
from pathlib import Path
from loguru import logger

# 配置日志
logger.add("geojson_to_gpkg.log", rotation="1 day", level="INFO")

def fix_geojson_geometry(geojson_data):
    """
    修复GeoJSON中的几何问题，如非闭合线环
    
    Args:
        geojson_data (dict): GeoJSON数据
    
    Returns:
        dict: 修复后的GeoJSON数据
    """
    if 'type' in geojson_data and geojson_data['type'] == 'FeatureCollection' and 'features' in geojson_data:
        for feature in geojson_data['features']:
            if 'geometry' in feature and feature['geometry'] is not None:
                geometry = feature['geometry']
                
                # 修复多边形的非闭合线环
                if geometry['type'] == 'Polygon':
                    for ring_idx, ring in enumerate(geometry['coordinates']):
                        # 检查环是否闭合（首尾坐标相同）
                        if ring and len(ring) > 3:  # 至少需要4个点才能形成有效的环
                            if ring[0] != ring[-1]:
                                # 如果不闭合，添加第一个点到末尾
                                logger.warning(f"发现非闭合线环，自动修复")
                                geometry['coordinates'][ring_idx].append(ring[0])
                
                # 修复多多边形的非闭合线环
                elif geometry['type'] == 'MultiPolygon':
                    for poly_idx, polygon in enumerate(geometry['coordinates']):
                        for ring_idx, ring in enumerate(polygon):
                            # 检查环是否闭合
                            if ring and len(ring) > 3:
                                if ring[0] != ring[-1]:
                                    # 如果不闭合，添加第一个点到末尾
                                    logger.warning(f"发现非闭合线环，自动修复")
                                    geometry['coordinates'][poly_idx][ring_idx].append(ring[0])
    
    return geojson_data

def convert_geojson_to_gpkg(geojson_file, output_dir="output", create_polygons=True, color_field=None):
    """
    将GeoJSON文件转换为GeoPackage格式，可选择创建填充区域
    
    Args:
        geojson_file (str): GeoJSON文件路径
        output_dir (str): 输出目录
        create_polygons (bool): 是否创建填充区域
        color_field (str): 用于颜色渲染的字段名
    """
    try:
        # 转换为Path对象
        geojson_path = Path(geojson_file)
        output_path = Path(output_dir)

        # 确保输入文件存在
        if not geojson_path.exists():
            logger.error(f"GeoJSON文件不存在: {geojson_path}")
            return None

        # 确保输出目录存在
        output_path.mkdir(parents=True, exist_ok=True)

        # 构建输出文件路径
        gpkg_file = output_path / f"{geojson_path.stem}.gpkg"

        logger.info(f"开始转换: {geojson_path} -> {gpkg_file}")

        # 尝试修复GeoJSON文件
        try:
            # 读取GeoJSON文件
            with open(geojson_path, 'r', encoding='utf-8') as f:
                geojson_data = json.load(f)
            
            # 修复几何问题
            fixed_geojson = fix_geojson_geometry(geojson_data)
            
            # 创建临时修复文件
            fixed_geojson_path = geojson_path.parent / f"{geojson_path.stem}_fixed.geojson"
            with open(fixed_geojson_path, 'w', encoding='utf-8') as f:
                json.dump(fixed_geojson, f)
            
            logger.info(f"已创建修复后的GeoJSON文件: {fixed_geojson_path}")
            
            # 使用修复后的文件
            use_path = fixed_geojson_path
        except Exception as e:
            logger.warning(f"修复GeoJSON失败，将使用原始文件: {str(e)}")
            use_path = geojson_path

        # 直接使用geopandas读取并转换
        try:
            import geopandas as gpd
            import shapely
            import os
            
            # 设置OGR配置，允许非闭合环
            os.environ['OGR_GEOMETRY_ACCEPT_UNCLOSED_RING'] = 'YES'
            
            # 读取GeoJSON文件，设置容错参数
            gdf = gpd.read_file(use_path)
            
            # 尝试修复无效的几何图形
            if hasattr(shapely, 'make_valid'):
                gdf['geometry'] = gdf['geometry'].apply(lambda geom: shapely.make_valid(geom) if geom else geom)
            
            # 保存为GeoPackage
            gdf.to_file(gpkg_file, driver="GPKG")
            
            # 清理临时文件
            if use_path != geojson_path and use_path.exists():
                try:
                    os.remove(use_path)
                    logger.info(f"已删除临时文件: {use_path}")
                except:
                    pass
            
            logger.success(f"转换完成: {gpkg_file}")
            return str(gpkg_file)
            
        except ImportError as e:
            logger.error(f"缺少必要的库: {str(e)}")
            logger.info("请安装必要的库: pip install geopandas shapely fiona pyogrio")
            return None
        
    except Exception as e:
        logger.error(f"转换失败: {str(e)}")
        import traceback
        logger.error(traceback.format_exc())
        return None

def main():
    """
    主函数，用于处理命令行参数并执行转换
    """
    parser = argparse.ArgumentParser(description='将GeoJSON文件转换为GeoPackage格式')
    parser.add_argument('input', help='GeoJSON文件路径')
    parser.add_argument('--output-dir', '-o', default='output', help='输出目录')
    parser.add_argument('--fix-geometry', '-f', action='store_true', help='修复几何问题')
    args = parser.parse_args()
    
    result = convert_geojson_to_gpkg(args.input, args.output_dir, create_polygons=False)
    if result:
        print(f"转换成功: {result}")
    else:
        print("转换失败")

if __name__ == "__main__":
    main()