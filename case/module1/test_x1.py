


#
# def test_x(login):
#     print("xxxxxxxxxx")

import pytest

# 测试数据，存放在list
user_data = ["user1", "user2"]


@pytest.fixture(scope="function", params=user_data)
def register_users(request):
    '''注册用户参数化'''
    print("用户开始注册：%s" % request.param)
    result = "success"
    return request.param, result


@pytest.mark.parametrize("mail", ["123@qq.com", "2222@qq.com"])
def test_registe_mail(register_users, mail):
    user, result = register_users
    print("注册用户：%s, 结果：%s" % (user, result))
    print("注册邮箱：%s" % mail)




def test_register(register_users):
    user, result = register_users
    print(user)
    assert result == "success"




@pytest.mark.parametrize("user", ["user1", "user2"])
def test_registe_x(user):
    print("注册用户：%s" % user)


