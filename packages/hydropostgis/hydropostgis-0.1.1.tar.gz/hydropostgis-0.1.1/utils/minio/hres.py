# -*- coding: utf-8 -*-
# @Author  : gaoyu
# @Time    : 2025/1/26 12:28 PM
# @Function:
# @File : minio_util_with_cert.py
# 获取自签名证书
# openssl s_client -connect 172.20.4.2:9000
# openssl x509 -in certificate.crt -text -noout

import os
import traceback

import urllib3
from loguru import logger
from minio import Minio
from minio.error import S3Error

from config import MINIO_COLD_ENDPOINT, MINIO_COLD_ACCESS_KEY, MINIO_COLD_SECRET_KEY

# 创建一个客户端
client = Minio(
    MINIO_COLD_ENDPOINT.replace('https://', '').replace('http://', ''),
    MINIO_COLD_ACCESS_KEY,
    MINIO_COLD_SECRET_KEY,
    secure=True,
    http_client=urllib3.PoolManager(
        cert_reqs='CERT_NONE',  # 禁用 SSL 验证
        assert_hostname=False,  # 不验证主机名
    )
)


def minio_file_upload_with_cert(
        bucket: str,
        remote_path: str,
        local_path: str,
        cert_file: str = None,
        file_size_range: int = 59
):
    """
    文件上传到 MinIO
    :param file_size_range:
    :param bucket: 存储桶名称
    :param remote_path: 远程存储路径
    :param local_path: 本地文件路径
    :param cert_file: 自签名证书路径（可选）
    :return: None
    """
    try:
        # 如果提供了自签名证书，设置环境变量用于信任
        if cert_file and os.path.exists(cert_file):
            os.environ['SSL_CERT_FILE'] = cert_file
            logger.info(f"使用自签名证书：{cert_file}")

        # 检查存储桶是否存在
        if not client.bucket_exists(bucket):
            client.make_bucket(bucket)
            logger.info(f"存储桶 '{bucket}' 创建成功")
        else:
            logger.warning(f"存储桶 '{bucket}' 已存在")

        # 获取文件大小（单位：字节）
        file_size = os.stat(local_path).st_size
        threshold = file_size_range * 1024 * 1024  # 32MB

        if file_size <= threshold:
            # 方法 1：小文件（≤ 32MB）
            logger.info(f"文件 '{local_path}' 小于 {file_size_range}MB")
            client.fput_object(bucket, remote_path, local_path)
        else:
            # 方法 2：大文件（> 32MB）
            logger.info(f"文件 '{local_path}' 大于 {file_size_range}MB")
            with open(local_path, "rb") as file_data:
                client.put_object(bucket, remote_path, file_data, file_size, part_size=64 * 1024 * 1024)

        logger.info(f"文件 '{local_path}' 成功上传至存储桶 '{bucket}' 的路径 '{remote_path}'")

    except S3Error as e:
        logger.error(f"MinIO 上传文件异常: {e}")
        logger.debug(traceback.format_exc())
        raise Exception(f"MinIO 上传文件异常: {e}")


def download_file_with_cert(
        bucket: str,
        file_name: str,
        file_path: str
):
    """
    文件下载
    :param end_point:
    :param access_key:
    :param secret_key:
    :param bucket:
    :param file_name:
    :param file_path:
    :return:
    """
    # Make 'asiatrip' bucket if not exist.
    found = client.bucket_exists(bucket)
    if not found:
        logger.info("Bucket {} not exists".format(bucket))
        return
    try:
        client.fget_object(
            bucket_name=bucket,
            object_name=file_name,
            file_path=file_path
        )
        logger.info("file '{0}' is successfully download".format(file_name))
        return file_path
    except S3Error as err:
        logger.error("download_failed:", err)


def _convert_size(size_bytes):
    """
    将字节大小转换为人类可读的格式
    """
    if size_bytes is None or size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.log(size_bytes, 1024))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"


def list_files_with_cert(
        bucket: str,
        prefix: str
):
    """
    列出 MinIO 中的文件
    :param bucket: 存储桶名称
    :param prefix: 文件前缀
    :return: 文件信息列表，包含文件名、大小、最后修改时间、是否为目录等信息
    """
    resp = client.list_objects(bucket_name=bucket, prefix=prefix, recursive=False)
    rtn_list = []
    for item in resp:
        file_info = {
            'name': item.object_name,  # 文件名
            'size': item.size if hasattr(item, 'size') else 0,  # 文件大小（字节）
            'last_modified': item.last_modified,  # 最后修改时间
            'etag': item.etag,  # ETag
            'is_dir': item.is_dir,  # 是否为目录
            'content_type': item.content_type,  # 内容类型
            'owner_id': item.owner_id if hasattr(item, 'owner_id') else None,  # 所有者ID
            'owner_name': item.owner_name if hasattr(item, 'owner_name') else None,  # 所有者名称
            'size_human': _convert_size(item.size if hasattr(item, 'size') else 0)  # 人类可读的文件大小
        }
        rtn_list.append(file_info)
    return rtn_list


# 在文件顶部添加 import
import math


def file_exists_with_cert(
        bucket: str,
        file_path: str
):
    """
    文件是否存在
    :param end_point:
    :param access_key:
    :param secret_key:
    :param bucket:
    :param file_path:
    :return:
    """
    # Make 'asiatrip' bucket if not exist.
    resp = client.list_objects(bucket_name=bucket, prefix=file_path)
    for item in resp:
        logger.info(item.object_name)
        return True
    return False
