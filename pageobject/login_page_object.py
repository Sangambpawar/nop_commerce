import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()


class register_nop():
    gender_male_xpath=By.XPATH,'//*[@id="gender-male"]'
    gender_female_xpath=By.XPATH,'//*[@id="gender-female"]'
    first_name_xpath=(By.XPATH,'/html/body/div[6]/div[3]/div/div/div/div[2]/form/div[1]/div[2]/div[2]/input')
    last_name_xpath=(By.XPATH,'//*[@id="LastName"]')
    drop_dob_day_xpath=By.XPATH,'/html/body/div[6]/div[3]/div/div/div/div[2]/form/div[1]/div[2]/div[4]/div/select[1]'
    drop_dob_mon_xpath=By.XPATH,'/html/body/div[6]/div[3]/div/div/div/div[2]/form/div[1]/div[2]/div[4]/div/select[2]'
    email_regi_xpath=By.XPATH,'//*[@id="Email"]'
    drop_dob_year_xpath=By.XPATH,'/html/body/div[6]/div[3]/div/div/div/div[2]/form/div[1]/div[2]/div[4]/div/select[3]'
    company_name_xpath=By.XPATH,'//*[@id="Company"]'
    newsletter_check_xpath=By.XPATH,'//*[@id="Newsletter"]'
    password_xpath_regi=By.XPATH,'//*[@id="Password"]'
    password_confirm_xpath_regi=By.XPATH,'//*[@id="ConfirmPassword"]'
    click_regi_button_xpath=By.XPATH,'//*[@id="register-button"]'
    regi_ststus_xpath=By.XPATH,'/html/body/div[6]/div[3]/div/div/div/div[2]/div[1]'
    email_login_xpath=By.XPATH,'//*[@id="Email"]'
    click_logout_xpath=By.XPATH,'/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a'
    click_relogin_xpath=By.XPATH,'/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a'

    def __init__(self,driver):
        self.driver=driver
        self.wait = WebDriverWait(self.driver, 10)


    def gender_male_method(self):
        self.driver.find_element(*register_nop.gender_male_xpath).click()
    def gender_female_method(self):
        self.driver.find_element(*register_nop.gender_female_xpath).click()
    def first_name_regi_method(self,firstname):
        self.driver.find_element(*register_nop.first_name_xpath).send_keys(firstname)
    def last_name_regi_method(self,lastname):
        self.driver.find_element(*register_nop.last_name_xpath).send_keys(lastname)
    def drop_day_method(self,ind):
        a=Select(self.driver.find_element(*register_nop.drop_dob_day_xpath))
        a.select_by_index(ind)
    def drop_mon_method(self,ind):
        a=Select(self.driver.find_element(*register_nop.drop_dob_mon_xpath))
        a.select_by_index(ind)
    def drop_year_method(self,ind):

        a=Select(self.driver.find_element(*register_nop.drop_dob_year_xpath))
        a.select_by_visible_text(ind)
    def email_regi_method(self,email):
        self.driver.find_element(*register_nop.email_regi_xpath).send_keys(email)
    def company_name_method(self,company):
        self.driver.find_element(*register_nop.company_name_xpath).send_keys(company)
    def newsletter_method(self):
        self.driver.find_element(*register_nop.newsletter_check_xpath).click()
    def password_regi_method(self,password):
        self.driver.find_element(*register_nop.password_xpath_regi).send_keys(password)
    def con_pass_regi_method(self,password):
        self.driver.find_element(*register_nop.password_confirm_xpath_regi).send_keys(password)
    def click_regi_button_method(self):
        self.driver.find_element(*register_nop.click_regi_button_xpath).click()
    def regi_status_method(self):
        try:
            self.driver.find_element(*register_nop.regi_ststus_xpath)
            return True
        except:
            return False

class login_nop(register_nop):
    pass_login_xpath = By.XPATH, '//*[@id="Password"]'
    click_login_butt_xpath = By.XPATH, '/html/body/div[6]/div[3]/div/div/div/div[2]/div[1]/div[2]/form/div[3]/button'

    def email_log_nop_method(self,email):
        self.driver.find_element(*login_nop.email_login_xpath).send_keys(email)
    def pass_log_method_nop(self,password):
        self.driver.find_element(*login_nop.pass_login_xpath).send_keys(password)
    def click_log_nop(self):
        self.driver.find_element(*login_nop.click_login_butt_xpath).click()
    def click_logout_method_nop(self):
        self.driver.find_element(*login_nop.click_logout_xpath).click()
    def click_relogin_method(self):
        self.driver.find_element(*login_nop.click_relogin_xpath).click()
    def login_status_method(self):
        try:
             self.driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/div/div/div/div[2]/div[1]/h2')
             return True


        except NoSuchElementException:
            return False














