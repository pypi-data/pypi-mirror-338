#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2025/2/14 10:26
# @Author   : songzb

import yaml
import datetime
import os
from loguru import logger
from collections import OrderedDict


def read_config(config_path):
    """"读取配置"""
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config


def update_config(config, config_path):
    """"更新配置"""
    with open(config_path, 'w') as yaml_file:
        yaml.dump(config, yaml_file)
    return None


def init_logger(version, log_env, use_vllm):
    """
    初始化日志存储
    """
    now = datetime.datetime.now()
    log_env_desc = "online" if log_env else "test"
    if log_env:
        vllm_desc = "_VLLM" if use_vllm else ""
        log_dir = os.path.expanduser(f"../nohup_logs/{now.year}_{now.month}_{now.day}")
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        log_file = os.path.join(log_dir, f"{version}_{now.year}-{now.month}-{now.day}_{log_env_desc}{vllm_desc}.log")
        logger.add(log_file, enqueue=True, rotation="1 day")
        logger.info("【开始存储日志】")
        logger.info(log_file)
        return logger
    else:
        return logger


def contains(items, targets, exist=True):
    """
    exist为True：则认为targets中有items中的元素 返回True 有在就是True
    exist为False：则认为items中的元素都在targets中 返回True 都在才是True
    """
    if exist:
        for item in items:
            if item in targets:
                return True
        return False
    else:
        for item in items:
            if item not in targets:
                return False
        return True


def unique_sort(items, sort=False):
    """
    列表去重并且排序
    """
    if isinstance(items, list):
        unique_items = list(OrderedDict.fromkeys(items))
        if sort:
            unique_items.sort()
        return unique_items
    else:
        return items


def has_level_type(level_list, key, extra=None):
    """

    """
    if extra:
        return True if key in [lev.split("-")[0] for lev in level_list] or contains(extra, level_list) else False
    else:
        return True if key in [lev.split("-")[0] for lev in level_list] else False
