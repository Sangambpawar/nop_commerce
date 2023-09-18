import time

from pageobject.login_page_object_nop import login_nop_ddt
from utilities.XLutils import RowCount, ReadData, WriteData


class Test_login_ddt_repet():
    def test_login_ddt_new(self,setup):
        self.driver=setup
        self.lp=login_nop_ddt(self.driver)
        self.xl_path='F:\\nopcommerce_project\\Testdata\\login_test_data.xlsx'
        self.rowcount=RowCount(self.xl_path,'Sheet1')


        list1=[]

        for i in range(2,self.rowcount+1):
            self.email = ReadData(self.xl_path, 'Sheet1', i, 1)
            self.password = ReadData(self.xl_path, 'Sheet1', i, 2)
            self.lp.email_for_login(self.email)
            self.lp.pass_for_login(self.password)
            self.lp.click_login_button()
            self.exp = ReadData(self.xl_path, 'Sheet1', i, 5)

            if self.lp.login_status()==True:
                self.write=WriteData(self.xl_path, 'Sheet1', i, 4,'Pass')
                if self.exp=='Pass':
                    list1.append('Pass')
                elif self.exp=='Fail':
                    list1.append('Fail')


                self.lp.click_logout()
                self.lp.click_login_again()
            else:
                self.write = WriteData(self.xl_path, 'Sheet1', i, 4, 'Fail')
                if self.exp=='Fail':
                    list1.append('Pass')
                elif self.exp=='Pass':
                    list1.append('Fail')
                self.lp.click_login_again()
        print(list1)
        if 'False' not in list1:
            assert True
        else:
            assert False

