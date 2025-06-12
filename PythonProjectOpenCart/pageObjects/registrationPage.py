from selenium.webdriver.common.by import By

from pageObjects.basePage import BasePage


class RegistrationPage(BasePage):

    gender_field=(By.ID, "gender-male")
    first_name_field=(By.ID,"FirstName")
    last_name_field=(By.ID, "LastName")
    email_field=(By.ID, "Email")
    password_field=(By.ID, "Password")
    confirmation_field=(By.ID, "ConfirmPassword")
    register_button_field=(By.ID, "register-button")
    result_field=(By.XPATH, "//div[contains(text(),'Your registration completed')]")

    register_continue_button=(By.XPATH, "//input[@class='button-1 register-continue-button']")

    def enter_gender_field(self):
        self.click(self.gender_field)

    def enter_first_name_field(self,f_name):
        self.send_keys(self.first_name_field,f_name)

    def enter_last_name_field(self,l_name):
        self.send_keys(self.last_name_field,l_name)

    def enter_email_field(self,email):
        self.send_keys(self.email_field,email)

    def enter_password_field(self,password):
        self.send_keys(self.password_field,password)

    def enter_confirmation_pwd_field(self,confirmation):
        self.send_keys(self.confirmation_field,confirmation)

    def enter_register_button_field(self):
        self.click(self.register_button_field)


    def get_conf_msg(self):
        return self.get_text(self.result_field)

    def click_on_register_continue_button(self):
        self.click(self.register_continue_button)


