from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class CompletionReq(FlaskForm):
    """聊天接口请求验证"""

    query = StringField("query", validators=[
        DataRequired(message="用户提问是必填的"),
        Length(max=1000, message="用户提问最大1000")
    ])

