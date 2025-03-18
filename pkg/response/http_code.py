from enum import Enum


class HttpCode(str,Enum):
    """HTTP基本业务状态码"""
    SUCCESS = "success"
    FAIL = "fail"
    NOT_FOUND = "not_found"
    UNAUTHORIZED = "unauthorized"
    FORBIDDEN = "forbidden"
    VALIDATE_ERROR = "validate_error"
    BAD_REQUEST = "bad_request"
