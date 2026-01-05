from pydantic import BaseModel, Field


class CompletionReq(BaseModel):
    """聊天接口请求验证"""
    query: str = Field(..., max_length=1000, description="用户提问")

