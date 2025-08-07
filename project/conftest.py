# Global Test Ayarları
import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from utils.screenshot import take_screenshot
@pytest.fixture # bütün test fonksiyonlarına enjekte edilecek bağımlılık.
def driver():
    options = Options()
    #options.add_argument("--headless")
    driver = Chrome(options=options)
    driver.maximize_window()
    yield driver # returnun multiple hali.
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call":
        driver = item.funcargs.get("driver", None)
        if driver is not None:
            take_screenshot(driver, item.name)
