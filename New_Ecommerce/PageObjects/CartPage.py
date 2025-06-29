"""
This file contains the product page related methods like get_product name,prices,add items to cart,sorting name and prices and reset app etc.,
"""

from selenium.webdriver.common.by import By
from PageObjects.HomePage import BasePage
from Locators.TestLocators import SauceTestLocator
from selenium.webdriver.support.ui import Select
import random

class CartPage(BasePage):
    CART = (By.XPATH, SauceTestLocator.cart_button)
    NAME_FETCH = (By.XPATH,SauceTestLocator.inventory_name)
    PRICE_FETCH = (By.XPATH,SauceTestLocator.inventory_price)
    ITEM = (By.XPATH,SauceTestLocator.invenory_item)
    P_CHECK = (By.XPATH,SauceTestLocator.product_check)
    P1_ADD = (By.ID,SauceTestLocator.product1)
    P2_ADD = (By.ID, SauceTestLocator.product2)
    P3_ADD = (By.ID, SauceTestLocator.product3)
    P4_ADD = (By.ID,SauceTestLocator.product4)
    COUNT_ITEMS = (By.CLASS_NAME,SauceTestLocator.count_items)
    PRODUCT_DETAILS1 = (By.XPATH,SauceTestLocator.product1_details)
    PRODUCT_DETAILS2 = (By.XPATH, SauceTestLocator.product2_details)
    PRODUCT_DETAILS3 = (By.XPATH,SauceTestLocator.product3_details)
    PRODUCT_DETAILS4 = (By.XPATH,SauceTestLocator.product4_details)
    HAMBURGER_BUTTON = (By.XPATH,SauceTestLocator.hamburger_click)
    RESET_APP = (By.XPATH,SauceTestLocator.reset_app_function)
    SORT = (By.CLASS_NAME,SauceTestLocator.sorting)
    NAME = (By.XPATH,SauceTestLocator.sort_name)
    PRICE = (By.XPATH, SauceTestLocator.sort_price)
    P1_PRICE = (By.XPATH,SauceTestLocator.p1_price)


    def check_cart(self):
        CART_BUTTON = self.find_element(self.CART)
        if CART_BUTTON.is_displayed():
            return True
        else:
            return False
    def click_cart(self):
        self.click(self.CART)

    def check_cart_name_price(self):
        items = self.find_elements(self.ITEM)
        product_info = []
        for item in items:
            product_name = self.find_elements(self.NAME_FETCH)
            product_price = self.find_elements(self.PRICE_FETCH)
            product_info.append((product_name,product_price))
            print(item)

        random_products = random.sample(product_info,4)
        selected_products = random_products
        print("Randomly selected products and prices:")
        for name, price in selected_products:
            print(f"{name} - {price}")
        return len(random_products)

    def add_cart(self):
        self.click(self.P1_ADD)
        self.click(self.P2_ADD)
        self.click(self.P3_ADD)
        self.click(self.P4_ADD)

    def count_items(self):
        count_item = self.find_element(self.COUNT_ITEMS).text.strip()
        return int(count_item) if count_item.isdigit() else 0

    def cart_description(self):
        inventory_item1 = self.find_element(self.PRODUCT_DETAILS1)
        inventory_item2 = self.find_element(self.PRODUCT_DETAILS2)
        inventory_item3 = self.find_element(self.PRODUCT_DETAILS3)
        inventory_item4 = self.find_element(self.PRODUCT_DETAILS4)
        if inventory_item1.is_displayed() and inventory_item2.is_displayed() and inventory_item3.is_displayed() and inventory_item4.is_displayed():
            return True
        else:
            return False

    def reset_page(self):
        self.is_clickable(self.RESET_APP)
        self.click(self.RESET_APP)

    def sort_name_asc(self):
        name_asc = self.is_clickable(self.SORT)
        select = Select(name_asc)
        select.select_by_value("az")

    def sort_price_desc(self):
        price_desc = self.is_clickable(self.SORT)
        select = Select(price_desc)
        select.select_by_value("hilo")

    def fetch_product_price(self):
        price_elements = self.find_elements(self.PRICE_FETCH)
        prices = []
        for element in price_elements:
            price = element.text.strip()
            number = float(price.replace('$', ''))
            prices.append(number)
        return prices

    def fetch_names(self):
        name_elements = self.find_elements(self.NAME_FETCH)
        names = []
        names.append(name_elements)
        return names

    def check_problem_user(self):
        if self.is_visible(self.P3_ADD):
            return False
        else:
            return True

    def check_visual_user(self):
        price_element1 = self.find_element(self.P1_PRICE)
        price = price_element1.text.strip()
        number = float(price.replace('$', ''))
        return number





