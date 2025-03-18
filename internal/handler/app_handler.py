from flask import request
from openai import OpenAI
import os
from internal.schema.app_schema import CompletionReq
from internal.exception import FailException


class AppHandler:
    """应用控制器"""

    def completion(self):
        """聊天窗口"""
        # 1. 提取接口中获取的输入
        # 2. 构建openAi客户端。并发起请求
        # 3. 得到请求响应返回给前端
        req = CompletionReq()
        if not req.validate():
            return req.errors
        clint = OpenAI(api_key=os.environ.get("DS_KEY"), base_url=os.environ.get("DS_API_BASE"))

        completions = clint.chat.completions.create(model="deepseek-chat", messages=[
            {"role": "system", "content": "你是一个简单的客服机器人，可以简单的回复用户的问题"},
            {"role": "user", "content": req.query.data}
        ])
        content = completions.choices[0].message.content
        return content

    def ping(self):
        
        raise FailException(message="数据未找到")
        # return {"ping": "pong"}
