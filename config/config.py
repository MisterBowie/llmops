import os
from typing import Any
from .default_config import DEFAULT_CONFIG


def _get_env(key: str):
    """从环境变量中读取 没有则从DEFAULT_CONFIG中获取"""
    return os.getenv(key, DEFAULT_CONFIG.get(key))


def _get_bool_env(key: str) -> bool:
    value: str = _get_env(key)

    return value.lower() == "true" if value is not None else False


class Config:
    def __init__(self):
        # 关闭CSRF
        self.WTF_CSRF_ENABLED = _get_bool_env("WTF_CSRF_ENABLED")
        # 配置数据库
        self.SQLALCHEMY_DATABASE_URI = _get_env("SQLALCHEMY_DATABASE_URI")
        self.SQLALCHEMY_ENGINE_OPTIONS = {
            "pool_size": int(_get_env("SQLALCHEMY_POOL_SIZE")),
            "pool_recycle": int(_get_env("SQLALCHEMY_POOL_RECYCLE")),
        }
        self.SQLALCHEMY_ECHO = (_get_bool_env("SQLALCHEMY_ECHO"),)
