from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from contextlib import contextmanager


class SQLAlchemy(_SQLAlchemy):

    @contextmanager
    def auto_commit(self):
        """重写flask sqlalchemy 实现自动提交"""
        try:
            yield
            self.session.commit()
        except Exception as e:
            raise e
