import pytest


@pytest.fixture(scope="module", autouse=True)
def start():
    print("\n测试用例开启前的准备工作")


@pytest.fixture(scope="function", autouse=True)
def open():
    result = "success"
    return result


def test_1():
    print("测试用例1111111")



def test_2():
    print("测试用例222222222")
