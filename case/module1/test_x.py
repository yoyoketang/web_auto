import time
import pytest


@pytest.fixture(scope="module", autouse=True)
def start():
    print('\n----->开始执行moule----')


@pytest.fixture(scope="function", autouse=True)
def open():
    print("--->执行open")
    return "hello"


def test_01():
    print('-----------用例01--------------')


def test_02():
    print('-----------用例02--------------')



import pytest


def login(username, password):
    '''登录'''
    print("登录账号：%s, 密码: %s" % (username, password))
    return {"code": 0, "msg": "success!"}

# 测试数据
test_datas = [
    ({"username": "yoyo1", "password": "123456"}, "success!"),
    ({"username": "yoyo2", "password": "123456"}, "success!"),
    ({"username": "yoyo3", "password": "123456"}, "success!"),
]


@pytest.mark.parametrize("test_input,expected",
                         test_datas,
                         ids=[
                             "输入正确账号，密码，登录成功",
                             "输入错误账号，密码，登录失败",
                             "输入正确账号，密码，登录成功",
                         ]
                         )
def test_login(test_input, expected):
    '''测试登录用例'''
    # 获取函数返回结果
    result = login(test_input["username"], test_input["password"])
    # 断言
    assert result["msg"] == expected