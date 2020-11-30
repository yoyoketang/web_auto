import pytest


# 测试数据
test_datas = [
        {"username": "yoyo1", "password": "123456", "expected": "success!"},
        {"username": "yoyo2", "password": "123456", "expected": "success!"},
        {"username": "yoyo3", "password": "123456", "expected": "success!"},
]


@pytest.fixture(params=test_datas, ids=[
    "测试用例1，username: yoyo1",
    "测试用例1，username: yoyo2",
    "测试用例1，username: yoyo3",
])
def login(request):
    '''登录'''
    print("登录账号：%s, 密码: %s" % (request.param["username"], request.param["password"]))
    result = {"code": 0, "msg": "success!"}
    return request.param, result


def test_login(login):
    test_input, result = login
    assert test_input["expected"] == result["msg"]



