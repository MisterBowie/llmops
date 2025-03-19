from flask import Flask
from internal.router import Router
from config import Config
from internal.exception import CustomException
from pkg.response import json, Response, HttpCode
import os


from internal.model import App
from pkg.sqlalchemy import SQLAlchemy


class Http(Flask):
    def __init__(self, *args, conf: Config, db: SQLAlchemy, router: Router, **kwargs):
        # 1.调用父类的构造的初始化
        super().__init__(*args, **kwargs)

        # 初始化应用配置
        self.config.from_object(conf)

        # 注册绑定异常
        self.register_error_handler(Exception, self._register_error_handler)

        # 注册数据库
        db.init_app(self)
        # 创建表
        with self.app_context():
            _ = App()
            db.create_all()
        # 注册应用路由
        router.register_router(self)

    def _register_error_handler(self, error: Exception):
        # 判断异常是不是我们的自定义异常

        if isinstance(error, CustomException):
            return json(Response(
                code=error.code,
                message=error.message,
                data=error.data if error.data is not None else {},
            ))
        # 2.如果不是我们的自定义异常，则有可能是程序、数据库抛出的异常，也可以提取信息，设置为FAIL状态码
        if self.debug or os.getenv("FLASK_ENV") == "development":
            raise error
        else:
            return json(Response(
                code=HttpCode.FAIL,
                message=str(error),
                data=None,
            ))
