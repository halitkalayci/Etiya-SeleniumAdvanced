from pages.login_page import LoginPage
from utils.csv_reader import read_csv_data
import pytest
from utils.screenshot import take_screenshot

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user","secret_sauce")
    take_screenshot(driver, "test_valid_login")
    assert driver.current_url == "https://www.saucedemo.com/v1/inventory.html"

def test_validation(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("","")
    take_screenshot(driver, "test_validation")
    assert login_page.get_error_message() == "Epic sadface: Username is required"

@pytest.mark.parametrize("username,password", [("abc123","1234")])
def test_invalid_login(driver, username, password):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(username,password)
    take_screenshot(driver, "test_invalid_login")
    assert login_page.get_error_message() == "Epic sadface: Username and password do not match any user in this service"


# run-time -> kodun çalıştığı an
# compile-time -> kodun çalıştırılabilir hale getirildiği an (build)