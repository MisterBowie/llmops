import os
import dotenv

from openai import OpenAI

dotenv.load_dotenv()


class ConversationSummaryBufferMemory:
    """摘要缓冲混合记忆类"""
    # max_token 用于判断是否需要生成新的摘要
    # summary 用户存储的摘要
    
    def __init__(self, llm, max_token_limit=1000):
        self.llm = llm
        self.max_token_limit = max_token_limit
        self.messages = []


# 1创建openai客户端
clint = OpenAI(api_key=os.environ.get('DS_KEY'),
               base_url=os.environ.get('DS_API_BASE'))


while True:
    # 获取人类的输入
    query = input("human:")

    if query == "q":
        break

    # 想AI获取生成的内容
    response = clint.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "user", "content": query}
        ],
        stream=True,
    )

    for chunk in response:
        content = chunk.choices[0].delta.content
        if content is None:
            break
        print(content, end="", flush=True)
    print("")
