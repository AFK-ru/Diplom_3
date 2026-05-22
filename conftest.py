import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):

    browser_name = request.param
    _driver = None

    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--window-size=1920,1080")
        service = ChromeService(ChromeDriverManager().install())
        _driver = webdriver.Chrome(service=service, options=chrome_options)

    elif browser_name == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument("--width=1920")
        firefox_options.add_argument("--height=1080")
        service = FirefoxService(GeckoDriverManager().install())
        _driver = webdriver.Firefox(service=service, options=firefox_options)

    yield _driver

    if _driver is not None:
        _driver.quit()
