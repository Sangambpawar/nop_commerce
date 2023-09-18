from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class login_nop_ddt():
    email_xpath_login=By.XPATH,'//*[@id="Email"]'
    pass_xpath_login=By.XPATH,'//*[@id="Password"]'
    click_login_xpath=By.XPATH,'/html/body/div[6]/div[3]/div/div/div/div[2]/div[1]/div[2]/form/div[3]/button'
    login_status_xpath=By.XPATH,'/html/body/div[6]/div[3]/div/div/div/div/div[2]/div[1]/h2'
    click_logout_xpath=By.XPATH,'/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a'
    click_again_login_xpath=By.XPATH,'/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a'
    def __init__(self,driver):
        self.driver=driver
    def email_for_login(self,email):
        self.driver.find_element(*login_nop_ddt.email_xpath_login).send_keys(email)

    def pass_for_login(self, password):
        self.driver.find_element(*login_nop_ddt.pass_xpath_login).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*login_nop_ddt.click_login_xpath).click()
    def click_logout(self):
        self.driver.find_element(*login_nop_ddt.click_logout_xpath).click()

    def click_login_again(self):
        self.driver.find_element(*login_nop_ddt.click_again_login_xpath).click()


    def login_status(self):
        try :
            if self.driver.find_element(*login_nop_ddt.login_status_xpath):
                return True
        except NoSuchElementException:
            return False













