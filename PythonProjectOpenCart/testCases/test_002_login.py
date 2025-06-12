import datetime

from pageObjects.homePage import HomePage
from pageObjects.landingPage import LandingPage
from pageObjects.loginPage import LoginPage
from utilities.customLogger import LogGenerator
from utilities.readProperties import ReadProperties
import os

class Test_002Login:

    #__test__ = False

    baseUrl=ReadProperties.get_base_url()

    logger=LogGenerator.get_logger("Login")

    userId=ReadProperties.get_user_name()
    password=ReadProperties.get_user_password()
    logger.info("***---Login is started---***")
    def test_001_login(self,set_up):
        self.driver=set_up
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.logger.info("***---Launching browser window---***")
        self.driver.get(self.baseUrl)
        self.logger.info("***---Launching Landing Page---***")
        landing_page_object=LandingPage(self.driver)
        landing_page_object.click_on_log_in_link()
        self.logger.info("***---Launching Login Page---***")
        login_page_object=LoginPage(self.driver)
        login_page_object.setUserName(self.userId)
        login_page_object.setUserPwd(self.password)
        login_page_object.setLoginButton()
        self.logger.info("***---Launching Home Page---***")
        home_page_object=HomePage(self.driver)
        result=home_page_object.verify_is_featured_products_present()
        print(result)
        if result == True:
            assert True
        else:
            self.driver.save_screenshot(os.path.join(os.path.dirname(os.path.dirname(__file__)), "screenshots", "Login1.png"))
            assert False
        self.logger.info("***---LLogin function is completed---***")