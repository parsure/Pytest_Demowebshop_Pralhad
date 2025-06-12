from selenium.webdriver.common.by import By

from pageObjects.basePage import BasePage


class LandingPage(BasePage):

    registerLink=(By.LINK_TEXT, "Register")
    logInLink=(By.LINK_TEXT, "Log in")
    shoppingCartLink=(By.LINK_TEXT, "Shopping Cart")
    wishListLink=(By.LINK_TEXT, "Wish List")



    def click_on_register_link(self):
        self.click(self.registerLink)

    def click_on_log_in_link(self):
        self.click(self.logInLink)

    def click_on_wishlist_link(self):
        self.click(self.wishListLink)

    def click_on_shopping_cart_link(self):
        self.click(self.shoppingCartLink)

    '''def click_on_register_link(self):
        self.driver.find_element(By.LINK_TEXT, self.registerLink).click()


    def click_on_log_in_link(self):
        self.driver.find_element(By.LINK_TEXT, self.logInLink).click()

    def click_on_wishlist_link(self):
        self.driver.find_element(By.LINK_TEXT, self.wishListLink).click()

    def click_on_shopping_cart_link(self):
        self.driver.find_element(By.LINK_TEXT, self.shoppingCartLink).click()'''

