import pytest

'''
request  pytest的内置fixture
作用：连接测试的上下文
'''

test_data = ["user1", "user2"]


@pytest.fixture(params=test_data)
def register_users(request):
     # 获取当前的测试数据
     user = request.param
     print("\n拿着这个账号去注册：%s"%user)
     result = "success"
     return user, result


def test_register(register_users):
    user, result = register_users
    print("在测试用例里面里面获取到当前测试数据：%s"%user)
    print(result)
    assert result == "success"

def test_register_x(register_users, request):
    print(dict(request.keywords))
    print(request.node.keywords)
    print(dict(request.node.keywords))



@pytest.mark.parametrize("user", ["user1", "user2"])
def test_user(user):
    print("获取测试参数：%s"%user)


@pytest.mark.parametrize("email", ["111@qq.com", "222@qq.com"])
def test_register_mail(register_users, email):
    user, result = register_users
    print(user, result)
    print(email)


