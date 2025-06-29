from PageObjects.LoginPage import LoginPage
from PageObjects.HomePage import BasePage
from PageObjects.CartPage import CartPage
from PageObjects.CheckoutPage import CheckoutPage
from time import sleep
import pytest
from Configuration.conftest import driver
from Data.TestData import SauceStoreData

@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
# Test case for Valid Username and valid Password
def test_valid_login(driver):
    driver.get(SauceStoreData.url)
    base_page = BasePage(driver)
    login_page = LoginPage(driver)
    login_page.enter_username(SauceStoreData.username)
    login_page.enter_password(SauceStoreData.password)
    login_page.click_login()

    # asserting expected vs actual url
    assert SauceStoreData.expected_url == base_page.fetch_url()
    print("Success: Test Case Passed for Valid Login")

@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
# Test case for Locked User
def test_locked_login(driver):
    driver.get(SauceStoreData.url)
    login_page = LoginPage(driver)
    login_page.enter_username(SauceStoreData.username_locked)
    login_page.enter_password(SauceStoreData.password)
    login_page.click_login()

    # Asserting the Proper Error Message Displayed
    assert login_page.error_message() == True
    print("Success: Test Case Passed for Locked User")

@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
# Test case for Glitch User
def test_glitch_login(driver):
    driver.get(SauceStoreData.url)
    login_page = LoginPage(driver)
    base_page = BasePage(driver)
    login_page.enter_username(SauceStoreData.user_glitch)
    login_page.enter_password(SauceStoreData.password)
    login_page.click_login()

    # asserting expected vs actual url
    assert SauceStoreData.expected_url == base_page.fetch_url()
    print("Success: Test Case Passed for Glitch User")

@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
# Test case for Problem User
def test_problem_user(driver):
    driver.get(SauceStoreData.url)
    login_page = LoginPage(driver)
    cart_page = CartPage(driver)
    login_page.enter_username(SauceStoreData.user_problem)
    login_page.enter_password(SauceStoreData.password)
    login_page.click_login()

    # Asserting the Product add-to-cart-sauce-labs-onesie is unclickable
    assert cart_page.check_problem_user() == False
    print("Success: Test Case Passed for Problem User")

@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
# Test case for Error User
def test_error_user(driver):
    driver.get(SauceStoreData.url)
    login_page = LoginPage(driver)
    cart_page = CartPage(driver)
    login_page.enter_username(SauceStoreData.user_error)
    login_page.enter_password(SauceStoreData.password)
    login_page.click_login()

    # Asserting the Product add-to-cart-sauce-labs-onesie is unclickable
    assert cart_page.check_problem_user() == False
    print("Success: Test Case Passed for Error User")

@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
# Test case for Visual User
def test_visual_user(driver):
    driver.get(SauceStoreData.url)
    login_page = LoginPage(driver)
    cart_page = CartPage(driver)
    login_page.enter_username(SauceStoreData.user_visual)
    login_page.enter_password(SauceStoreData.password)
    login_page.click_login()
    new_visual_user = cart_page.check_visual_user()

    # Asserting the Product Price is not Expected Price
    assert new_visual_user != 29.99
    print("Success: Test Case Passed for Visual User")

@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
# Test case for Valid User and Invalid Password
def test_invalid_password_login(driver):
    driver.get(SauceStoreData.url)
    login_page = LoginPage(driver)
    login_page.enter_username(SauceStoreData.username)
    login_page.enter_password(SauceStoreData.password_invalid)
    login_page.click_login()

    # Asserting the Proper Error Message Displayed
    assert login_page.error_message() == True
    print("Success:Test Case Passed for Valid User and Invalid Password")

@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
# Test Case for Invalid Email and Valid Password
def test_invalid_email_login(driver):
    driver.get(SauceStoreData.url)
    login_page = LoginPage(driver)
    login_page.enter_username(SauceStoreData.username_invalid)
    login_page.enter_password(SauceStoreData.password)
    login_page.click_login()

    # Asserting the Proper Error Message Displayed
    assert login_page.error_message() == True
    print("Success:Test Case Passed for Invalid Email and Valid Password")

@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
# Test Case for Empty Username and Valid Password
def test_empty_username(driver):
    driver.get(SauceStoreData.url)
    login_page = LoginPage(driver)
    login_page.enter_username(SauceStoreData.empty_username)
    login_page.enter_password(SauceStoreData.password)
    login_page.click_login()

    # Asserting the Proper Error Message Displayed
    assert login_page.error_message() == True
    print("Success:Test Case Passed for Empty Username and Valid Password")

@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
# Test Case for Valid Username and Empty Password
def test_empty_password(driver):
    driver.get(SauceStoreData.url)
    login_page = LoginPage(driver)
    login_page.enter_username(SauceStoreData.username)
    login_page.enter_password(SauceStoreData.empty_password)
    login_page.click_login()

    # Asserting the Proper Error Message Displayed
    assert login_page.error_message() == True
    print("Success:Test Case Passed for Valid Username and Empty Password")

@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
# Test Case for Empty Username and Empty Password
def test_empty_username_password(driver):
    driver.get(SauceStoreData.url)
    login_page = LoginPage(driver)
    login_page.enter_username(SauceStoreData.empty_username)
    login_page.enter_password(SauceStoreData.empty_password)
    login_page.click_login()

    # Asserting the Proper Error Message Displayed
    assert login_page.error_message() == True
    print("Success:Test Case Passed for  Empty Username and Empty Password")

@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
# Test Case for Invalid Username and Invalid Password
def test_invalid_email_invalid_password(driver):
    driver.get(SauceStoreData.url)
    login_page = LoginPage(driver)
    login_page.enter_username(SauceStoreData.username_invalid)
    login_page.enter_password(SauceStoreData.password_invalid)
    login_page.click_login()

    # Asserting the Proper Error Message Displayed
    assert login_page.error_message() == True
    print("Success:Test Case Passed for InValid Username and InValidPassword")

