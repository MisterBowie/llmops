from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base
from contextlib import contextmanager


Base = declarative_base()


class SQLAlchemy:
    def __init__(self, database_uri: str = None, engine_options: dict = None):
        self._engine = None
        self._session_factory = None
        self._Session = None
        self._database_uri = database_uri
        self._engine_options = engine_options or {}

    def init(self, database_uri: str, engine_options: dict = None):
        """初始化数据库连接"""
        self._database_uri = database_uri
        self._engine_options = engine_options or {}
        self._engine = create_engine(database_uri, **self._engine_options)
        self._session_factory = sessionmaker(bind=self._engine)
        self._Session = scoped_session(self._session_factory)

    @property
    def engine(self):
        return self._engine

    @property
    def session(self):
        return self._Session()

    def create_all(self):
        """创建所有表"""
        Base.metadata.create_all(self._engine)

    @contextmanager
    def auto_commit(self):
        """自动提交上下文管理器"""
        session = self.session
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
