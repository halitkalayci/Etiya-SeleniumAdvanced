from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

def test_shadow_dom():
    driver = Chrome()
    driver.get("https://books-pwakit.appspot.com/")
    
    book_app = driver.find_element(By.TAG_NAME, "book-app")

    shadow_root_1 = book_app.shadow_root #Selenium üzerinde halihazırda varsa.
    #shadow_root_1 = driver.execute_script("return arguments[0].shadowRoot", book_app) 
    # Seleniumda destek yoksa ya da daha zorsa, JS ile çalıştıralabilir.

    app_header = shadow_root_1.find_element(By.CSS_SELECTOR, "app-header")
    # Eğer aradığım eleman shadow dom altında ise, önce o shadow dom'a focus olmalıyız.
    search_input = app_header.find_element(By.ID, "input")

    search_input.send_keys("Orhan Pamuk")