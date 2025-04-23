import dotenv

from openai import OpenAI

dotenv.load_dotenv()
import os

# 1创建openai客户端

clint = OpenAI(api_key=os.environ.get('DS_KEY'), base_url=os.environ.get('DS_KEY'))


while True:
    #获取人类的输入
    query = input("human:")