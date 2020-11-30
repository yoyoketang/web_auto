import pytest
from selenium import webdriver


@pytest.fixture(scope="session", name="driver")
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    # quit是退出浏览器
    driver.quit()


@pytest.fixture(scope="session")
def base_url():
    url = "http://49.235.92.12:8200"
    return url