@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
# Test Case for Logout
def test_logout(driver):
    driver.get(SauceStoreData.url)
    login_page = LoginPage(driver)
    login_page.enter_username(SauceStoreData.username)
    login_page.enter_password(SauceStoreData.password)
    login_page.click_login()
    sleep(5)
    login_page.click_hamburger()
    login_page.click_logout()
    sleep(5)

    # asserting expected vs actual url
    assert SauceStoreData.url == "https://www.saucedemo.com/"
    print("Success: Test Case Passed for Logout Functionality")

@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
# Test Case for Check Cart Button is Displayed
def test_cart_button(driver):
    driver.get(SauceStoreData.url)
    login_page = LoginPage(driver)
    cart_page = CartPage(driver)
    login_page.enter_username(SauceStoreData.username)
    login_page.enter_password(SauceStoreData.password)
    login_page.click_login()
    sleep(3)

    # Assertinf Cart Button is Displayed
    assert cart_page.check_cart() == True
    print("Success: Test Case Passed for Testing Cart Button")

@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
# Test Case for Checking the Count for Name and Prices for Random Prices
def test_product_name_price_extract(driver):
    driver.get(SauceStoreData.url)
    login_page = LoginPage(driver)
    cart_page = CartPage(driver)
    login_page.enter_username(SauceStoreData.username)
    login_page.enter_password(SauceStoreData.password)
    login_page.click_login()
    sleep(3)
    count_cart = cart_page.check_cart_name_price()

    # Asserting Random Name_Price to be 4
    assert count_cart == 4
    print("Success: Test Case Passed for Product Name_Price_Extract")

@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
# Test Case for Check the Count for Selected Product
def test_selected_product_count(driver):
    driver.get(SauceStoreData.url)
    login_page = LoginPage(driver)
    cart_page = CartPage(driver)
    login_page.enter_username(SauceStoreData.username)
    login_page.enter_password(SauceStoreData.password)
    login_page.click_login()
    sleep(5)
    cart_page.add_cart()
    new_count_items = cart_page.count_items()

    # Asserting Selected Product Count to be 4
    assert new_count_items == 4
    print("Success: Test Case Passed for Product Count")

@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
# Test Case for  Product Description
def test_product_description(driver):
    driver.get(SauceStoreData.url)
    login_page = LoginPage(driver)
    cart_page = CartPage(driver)
    login_page.enter_username(SauceStoreData.username)
    login_page.enter_password(SauceStoreData.password)
    login_page.click_login()
    sleep(3)
    cart_page.add_cart()
    cart_page.click_cart()

    # Assert Cart Description to be displayed
    assert cart_page.cart_description() == True
    print("Success: Test Case Passed for Product Description")

@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
# Test Case for Checkout Items
def test_checkout_items(driver):
    driver.get(SauceStoreData.url)
    login_page = LoginPage(driver)
    cart_page = CartPage(driver)
    base_page = BasePage(driver)
    checkout_page = CheckoutPage(driver)
    login_page.enter_username(SauceStoreData.username)
    login_page.enter_password(SauceStoreData.password)
    login_page.click_login()
    sleep(5)
    cart_page.add_cart()
    cart_page.click_cart()
    checkout_page.checkout()
    checkout_page.enter_fname(SauceStoreData.first_name)
    checkout_page.enter_lname(SauceStoreData.last_name)
    checkout_page.enter_pincode(SauceStoreData.post_code)
    checkout_page.click_cont()
    base_page.take_screenshot()
    checkout_page.click_finish()
    sleep(3)

    # Asserting the Product has been checked out
    assert checkout_page.back_product() == True
    print("Success: Test Case Passed for Checkout Items")

@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
# Test Case for Reset Function
def test_reset_function(driver):
    driver.get(SauceStoreData.url)
    login_page = LoginPage(driver)
    cart_page = CartPage(driver)
    login_page.enter_username(SauceStoreData.username)
    login_page.enter_password(SauceStoreData.password)
    login_page.click_login()
    sleep(5)
    cart_page.add_cart()
    login_page.click_hamburger()
    sleep(3)
    cart_page.reset_page()
    cart_page.click_cart()
    new_count_items = cart_page.count_items()

    # Asserting Count Items to be Zero
    assert new_count_items == 0
    print("Success: Test Case Passed for Reset Items")

@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
# Test Case for Sorting Name for Ascending Order
def test_sort_name(driver):
    driver.get(SauceStoreData.url)
    login_page = LoginPage(driver)
    cart_page = CartPage(driver)
    login_page.enter_username(SauceStoreData.username)
    login_page.enter_password(SauceStoreData.password)
    login_page.click_login()
    cart_page.sort_name_asc()
    cart_names = cart_page.fetch_names()
    sorted_names = sorted(cart_names)

    # validate the sorted Name
    assert cart_names == sorted_names, "Names are not sorted!"
    print("Success: Test Case Passed for Sorting Name")

@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
# Test Case for Sorting Price Product in Descending Order
def test_sort_price(driver):
    driver.get(SauceStoreData.url)
    login_page = LoginPage(driver)
    cart_page = CartPage(driver)
    login_page.enter_username(SauceStoreData.username)
    login_page.enter_password(SauceStoreData.password)
    login_page.click_login()
    cart_page.sort_price_desc()
    cart_prices = cart_page.fetch_product_price()
    sorted_prices = sorted(cart_prices,reverse=True)

    # validate the sorted Product Price
    assert cart_prices == sorted_prices, "Prices are not sorted!"
    print("Success: Test Case Passed for Sorting Prices")





















