import time

from pageobject.login_page_object import orangehrm_login



class Test_login_fun:
    def test_title(self,setup):
        self.driver=setup
        time.sleep(2)
        if self.driver.title=='OrangeHRM':
            self.driver.save_screenshot('F:\\pythonProject1\\Screenshot\\titlepass.png')

            assert True
        else:
            self.driver.save_screenshot('F:\\pythonProject1\\Screenshot\\failtitle.png')
            assert False
        self.driver.close()


    def test_login(self,setup):
        self.driver=setup
        time.sleep(3)
        self.lp=orangehrm_login(self.driver)


        # self.lp.user_name('Admin')
        time.sleep(2)
        self.lp.password('123')
        time.sleep(2)
    #     self.lp.click_login()
    #
    #     if self.lp.login_status_method()==True:
    #         self.lp.click_menu()
    #         self.lp.click_logout()
    #
    #
    #         assert True
    #     else:
    #         assert False
    #
    #
    #
    #
