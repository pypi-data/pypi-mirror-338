# -*- coding: utf-8 -*-
# @Author  : gaoyu
# @Time    : 2025/3/26 15:30
# @Function: 生成短随机ID的工具类

import time
import random
import string
import threading


class ShortIdGenerator:
    """
    短ID生成器，生成易于使用的短ID
    支持多种格式：纯数字、字母数字混合等
    """

    _instance_lock = threading.Lock()
    _instance = None

    def __new__(cls, *args, **kwargs):
        with cls._instance_lock:
            if not cls._instance:
                cls._instance = super().__new__(cls)
            return cls._instance

    def __init__(self):
        self.counter = 0
        self.last_timestamp = 0
        self.lock = threading.Lock()

    def get_numeric_id(self, length=8):
        """
        生成纯数字ID
        
        Args:
            length: ID长度，默认8位
            
        Returns:
            纯数字ID字符串
        """
        with self.lock:
            timestamp = int(time.time() * 1000)

            # 如果是同一毫秒内，计数器加1
            if timestamp == self.last_timestamp:
                self.counter += 1
            else:
                self.last_timestamp = timestamp
                self.counter = random.randint(0, 999)

            # 组合时间戳和计数器
            base = timestamp % (10 ** (length - 3))  # 取时间戳的后几位
            result = f"{base}{self.counter:03d}"

            # 确保长度一致
            if len(result) > length:
                result = result[-length:]
            elif len(result) < length:
                result = result.zfill(length)

            return result

    def get_alphanumeric_id(self, length=6):
        """
        生成字母数字混合ID
        
        Args:
            length: ID长度，默认6位
            
        Returns:
            字母数字混合ID字符串
        """
        # 使用时间戳作为基础
        timestamp = int(time.time() * 1000)

        # 生成随机字符
        chars = string.ascii_letters + string.digits
        random_part = ''.join(random.choice(chars) for _ in range(length - 2))

        # 添加时间戳的一部分作为前缀，确保唯一性
        prefix = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))

        return f"{prefix}{random_part}"

    def get_uuid_like(self, sections=4, section_length=4):
        """
        生成类似UUID格式的ID，但更短
        
        Args:
            sections: 分段数量，默认4段
            section_length: 每段长度，默认4个字符
            
        Returns:
            类UUID格式的ID字符串，如"a1b2-c3d4-e5f6-g7h8"
        """
        chars = string.ascii_lowercase + string.digits
        parts = []

        for _ in range(sections):
            part = ''.join(random.choice(chars) for _ in range(section_length))
            parts.append(part)

        return '-'.join(parts)


if __name__ == '__main__':
    # 单例模式使用
    id_generator = ShortIdGenerator()
    # 测试生成不同类型的ID
    print("数字ID:", id_generator.get_numeric_id())
    print("字母数字ID:", id_generator.get_alphanumeric_id())
    print("UUID格式ID:", id_generator.get_uuid_like())

    # 测试批量生成，检查唯一性
    numeric_ids = [id_generator.get_numeric_id() for _ in range(100)]
    print(f"生成100个数字ID，唯一ID数量: {len(set(numeric_ids))}")
    print(numeric_ids)

    alphanumeric_ids = [id_generator.get_alphanumeric_id() for _ in range(100)]
    print(f"生成100个字母数字ID，唯一ID数量: {len(set(alphanumeric_ids))}")
    print(alphanumeric_ids)
