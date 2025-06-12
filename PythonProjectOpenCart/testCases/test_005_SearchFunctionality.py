import time

import pytest

from pageObjects.cartPage import CartPage
from pageObjects.homePage import HomePage
import os

from utilities.customLogger import LogGenerator


class Test_SearchFunctionality:
    logger=LogGenerator.get_logger("searched_product")
    @pytest.mark.search
    def test_search_item(self,login_to_app):
        driver = login_to_app

        home_page_object=HomePage(driver)
        home_page_object.send_on_search_field()
        #  xpath--->  //ul[contains(@id,'ui-id-1')]//li//a     css--->  ul[id^=ui] li a
        time.sleep(3)

        all_auto=home_page_object.get_all_autosuggestion()
        for item in all_auto:
            product_name=item.text
            print(product_name)
            if  product_name.lower()=="simple computer":
                item.click()
                break

        act_product_name=home_page_object.get_product_name()
        print(act_product_name)

        if act_product_name.strip()=="Simple Computer":

            assert True
        else:
            driver.save_screenshot(os.path.join(os.path.dirname(os.path.dirname(__file__)), "screenshots", "search_functionality.png"))
            assert False
        time.sleep(3)
        home_page_object.click_on_processor_radio_button()
        time.sleep(3)
        home_page_object.click_addToCart_searched_product()
        self.logger.info("** clicked on the cart **")
        time.sleep(3)
        home_page_object.click_on_cart()
        time.sleep(3)
        self.logger.info("** Verifying the cart product name **")
        act_text = home_page_object.get_cart_ele_name()
        print("actual", act_text)
        assert act_text == "Simple Computer"

        cart_page_object=CartPage(driver)
        cart_page_object.clck_on_product_checkbox()
        cart_page_object.clck_on_update_shopping_cart_button()









