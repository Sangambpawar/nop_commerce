import time

from selenium.common import NoSuchElementException

from pageobject.login_page_object import register_nop, login_nop


class Test_regi_nop_commerce:
    def test_regi_nop(self,setup):
        self.driver=setup
        self.driver.get('https://demo.nopcommerce.com/register?returnUrl=%2F')
        time.sleep(2)
        self.lp=register_nop(self.driver)
        time.sleep(2)
        self.lp.gender_male_method()
        time.sleep(2)
        self.lp.first_name_regi_method('sangam')

        self.lp.last_name_regi_method('pawar')
        time.sleep(2)
        self.lp.drop_day_method('28')
        self.lp.drop_mon_method('1')
        self.lp.drop_year_method('1997')
        self.lp.email_regi_method('sangam@gmail.com')
        self.lp.company_name_method('dazzling')
        self.lp.password_regi_method('123456')
        self.lp.con_pass_regi_method('123456')
        time.sleep(3)
        self.lp.click_regi_button_method()
        time.sleep(3)

        if self.lp.regi_status_method()==True:

            self.driver.save_screenshot("F:\\pythonProject1\\Screenshot\\test_regi_pass.png")
            assert True
        else:
            self.driver.save_screenshot("F:\\pythonProject1\\Screenshot\\test_login_fail.png")
            assert False

    # def test_login_01(self, setup):
    #     self.driver = setup
    #     self.lp = login_nop(self.driver)
    #     self.lp.email_log_nop_method('sangam@gmail.com')
    #     self.lp.pass_log_method_nop('123456')
    #     if self.lp.login_status_method() == True:
    #
    #         self.driver.save_screenshot("F:\\pythonProject1\\Screenshot\\test_login_pass.png")
    #         assert False
    #     else:
    #         self.driver.save_screenshot("F:\\pythonProject1\\Screenshot\\test_login_failed.png")
    #         assert True




