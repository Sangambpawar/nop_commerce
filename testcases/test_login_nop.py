import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageobject.login_page_object import register_nop, login_nop
class Test_login():
    def test_login_01(self, setup):
        self.driver = setup
        self.lp = login_nop(self.driver)
        self.lp.email_log_nop_method('sangam1@gmail.com')
        self.lp.pass_log_method_nop('1234566')
        self.lp.click_log_nop()
        time.sleep(2)
        if self.lp.login_status_method() == True:
            self.driver.save_screenshot("F:\\nopcommerce_project\\Screenshot\\test_login_pass.png")
            # self.lp.click_logout_method_nop()
            # time.sleep(2)
            # self.lp.click_log_nop()
            # time.sleep(2)
            assert True



        else:
            self.driver.save_screenshot("F:\\nopcommerce_project\\Screenshot\\test_login_fail.png")
            assert False

        #

