"""
This base_page contains common methods like find_element, find_elements, etc.,
"""

# import all necessary dependencies
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# import the exceptions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException, TimeoutException


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 15

    def find_element(self, locator):
        # exception handling
        try:
            web_element = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
            return web_element
        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR", error)

    def find_elements(self, locator):
        # exception handling
        try:
            web_elements = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_all_elements_located(locator))
            return web_elements
        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR", error)

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def fetch_url(self):
        try:
            return self.driver.current_url
        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR", error)

    def take_screenshot(self):
        try:
            return self.driver.save_screenshot("OrderPage.png")
        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR", error)

    def is_visible(self, locator):
        try:
            web_element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
            return web_element.is_displayed()
        except (TimeoutException, ElementNotVisibleException, NoSuchElementException) as error:
            print("ERROR: ", error)

    def is_clickable(self, locator):
        try:
            web_element = WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator))
            return web_element
        except (TimeoutException, ElementNotVisibleException, NoSuchElementException) as error:
            print("ERROR: ", error)

