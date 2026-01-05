"""
FastAPI 依赖注入 Demo
"""
from fastapi import FastAPI, Depends
from dataclasses import dataclass


# ============ 1. 基础依赖注入 ============
def get_db_connection():
    """简单的函数依赖"""
    print("创建数据库连接...")
    return {"connection": "database_connection"}


# ============ 2. 带参数的依赖 ============
def get_pagination(page: int = 1, size: int = 10):
    """从查询参数自动获取分页信息"""
    return {"page": page, "size": size, "offset": (page - 1) * size}


# ============ 3. 类作为依赖 ============
class DatabaseSession:
    """类依赖 - 使用 __init__ 注入"""
    def __init__(self):
        self.session_id = "session_123"
        print(f"创建 session: {self.session_id}")
    
    def query(self, model):
        return f"查询 {model}"


# ============ 4. 依赖链（嵌套依赖） ============
@dataclass
class UserService:
    """Service 依赖于 DatabaseSession"""
    db: DatabaseSession
    
    def get_user(self, user_id: int):
        return f"User {user_id} from {self.db.session_id}"


def get_user_service(db: DatabaseSession = Depends(DatabaseSession)):
    """工厂函数 - 创建 Service 并注入其依赖"""
    return UserService(db=db)


# ============ 5. yield 依赖（资源管理） ============
def get_db_with_cleanup():
    """使用 yield 实现资源清理（类似 with 语句）"""
    print("开始: 创建连接")
    db = {"conn": "active"}
    try:
        yield db  # 请求处理期间使用
    finally:
        print("结束: 关闭连接")  # 请求结束后自动执行


# ============ 创建应用 ============
app = FastAPI(title="依赖注入 Demo")


@app.get("/demo1")
def demo_basic(db=Depends(get_db_connection)):
    """基础依赖注入"""
    return {"db": db}


@app.get("/demo2")
def demo_pagination(pagination=Depends(get_pagination)):
    """带参数的依赖 - 访问 /demo2?page=2&size=20"""
    return pagination


@app.get("/demo3")
def demo_class(db: DatabaseSession = Depends()):
    """类依赖 - Depends() 空参数会自动实例化类"""
    result = db.query("User")
    return {"session": db.session_id, "result": result}


@app.get("/demo4")
def demo_chain(service: UserService = Depends(get_user_service)):
    """嵌套依赖 - Service 自动获得 DatabaseSession"""
    return {"user": service.get_user(1)}


@app.get("/demo5")
def demo_yield(db=Depends(get_db_with_cleanup)):
    """yield 依赖 - 请求结束后自动清理资源"""
    return {"status": db["conn"]}


# ============ 你的项目中的应用方式 ============
"""
在你的项目 router.py 中:

def get_app_handler() -> AppHandler:
    from internal.extension.datebase_extension import db
    from internal.service import AppService
    app_service = AppService(db=db)        # 手动注入 db 到 Service
    return AppHandler(app_service=app_service)  # 手动注入 Service 到 Handler


@router.get("/app/{id}")
def get_app(id: UUID, handler: AppHandler = Depends(get_app_handler)):
    # FastAPI 自动调用 get_app_handler() 获取 handler
    return handler.get_app(id)


更优雅的方式（使用类依赖）:

class AppHandlerDep:
    def __init__(self):
        from internal.extension.datebase_extension import db
        from internal.service import AppService
        self.service = AppService(db=db)
    
    def create_app(self):
        return self.service.create_app()

@router.post("/app")
def create(handler: AppHandlerDep = Depends()):
    return handler.create_app()
"""


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8004)
