import time

import pytest
from selenium.webdriver.common.by import By

from pageObjects.cartPage import CartPage
from pageObjects.checkoutPage import CheckoutPage
from pageObjects.homePage import HomePage
from pageObjects.landingPage import LandingPage

from utilities.customLogger import LogGenerator
import os

# //h2[@class='product-title']//a/parent::h2/parent::div/child::div[3]
class Test_AddToCart_Checkout():

    logger=LogGenerator.get_logger()
    logger.info("** Started add to cart and checkout product feature**")
    @pytest.mark.dependency(name="add_to_cart")
    @pytest.mark.addToCart
    def test_001_add_to_cart_form(self,login_to_app):
        self.logger.info("** login to application**")
        driver=login_to_app
        self.logger.info("** fetching all product names in homepage **")
        home_page_object=HomePage(driver)
        all_products=home_page_object.all_products()
        time.sleep(3)
        for item in all_products:
            product_name=item.text
            print(product_name)

            if product_name=="14.1-inch Laptop":
                self.logger.info("** selected required product name** **")

                item.click()
                time.sleep(3)
                driver.find_element(By.ID, "add-to-cart-button-31").click()
                time.sleep(3)
                #item.find_element(By.XPATH, "parent::h2/parent::div/child::div[3]").click()
                break

        self.logger.info("** Adding product to the cart **")
        home_page_object.click_on_cart()

        self.logger.info("** Verifying the cart product name **")
        act_text=home_page_object.get_cart_ele_name()
        print("actual", act_text)

        assert act_text == "14.1-inch Laptop"

        self.logger.info("** selecting terms checkbox and clicking on checkout button **")
        cart_page_object=CartPage(driver)
        cart_page_object.clck_on_product_checkbox()
        cart_page_object.clck_on_terms_checkbox()
        cart_page_object.clck_on_checkout_button()

        self.logger.info("** performing action checkout page**")

        checkout_page_object=CheckoutPage(driver)
        checkout_page_object.click_on_bill_address_continue_button()

        self.logger.info("Waiting for shipping address continue button to be clickable")
        checkout_page_object.click_on_ship_address_continue_button()

        checkout_page_object.click_on_ship_method_continue_button()

        checkout_page_object.click_on_payment_continue_button()

        checkout_page_object.click_on_info_continue_button()

        checkout_page_object.click_on_confirmation_continue_button()
        time.sleep(3)

        checkout_page_object.click_on_order_continue_button()








