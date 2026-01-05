import uvicorn
from config import Config
from dotenv import load_dotenv
from internal.server.http import create_app
from internal.router.router import router
from internal.extension.datebase_extension import db

load_dotenv()

conf = Config()

app = create_app(conf=conf, db=db)
app.include_router(router)

if __name__ == '__main__':
    uvicorn.run("app.http.app:app", host="0.0.0.0", port=8003, reload=True)
