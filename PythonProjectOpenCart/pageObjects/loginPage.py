from selenium.webdriver.common.by import By

from pageObjects.basePage import BasePage


class LoginPage(BasePage):

    userId=(By.ID, "Email")
    userPwd=(By.ID, "Password")
    loginButton=(By.XPATH, "//input[@value='Log in']")


    def setUserName(self,userName):
        self.send_keys(self.userId,userName)


    def setUserPwd(self,userPwd):
        self.send_keys(self.userPwd,userPwd)


    def setLoginButton(self,):
        self.click(self.loginButton)