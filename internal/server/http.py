from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from config import Config
from internal.exception import CustomException
from pkg.response import Response, HttpCode
import os

from internal.model import App
from pkg.sqlalchemy import SQLAlchemy


def create_app(conf: Config, db: SQLAlchemy) -> FastAPI:
    """创建 FastAPI 应用"""
    app = FastAPI(title="LLMOps API", debug=conf.DEBUG if hasattr(conf, 'DEBUG') else False)

    # 初始化数据库
    db.init(
        database_uri=conf.SQLALCHEMY_DATABASE_URI,
        engine_options=conf.SQLALCHEMY_ENGINE_OPTIONS
    )
    # 确保模型被加载
    _ = App
    # 创建表
    db.create_all()

    # CORS 中间件
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # 自定义异常处理
    @app.exception_handler(CustomException)
    async def custom_exception_handler(request: Request, exc: CustomException):
        return JSONResponse(
            status_code=200,
            content=Response(
                code=exc.code,
                message=exc.message,
                data=exc.data if exc.data is not None else {},
            )
        )

    # 通用异常处理
    @app.exception_handler(Exception)
    async def general_exception_handler(request: Request, exc: Exception):
        debug = os.getenv("FASTAPI_ENV") == "development"
        if debug:
            raise exc
        return JSONResponse(
            status_code=200,
            content=Response(
                code=HttpCode.FAIL,
                message=str(exc),
                data=None,
            )
        )

    return app
