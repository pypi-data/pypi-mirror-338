# -*- coding: utf-8 -*-
# @Author  : gaoyu
# @Time    : 2023/7/18 2:57 PM
# @Function:
import json
import re


def get_json_field(item_object, key):
    """
    取json字段
    Args:
        item_object:
        key:

    Returns:

    """
    if key is None:
        return None
    else:
        return None if (item_object.get(key) is None) else item_object[key]


def get_json_field_code(item_object, key):
    """
    取编码中的英文和数字
    Args:
        item_object:
        key:

    Returns:

    """
    return re.sub(r'[^a-zA-Z0-9]', '', str(get_json_field(item_object, key)))


def get_json_field_zh_cn(item_object, key):
    """
    取编码中的中文
    Args:
        item_object:
        key:

    Returns:

    """
    return re.sub(r'[a-zA-Z0-9]', '', str(get_json_field(item_object, key)))


def json_to_post_json_data(_data):
    """
    纯json转为post接口json
    Args:
        _data:

    Returns:

    """
    return json.dumps(_data, ensure_ascii=False)


def df_to_post_json_data(df):
    """
    df转为json
    Args:
        df:

    Returns:

    """
    return json.loads(df.to_json(orient="records", force_ascii=False))


def df_to_post_body(df):
    """
    df转为post body
    Args:
        df:

    Returns:

    """
    return json_to_post_json_data(df_to_post_json_data(df))
