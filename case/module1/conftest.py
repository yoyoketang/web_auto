import pytest


@pytest.fixture(scope="function")
def step1():
    print("步骤1")


@pytest.fixture()
def step2():
    print("步骤2")


@pytest.fixture()
def step3():
    print("步骤3")


@pytest.fixture(scope="class")
def first():
    print("获取用户名")
    a = "yoyo"
    return a


@pytest.fixture()
def second(first):
    print("再获取密码")
    b = "123456"
    return (first, b)


@pytest.fixture(scope="module")
def three():
    print("用例前置：aaaaaaaaaa")



@pytest.fixture(scope="session")
def four():
    print("会话级别，整个会话只执行一次")


# @pytest.fixture(scope="session")
# def driver():
#     from selenium import webdriver
#     browser = webdriver.Chrome()
#     return browser




# hooks函数

def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        # print(item.nodeid)
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")