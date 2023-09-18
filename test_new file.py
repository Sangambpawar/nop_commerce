import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_file():
    def test_login(self):
        driver=webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
        # driver.get('https://demo.nopcommerce.com/register?returnUrl=%2F')
        # time.sleep(5)
        # driver.find_element(By.XPATH,'//*[@id="FirstName"]').send_keys('sangam')
        # time.sleep(5)

        try:
            if driver.find_element(By.XPATH,'/html/body/div/div/div[1]/strong'):
                assert True
        except:
            assert False