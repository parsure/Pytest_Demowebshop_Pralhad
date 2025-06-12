from selenium.webdriver.common.by import By

from pageObjects.basePage import BasePage


class CartPage(BasePage):

    product_checkbox=(By.CSS_SELECTOR, "tr[class='cart-item-row'] td:nth-child(1)")
    terms_checkbox=(By.ID, "termsofservice")
    checkout_button=(By.ID, "checkout")
    update_shopping_cart_button=(By.XPATH, "//input[@value='Update shopping cart']")

    def clck_on_product_checkbox(self):
        self.click(self.product_checkbox)

    def clck_on_terms_checkbox(self):
        self.click(self.terms_checkbox)

    def clck_on_checkout_button(self):
        self.click(self.checkout_button)

    def clck_on_update_shopping_cart_button(self):
        self.click(self.update_shopping_cart_button)


    '''def clck_on_product_checkbox(self):
        self.driver.find_element(By.CSS_SELECTOR,self.product_checkbox).click()

    def clck_on_terms_checkbox(self):
        self.driver.find_element(By.ID,self.terms_checkbox).click()

    def clck_on_checkout_button(self):
        self.driver.find_element(By.ID,self.checkout_button).click()'''
