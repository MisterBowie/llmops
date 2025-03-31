import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import (ChatPromptTemplate, PromptTemplate)
from langchain_core.output_parsers import StrOutputParser
from typing import Any
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from operator import itemgetter


def retrieval(query: str) -> str:
    """模拟一个检索器，传入query，输出文本"""
    print("执行检索", query)
    return "我叫VV，是一名AI应用开发工程师"


# 1.编排Prompt
prompt = ChatPromptTemplate.from_template("""请根据用户的提问回他问题，可以参考上下文进行回复
<context>
{context}
</context>
用户的问题是:{query}
""")

# 构建大语言模型
llm = ChatOpenAI(model="deepseek-chat", api_key=os.environ.get("DS_KEY"), base_url=os.environ.get("DS_API_BASE"))

parser = StrOutputParser()

chain = (
    RunnablePassthrough.assign(context=lambda query: retrieval(query)) |
    prompt |
    llm |
    parser
)
content = chain.invoke({"query": "你好我叫什么"})

print(content)
