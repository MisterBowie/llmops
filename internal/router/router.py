from uuid import UUID
from fastapi import APIRouter, Depends
from internal.handler import AppHandler
from internal.schema.app_schema import CompletionReq


router = APIRouter()


def get_app_handler() -> AppHandler:
    """获取 AppHandler 依赖"""
    from internal.extension.datebase_extension import db
    from internal.service import AppService
    app_service = AppService(db=db)
    return AppHandler(app_service=app_service)


@router.get("/ping")
def ping(handler: AppHandler = Depends(get_app_handler)):
    return handler.ping()


@router.post("/app/completion")
def completion(req: CompletionReq, handler: AppHandler = Depends(get_app_handler)):
    return handler.completion(req)


@router.post("/apps/{app_id}/debug")
def debug(app_id: UUID, handler: AppHandler = Depends(get_app_handler)):
    return handler.debug()


@router.post("/app")
def create_app(handler: AppHandler = Depends(get_app_handler)):
    return handler.create_app()


@router.get("/app/{id}")
def get_app(id: UUID, handler: AppHandler = Depends(get_app_handler)):
    return handler.get_app(id)


@router.put("/app/{id}")
def update_app(id: UUID, handler: AppHandler = Depends(get_app_handler)):
    return handler.update_app(id)


@router.delete("/app/{id}")
def delete_app(id: UUID, handler: AppHandler = Depends(get_app_handler)):
    return handler.delete_app(id)
