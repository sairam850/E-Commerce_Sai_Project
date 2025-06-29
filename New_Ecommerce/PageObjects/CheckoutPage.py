"""
This file contains the product page related methods like Checkout the Order etc.,
"""

from selenium.webdriver.common.by import By
from PageObjects.HomePage import BasePage
from Locators.TestLocators import SauceTestLocator

class CheckoutPage(BasePage):
    checkout1 = (By.ID, SauceTestLocator.checkout)
    f_name = (By.ID,SauceTestLocator.first_name)
    l_name = (By.ID,SauceTestLocator.last_name)
    p_code = (By.ID,SauceTestLocator.postalcode)
    cont = (By.ID,SauceTestLocator.continue_button)
    finish = (By.ID,SauceTestLocator.finish_button)
    back = (By.ID,SauceTestLocator.back_product)
    def checkout(self):
        self.click(self.checkout1)

    def enter_fname(self,first_name):
        self.enter_text(self.f_name,first_name)

    def enter_lname(self,last_name):
        self.enter_text(self.l_name,last_name)

    def enter_pincode(self,pincode):
        self.enter_text(self.p_code,pincode)

    def click_cont(self):
        self.click(self.cont)

    def click_finish(self):
        self.click(self.finish)

    def back_product(self):
        back_product = self.find_element(self.back)
        if back_product.is_enabled():
            return True
        else:
            return False



