import pytest

from pageObjects.homePage import HomePage
from pageObjects.landingPage import LandingPage
from pageObjects.loginPage import LoginPage
from utilities.XLUtils import XLUtils
from utilities.customLogger import LogGenerator
from utilities.readProperties import ReadProperties
import os

class TestLogin_DDT:


    baseURL=ReadProperties.get_base_url()
    logger=LogGenerator.get_logger("Login_DataDriven")
    excel_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), "tesData", "demowebData.xlsx")
    '''email = ReadProperties.get_user_name()
    password = ReadProperties.get_user_password()'''
    logger.info("** Login DDT testing started **")

    def test_001_login_ddt(self,set_up):
        self.logger.info("** getting total rows **")
        total_row=XLUtils.getRowCount(self.excel_path,"Sheet1")
        print("***Total Rows***",total_row)
        self.logger.info("** getting total columns **")
        total_column=XLUtils.getColumnCount(self.excel_path,"Sheet1")
        print("***Total Columns***",total_column)

        list_result=[]
        self.driver=set_up
        self.driver.get(self.baseURL)
        self.logger.info("** creating all page objects **")
        self.landing_page_object = LandingPage(self.driver)
        self.login_page_object = LoginPage(self.driver)
        self.home_page_object=HomePage(self.driver)
        self.logger.info("** ddt for loop **")
        for d in range(2,total_row+1):
            self.landing_page_object.click_on_log_in_link()
            self.email=XLUtils.readData(file=self.excel_path,sheetName="Sheet1",rowNo=d, columnNo=1)
            self.pwd=XLUtils.readData(file=self.excel_path, sheetName="Sheet1", rowNo=d, columnNo=2)
            self.exp=XLUtils.readData(file=self.excel_path,sheetName="Sheet1",rowNo=d, columnNo=3)
            self.login_page_object.setUserName(self.email)
            self.login_page_object.setUserPwd(self.pwd)
            self.login_page_object.setLoginButton()
            self.logger.info("** getting result **")
            result=self.home_page_object.verify_is_featured_products_present()
            self.logger.info("** Verifying result **")
            if self.exp=="valid":
                if result==True:
                    self.logger.info("** result matched **")
                    list_result.append("pass")
                    self.home_page_object.click_logout_button()
                else:
                    self.logger.info("** result not matched **")
                    list_result.append("fail")
                    self.driver.save_screenshot(os.path.join(os.path.dirname(os.path.dirname(__file__)), "screenshots", "DDT.png"))
                    assert False
            elif self.exp=="invalid":
                if result==False:
                    self.logger.info("** result matched **")
                    list_result.append("pass")
                    self.landing_page_object.click_on_log_in_link()
                else:
                    self.logger.info("** result not matched **")
                    list_result.append("fail")
                    self.driver.save_screenshot(os.path.join(os.path.dirname(os.path.dirname(__file__)), "screenshots", "DDT.png"))

            print("my list",list_result)
            if "fail" in list_result:
                assert False

            else:
                assert True










