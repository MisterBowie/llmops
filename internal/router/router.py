from flask import Flask, Blueprint
from internal.handler import AppHandler
from dataclasses import dataclass
from injector import Injector, inject


@inject
@dataclass
class Router:
    """路由"""
    app_handler: AppHandler

    def register_router(self, app: Flask):
        """注册路由"""
        # 1. 创建一个蓝图
        bp = Blueprint("llmpos", __name__, url_prefix="")

        # 将Url与对应的控制器方法做
        # view_func 如果是app_handler.ping() 则代表的是使用返回值
        bp.add_url_rule("/ping", view_func=self.app_handler.ping)
        bp.add_url_rule("/app/completion", methods=["POST"], view_func=self.app_handler.completion)
        bp.add_url_rule("/apps/<uuid:app_id>/debug", methods=["POST"], view_func=self.app_handler.debug)
        bp.add_url_rule("/app", methods=["POST"], view_func=self.app_handler.create_app)
        bp.add_url_rule("/app/<uuid:id>", methods=["GET"], view_func=self.app_handler.get_app)
        bp.add_url_rule("/app/<uuid:id>", methods=["PUT"], view_func=self.app_handler.update_app)
        bp.add_url_rule("/app/<uuid:id>", methods=["DELETE"], view_func=self.app_handler.delete_app)
        # 在应用上去注册蓝图
        app.register_blueprint(bp)
