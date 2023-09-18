import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_multwindow():

    def test_mul(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get('https://www.hyrtutorials.com/p/window-handles-practice.html')
        WebDriverWait(driver,10).until(expected_conditions._element_if_visible(d))
        driver.find_element(By.XPATH,'//*[@id="newTabBtn"]').click()
        driver.switch_to.window(driver.window_handles[1])
        print(driver.find_element(By.XPATH,'//*[@id="Blog1"]/div[1]/div/div[1]/div[1]/div/h1').text)
        driver.find_element(By.XPATH,'//*[@id="promptBox"]').click()
        time.sleep(2)



        time.sleep(2)
        print(Alert(driver).text)
        Alert(driver.remove_all_credentials)

        Alert(driver).send_keys('hii')

        Alert(driver).accept()

        time.sleep(3)






