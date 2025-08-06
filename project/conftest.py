# Global Test Ayarları
import pytest
from selenium.webdriver import Chrome

@pytest.fixture # bütün test fonksiyonlarına enjekte edilecek bağımluluk.
def driver():
    driver = Chrome()
    yield driver # returnun multiple hali.
    driver.quit()