from selenium.common import ElementClickInterceptedException, ElementNotInteractableException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class CheckoutPage:

    billing_address_continue_button="div[id='billing-buttons-container'] input"
    ship_pickup_checkbox="PickUpInStore"
    ship_add_continue_button="(//p[@class='back-link']/following-sibling::input)[1]"
    ship_method_continue_button="//input[@onclick='ShippingMethod.save()']"
    payment_continue_button="(//p[@class='back-link']/following-sibling::input)[3]"
    info_continue_button="(//p[@class='back-link']/following-sibling::input)[4]"
    confirmation_continue_button="(//p[@class='back-link']/following-sibling::input)[5]"

    confirm_msg="div[class='title'] strong"
    order_continue_button="//input[@value='Continue']"

    def __init__(self, driver):
        self.driver = driver

    def click_on_bill_address_continue_button(self):
        self.driver.find_element(By.CSS_SELECTOR,self.billing_address_continue_button).click()



    def click_on_ship_address_continue_button(self):
        self.driver.find_element(By.XPATH,self.ship_add_continue_button).click()
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.ship_add_continue_button))
        )
        element.click()
    def click_on_ship_method_continue_button(self):
        self.driver.find_element(By.XPATH,self.ship_method_continue_button).click()

    def click_on_payment_continue_button(self):
        self.driver.find_element(By.XPATH,self.payment_continue_button).click()

    def click_on_info_continue_button(self):
        self.driver.find_element(By.XPATH,self.info_continue_button).click()

    def click_on_confirmation_continue_button(self):
        self.driver.find_element(By.XPATH,self.confirmation_continue_button).click()

    def get_on_confirm_msg(self):
        try:
            return self.driver.find_element(By.XPATH,self.confirm_msg).text
        except:
            return "none"

    def click_on_order_continue_button(self):
        self.driver.find_element(By.XPATH,self.order_continue_button).click()











