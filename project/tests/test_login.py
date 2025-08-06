# Yeteneklerin farklı 
# veriler/sıralar ile çağırılarak testlerin yazılması.

#class TestLogin():
   # def test_valid_login(self):
from pages.login_page import LoginPage

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user","secret_sauce")
    assert driver.current_url == "https://www.saucedemo.com/v1/inventory.html"

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user","secret_sauce123")
    assert login_page.get_error_message() == "Epic sadface: Username and password do not match any user in this service"