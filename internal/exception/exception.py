from pkg.response.http_code import HttpCode
from typing import Any
from dataclasses import field


class CustomException(Exception):
    code: HttpCode = HttpCode.FAIL
    message: str = ""
    data: Any = field(default_factory=dict)

    def __init__(self, message: str = None, data: Any = None):
        super().__init__()
        self.message = message
        self.data = data


class FailException(CustomException):
    """通用失败异常"""
    pass


class NotFoundException(CustomException):
    """未找到数据异常"""
    code: HttpCode.NOT_FOUND


class UnauthorizedException(CustomException):
    """未授权异常"""
    code: HttpCode.UNAUTHORIZED


class ForbiddenException(CustomException):
    """禁止访问异常"""
    code: HttpCode.FORBIDDEN


class BadRequestException(CustomException):
    """请求参数异常"""
    code: HttpCode.BAD_REQUEST


class ValidationException(CustomException):
    """请求参数异常"""
    code: HttpCode.VALIDATE_ERROR
