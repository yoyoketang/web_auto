import pytest


@pytest.fixture(scope="module")
def start():
    print("\n数据准备：00000000000")
    yield
    print("数据清理操作：xxxxxxxxxx")


def test_01(start):
    print("用例1111111111111")


def test_02(start):
    print("用例222222222222")


def test_03(start):
    print("用例33333333333333")

