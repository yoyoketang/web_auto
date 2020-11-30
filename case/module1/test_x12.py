from selenium import webdriver
import pytest
import time


# @pytest.fixture(name="driver")
# def open_browser():
#     driver = webdriver.Chrome()
#     yield driver
#     driver.quit()
#
#
# def test_a(driver):
#     # 重命名
#     driver.get("http://49.235.92.12:8200/users/login/")
#     time.sleep(2)
#
#
# def test_b(driver):
#     driver.get("http://49.235.92.12:8200/users/register/")
#     time.sleep(2)
#
#
