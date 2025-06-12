from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):



    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def click(self, locator):
        """Wait until the element is clickable, then click."""
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def send_keys(self, locator, text):
        """Wait until the element is visible, then clear and send keys."""
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def get_text(self, by_locator):
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(by_locator)
        )
        return element.text

    def is_element_displayed(self, by_locator, timeout=5):

        try:
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locator))
            return element.is_displayed()
        except TimeoutException:
            return False

    def get_elements(self, by_locator, timeout=10):
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(by_locator)
            )
            return elements
        except TimeoutException:
            return []