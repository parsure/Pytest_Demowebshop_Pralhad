import pytest

from pageObjects.landingPage import LandingPage
from pageObjects.registrationPage import RegistrationPage
from utilities.customLogger import LogGenerator
from utilities.randonString import generate_random_email
import os

from utilities.readProperties import ReadProperties


class TestRegistration:

    #base="https://demowebshop.tricentis.com/"
    base=ReadProperties.get_base_url()

    logger=LogGenerator.get_logger("Account registration")

    @pytest.mark.sanity
    def test_001_registration(self,set_up):
        self.logger.info("**---TC001 Account Registration started----**")
        self.driver=set_up

        self.logger.info("**---Launching Application----**")
        self.driver.get(self.base)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        landing_page_object=LandingPage(self.driver)
        self.logger.info("**---clicking on Register link----**")
        landing_page_object.click_on_register_link()

        reg_page_object=RegistrationPage(self.driver)
        reg_page_object.enter_gender_field()
        self.logger.info("**---Entering basic details----**")
        reg_page_object.enter_first_name_field("Pralhad")
        reg_page_object.enter_last_name_field("Parsure")
        random_email=generate_random_email()
        print(random_email)
        reg_page_object.enter_email_field(random_email)
        reg_page_object.enter_password_field("12345abcde")
        reg_page_object.enter_confirmation_pwd_field("12345abcde")
        self.logger.info("**---clicking on Registration button----**")
        reg_page_object.enter_register_button_field()
        success_msg=reg_page_object.get_conf_msg()
        print("result msg:", success_msg)
        if "Your registration completed" in success_msg:
            assert True
            self.logger.info("**---result msg is matched----**")
        else:
            self.driver.save_screenshot(os.path.join(os.path.dirname(os.path.dirname(__file__)), "screenshots", "Registration.png"))
            self.logger.info("**---result msg is not matched----**")
            assert False
        self.logger.info("**---TC001 Account Registration finished----**")
