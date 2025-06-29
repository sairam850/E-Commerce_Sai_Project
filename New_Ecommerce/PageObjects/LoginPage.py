"""
Login page contain methods related to the login action
"""

from selenium.webdriver.common.by import By
from PageObjects.HomePage import BasePage
from Locators.TestLocators import SauceTestLocator


class LoginPage(BasePage):
    # Storing all the Locators
    USERNAME_INPUT = (By.ID, SauceTestLocator.username_locator)
    PASSWORD_INPUT = (By.ID, SauceTestLocator.password_locator)
    LOGIN_BUTTON = (By.ID, SauceTestLocator.login_button_locator)
    HAMBURGER_BUTTON = (By.XPATH, SauceTestLocator.hamburger_click)
    LOGOUT_CLICK = (By.ID, SauceTestLocator.logout_click)
    ERROR_MESSAGE = (By.XPATH,SauceTestLocator.error_message)

    def enter_username(self, username):
        self.enter_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def click_hamburger(self):
        self.is_clickable(self.HAMBURGER_BUTTON)
        self.click(self.HAMBURGER_BUTTON)

    def click_logout(self):
        self.is_clickable(self.LOGOUT_CLICK)
        self.click(self.LOGOUT_CLICK)

    def error_message(self):
        error_message = self.find_element(self.ERROR_MESSAGE)
        if error_message.is_enabled() and error_message.is_displayed():
            return True
        else:
            return False
