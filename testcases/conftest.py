import pytest
from selenium import webdriver


@pytest.fixture
def setup():
    driver=webdriver.Chrome()
    driver.maximize_window()
#register url
    # driver.get('https://demo.nopcommerce.com/register?returnUrl=%2F')
    # login url
    driver.get('https://demo.nopcommerce.com/login?returnUrl=%2F')

    driver.implicitly_wait(5)

    return driver

