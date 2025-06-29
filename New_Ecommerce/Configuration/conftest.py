import pytest
from selenium import webdriver


# updated driver with cross browser testing
def get_driver(browser):
    if browser.lower() == "chrome":
        my_driver = webdriver.Chrome()
    elif browser.lower() == "firefox":
        my_driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    my_driver.maximize_window()
    return my_driver


@pytest.fixture(scope="function")
def driver(request):
    browser = request.param  # Passed via test param
    driver = get_driver(browser)
    yield driver
    driver.quit()