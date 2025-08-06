# Global Test Ayarları
import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

@pytest.fixture # bütün test fonksiyonlarına enjekte edilecek bağımluluk.
def driver():
    options = Options()
    #options.add_argument("--headless")
    driver = Chrome(options=options)
    yield driver # returnun multiple hali.
    driver.quit()