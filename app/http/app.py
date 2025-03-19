from injector import Injector, Module, Binder
from internal.server import Http
from internal.router import Router
from config import Config
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from app.http.module import ExtensionModule

load_dotenv()

conf = Config()

injector = Injector([ExtensionModule])
app = Http(__name__, conf=conf, db=injector.get(SQLAlchemy), router=injector.get(Router))

if __name__ == '__main__':
    app.run(debug=True, port=8000)
