import dataclasses
import uuid

from flask import request
from injector import inject
from openai import OpenAI
import os
from internal.schema.app_schema import CompletionReq
from internal.exception import FailException
from internal.service import AppService
from pkg.response.response import json, success_json, validate_error_json, success_message
from dataclasses import dataclass


@inject
@dataclass
class AppHandler:
    """应用控制器"""
    app_service: AppService

    def create_app(self):
        """创建应用"""
        app = self.app_service.create_app()
        return success_message(f"应用已经创建id:{app.id}")

    def get_app(self, id: uuid.UUID):
        """获取应用"""
        app = self.app_service.get_app(id)
        return success_json(app.to_dict())

    def update_app(self, id: uuid.UUID):
        app = self.app_service.update_app(id)
        return success_message(f"名称已经修改，新的名字为:{app.name}")

    def delete_app(self, id: uuid.UUID):
        app = self.app_service.delete_app(id)
        return success_message(f"应用已删除，id为:{app.id}")

    def completion(self):
        """聊天窗口"""
        # 1. 提取接口中获取的输入
        # 2. 构建openAi客户端。并发起请求
        # 3. 得到请求响应返回给前端
        req = CompletionReq()
        if not req.validate():
            return validate_error_json(req.errors)
        clint = OpenAI(api_key=os.environ.get("DS_KEY"), base_url=os.environ.get("DS_API_BASE"))

        completions = clint.chat.completions.create(model="deepseek-chat", messages=[
            {"role": "system", "content": "你是一个简单的客服机器人，可以简单的回复用户的问题"},
            {"role": "user", "content": req.query.data}
        ])
        content = completions.choices[0].message.content
        return success_json(content)

    def ping(self):
        raise FailException(message="数据未找到")
        # return {"ping": "pong"}
