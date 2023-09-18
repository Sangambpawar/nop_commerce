import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageobject.login_page_object import register_nop, login_nop
from utilities import XLutils


class Test_login():
    xl_path='F:\\nopcommerce_project\\Testdata\\login_test_data.xlsx'
    def test_login_01(self, setup):
        self.driver = setup
        self.rows=XLutils.RowCount(self.xl_path,'Sheet1')

        print(self.rows)
        for i in range(2,self.rows+1):
            self.exp = XLutils.ReadData(self.xl_path, 'Sheet1', i, 5)
        #
            self.user_name=XLutils.ReadData(self.xl_path,'Sheet1',i,1)
            time.sleep(3)
            self.password=XLutils.ReadData(self.xl_path,'Sheet1',i,2)
        #
            self.lp = login_nop(self.driver)
            self.lp.email_log_nop_method(self.user_name)
            self.lp.pass_log_method_nop(self.password)
            time.sleep(2)
            self.lp.click_log_nop()
            time.sleep(2)
            list1 = []

            if self.lp.login_status_method() == True:
                self.driver.save_screenshot(f'F:\\nopcommerce_project\\Screenshot\\loginpass{i}.png')
                if self.exp =='Pass':
                    list1.append('Pass')
                elif self.exp == 'Fail':
                    list1.append('Fail')

                XLutils.WriteData(self.xl_path,'Sheet1',i,4,'Pass')
                self.lp.click_logout_method_nop()
                time.sleep(1)
                self.lp.click_relogin_method()
                time.sleep(1)
            else:
                self.driver.save_screenshot(f'F:\\nopcommerce_project\\Screenshot\\loginfail{i}.png')
                if self.exp=='Pass':
                    list1.append('Fail')
                elif self.exp=='Fail':
                    list1.append('Pass')

                XLutils.WriteData(self.xl_path,'Sheet1',i,4,'Fail')
            self.lp.click_relogin_method()
            time.sleep(1)

            print(list1)
            if "Fail" not in list1:
                assert True
            else:
                assert False









