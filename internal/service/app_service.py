"""
应用服务service
"""
import uuid
from dataclasses import dataclass

from internal.model import App
from pkg.sqlalchemy import SQLAlchemy


@dataclass
class AppService:
    """应用服务逻辑"""
    db: SQLAlchemy

    def create_app(self) -> App:
        """创建APP"""
        # 创建模型的实体类
        app = App(name="测试机器人", account_id=uuid.uuid4(), icon="", description="这是一个简单的聊天机器人")
        with self.db.auto_commit() as session:
            # 将实体类添加到session中
            session.add(app)
        return app

    def get_app(self, id: uuid.UUID) -> App:
        """获取APP"""
        session = self.db.session
        app = session.query(App).filter(App.id == id).first()
        session.close()
        return app

    def update_app(self, id: uuid.UUID) -> App:
        with self.db.auto_commit() as session:
            app = session.query(App).filter(App.id == id).first()
            app.name = "新的聊天机器人"
        return app

    def delete_app(self, id: uuid.UUID) -> App:
        with self.db.auto_commit() as session:
            app = session.query(App).filter(App.id == id).first()
            session.delete(app)
        return app

