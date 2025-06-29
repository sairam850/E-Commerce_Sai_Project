"""
This locator file contains all the web locators like ID, CLASS NAME, XPATH etc.,
"""

class SauceTestLocator:
    # login page
    username_locator = 'user-name'  # ID
    password_locator = 'password'  # ID
    login_button_locator = 'login-button'  # ID
    error_message = '//h3[@data-test = "error"]'  # XPATH
    # Logout Page
    hamburger_click = '//div[@class = "bm-burger-button"]'  # XPATH
    logout_click = 'logout_sidebar_link'  # ID
    # Cart Page
    cart_button = '//a[@class = "shopping_cart_link"]'  # XPATH
    inventory_name = '//div[@class = "inventory_item_name "]' # XPATH
    inventory_price = '//div[@class = "inventory_item_price"]' # XPATH
    invenory_item  = '//div[@class = "inventory_item"]' #XPATH
    product1 = 'add-to-cart-sauce-labs-backpack'  # ID
    product2 = 'add-to-cart-sauce-labs-fleece-jacket'  # ID
    product3 = 'add-to-cart-sauce-labs-onesie'  # ID
    product4 = 'add-to-cart-sauce-labs-bolt-t-shirt'  # ID
    count_items = 'shopping_cart_link'   # XPATH
    product1_details = '//div[contains(text(),"carry.allTheThings()")]' #XPATH
    product2_details = '//div[contains(text(),"fleece jacket")]' #XPATH
    product3_details = '//div[contains(text(),"Sauce Labs bolt T-shirt")]' #XPATH
    product4_details = '//div[contains(text()," Reinforced 3-snap bottom")]' #XPATH
    p1_price = '//button[@id = "add-to-cart-sauce-labs-backpack"]/preceding-sibling::div'
    product_check = '//span[contains(text(), "Products")]'  # XPATH
    reset_app_function = '//a[@id = "reset_sidebar_link" and @data-test = "reset-sidebar-link"]'  # XPATH
    sorting = 'product_sort_container'  # CLASSNAME
    sort_price = '//div[@class = "inventory_item_price"]'  # XPATH
    sort_name = '//div[@class = "inventory_item_name "]'  # XPATH
    # Checkout Page
    checkout = 'checkout'  # ID
    first_name = 'first-name'  # ID
    last_name = 'last-name'  # ID
    postalcode = 'postal-code'  # ID
    continue_button = 'continue'  # ID
    finish_button = 'finish'  # ID
    back_product = 'back-to-products'  # ID

