from selenium import webdriver
import pytest
import time


# @pytest.fixture()
# def open_browser():
#     driver = webdriver.Chrome()
#     yield driver
#     driver.quit()
#
#
# def test_a(open_browser):
#     open_browser.get("http://49.235.92.12:8200/users/login/")
#     time.sleep(2)
#
#
# def test_b(open_browser):
#     open_browser.get("http://49.235.92.12:8200/users/register/")
#     time.sleep(2)
#
