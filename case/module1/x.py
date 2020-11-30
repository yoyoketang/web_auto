# import pytest
#
#
# @pytest.fixture()
# def start():
#     print("数据准备：XXXXX")
#     yield
#     print("数据清理操作")
#
#
# def test_01(start):
#     print("测试用例1111111111")
#
#
# def test_02(start):
#     print("测试用例22222222222")
#
#
# def test_03(start):
#     print("测试用例33333333333")
#
#
#
# from selenium import webdriver
# import pytest
# import time
#
#
# @pytest.fixture(scope="module")
# def open_broswer():
#     '''打开浏览器'''
#     driver = webdriver.Chrome()
#     yield driver
#     driver.close()
#
#
# def test_blog(open_broswer):
#     '''打开我的blog: https://www.cnblogs.com/yoyoketang/'''
#     open_broswer.get("https://www.cnblogs.com/yoyoketang/")
#     time.sleep(3)


x = ["hello", "worle"]
a, b =x
print(a)
print(b)