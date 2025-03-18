
from pkg.response.http_code import HttpCode
import pytest

class TestAppHandler:
    """应用控制器测试"""

    @pytest.mark.parametrize("query", [None,"你好", "你好呀"])
    def test_completion(self,query, client):
        resp = client.post("/app/completion", json={"query": query})
        print("响应内容", resp.json)
        if(query is not None):
            assert resp.json.get("code") == HttpCode.SUCCESS
        else:
            assert resp.json.get("code") == HttpCode.VALIDATE_ERROR
       
