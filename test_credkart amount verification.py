import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
# login
# def test_login():
#     driver.get('https://automation.credence.in/login')
#     # enter  username
#     driver.find_element(By.XPATH,'//*[@id="email"]').send_keys('test@credence.in')
#     # enter pass
#     driver.find_element(By.XPATH,'//*[@id="password"]').send_keys('test@123')
#     #click login
#     driver.find_element(By.XPATH,'/html/body/div/div/div/div/div[2]/form/div[4]/div/button').click()
#
#     try:
#         if driver.find_element(By.XPATH,'/html/body/div/div[1]/h2'):
#             print('Login Test is pass')
#             driver.find_element(By.XPATH, '//*[@id="navbar"]/ul[2]/li[3]/a').click()
#             driver.find_element(By.XPATH,'//*[@id="navbar"]/ul[2]/li[3]/ul/li/a').click()
#     except NoSuchElementException:
#         print('login test is failed')
#
#
#
# def test_addcart():
#     driver.get('https://automation.credence.in/login')
#     # enter  username
#     driver.find_element(By.XPATH, '//*[@id="email"]').send_keys('test@credence.in')
#     # enter pass
#     driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('test@123')
#     # click login
#     driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/form/div[4]/div/button').click()
#
#     #2) select product
#     driver.find_element(By.XPATH,'/html/body/div/div[2]/div[1]/div/div/a[2]/h3').click()
#     #  add car
#     driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/form[1]/input[5]').click()
#     # select quantity
#     a=Select(driver.find_element(By.XPATH,'/html/body/div/table/tbody/tr[1]/td[3]/select'))
#     a.select_by_visible_text('3')
#     # click on continue shoping
#     time.sleep(2)
#
#     driver.find_element(By.XPATH,'/html/body/div/a[1]').click()
#     time.sleep(5)
#     # # add another product
#     time.sleep(2)
#     driver.find_element(By.XPATH,'/html/body/div/div[2]/div[2]/div/div/a[2]/h3').click()
#     time.sleep(2)
#     driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/form[1]/input[5]').click()
#     b=Select(driver.find_element(By.XPATH,'/html/body/div/table/tbody/tr[2]/td[3]/select'))
#     b.select_by_index(3)
#     time.sleep(2)
#     # click  on proced  to checkout
#     driver.find_element(By.XPATH,'/html/body/div/a[2]').click()
#
#     # fill info
#     driver.find_element(By.XPATH, '//*[@id="first_name"]').send_keys('sangam')
#     driver.find_element(By.XPATH, '//*[@id="last_name"]').send_keys('pawar')
#     driver.find_element(By.XPATH, '//*[@id="phone"]').send_keys(9960541587)
#
#     driver.find_element(By.XPATH, '//*[@id="address"]').send_keys('near  samarth vidyalaya pokhari')
#     driver.find_element(By.XPATH, '//*[@id="zip"]').send_keys(414304)
#
#     a=Select(driver.find_element(By.XPATH, '//*[@id="state"]'))
#     a.select_by_index(1)
#
#     driver.find_element(By.XPATH, '//*[@id="owner"]').send_keys('sangam')
#     driver.find_element(By.XPATH, '//*[@id="cvv"]').send_keys(257)
#     driver.find_element(By.XPATH, '//*[@id="cardNumber"]').send_keys(4716)
#
#     driver.find_element(By.XPATH, '//*[@id="cardNumber"]').send_keys(1089)
#     driver.find_element(By.XPATH, '//*[@id="cardNumber"]').send_keys(9971)
#     driver.find_element(By.XPATH, '//*[@id="cardNumber"]').send_keys(6531)
#
#     b=Select(driver.find_element(By.XPATH, '/html/body/form/div/div[3]/div[2]/div/div[2]/div[4]/select[2]'))
#
#     b.select_by_index(3)
#
#     c=Select(driver.find_element(By.XPATH, '/html/body/form/div/div[3]/div[2]/div/div[2]/div[4]/select[1]'))
#
#     c.select_by_index(3)
#     driver.find_element(By.XPATH,'//*[@id="confirm-purchase"]').click()
#
#
#     try:
#         if driver.find_element(By.XPATH,'/html/body/div/div[1]/h1'):
#             print('check out test case is pass')
#             print(driver.find_element(By.XPATH,'/html/body/div/div[1]/p[2]').text)
#     except NoSuchElementException:
#         print('Checkout test case is failed')
#     #
    #
