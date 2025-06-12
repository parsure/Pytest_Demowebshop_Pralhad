from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pageObjects.basePage import BasePage


class HomePage():

    featured_products=(By.XPATH, "//strong[text()='Featured products']")
    logout_button=(By.LINK_TEXT,"Log out")
    all_product_names=(By.XPATH, "//div[@class='details']//h2//a")
    cart=(By.XPATH, "(//a[@class='ico-cart'])[1]")
    cart_element=(By.XPATH, "//tr[@class='cart-item-row']//td[3]//a")
    search_field=(By.XPATH, "//input[@value='Search store']")
    all_autosuggest=(By.XPATH, "//ul[contains(@id,'ui-id-1')]//li//a")   #css--->  ul[id^=ui] li a
    product=(By.XPATH, "//div[@class='product-name']//h1")

    searched_product=(By.XPATH, "//input[contains(@id,'add-to-cart-button-75')]")
    processor_radio_button=(By.XPATH, "(//input[contains(@id,'product_attribute_')])[1]")

    def __init__(self, driver):
        self.driver=driver

    '''def verify_is_featured_products_present(self):
        return self.is_element_displayed(self.featured_products)

    def click_on_logout_button(self):
        self.click(self.logout_button)

    def all_products(self):
        try:
            return self.driver.find_elements(By.XPATH, self.all_product_names)
        except:
            return []

    def all_products(self):
        self.get_elements(self.all_auto_text)

    def click_on_cart(self):
        self.click(self.cart)

    def get_cart_ele_name(self):
        try:
            return self.get_text(self.cart_element)
        except:
            return "None"
    def send_on_search_field(self, name):
        self.send_keys(self.search_field, name)

    def get_all_auto(self):
        try:
            self.get_elements(self.all_auto)
        except:
            return []


    def get_product_name(self):
        self.get_text(self.product)

    def click_addToCart_searched_product(self):
        self.click(self.searched_product)

    def click_on_processor_radio_button(self):
        self.click(self.processor_radio_button)'''




    def verify_is_featured_products_present(self):
        try:
            return self.driver.find_element(*self.featured_products).is_displayed()
        except:
            return False

    def click_logout_button(self):
        self.driver.find_element(*self.logout_button).click()

    def all_products(self):
        try:
            return self.driver.find_elements(*self.all_product_names)
        except:
            return []


    def click_on_cart(self):
        self.driver.find_element(*self.cart).click()

    def get_cart_ele_name(self):
        try:
            return self.driver.find_element(*self.cart_element).text
        except:
            return "none"

    def send_on_search_field(self):
        self.driver.find_element(*self.search_field).send_keys("com")

    def get_all_autosuggestion(self):
        try:
            return self.driver.find_elements(*self.all_autosuggest)
        except:
            return []

    def get_product_name(self):
        try:
            return self.driver.find_element(*self.product).text
        except:
            return "none"

    def click_addToCart_searched_product(self):
        self.driver.find_element(*self.searched_product).click()

    def click_on_processor_radio_button(self):
        self.driver.find_element(*self.processor_radio_button).click()



