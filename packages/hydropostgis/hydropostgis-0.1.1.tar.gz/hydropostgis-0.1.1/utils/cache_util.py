# -*- coding: utf-8 -*-
# @Author  : gaoyu
# @Time    : 2025/4/10 10:30
# @Function: 缓存工具

import functools
from datetime import datetime, timedelta
from loguru import logger

# 缓存装饰器
def cache_result(seconds=3600):
    """缓存函数结果的装饰器，默认缓存1小时
    
    该装饰器用于缓存函数的返回结果，减少重复查询数据库的开销
    缓存基于函数参数创建键值，并在指定时间内返回缓存的结果
    
    Args:
        seconds (int): 缓存有效时间，单位为秒，默认3600秒(1小时)
        
    Returns:
        function: 装饰器函数
    """
    cache = {}

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = str(args) + str(kwargs)
            now = datetime.now()

            # 检查缓存是否存在且未过期
            if key in cache and now - cache[key]['time'] < timedelta(seconds=seconds):
                logger.debug(f"从缓存获取结果: {func.__name__}{args}{kwargs}")
                return cache[key]['result']

            # 执行函数并缓存结果
            logger.debug(f"执行函数并缓存结果: {func.__name__}{args}{kwargs}")
            result = func(*args, **kwargs)
            cache[key] = {'result': result, 'time': now}
            return result

        return wrapper

    return decorator