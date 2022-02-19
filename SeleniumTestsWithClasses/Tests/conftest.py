import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.common.by import By


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')  # Use headless if don't need a browser UI
    options.add_argument('--start -maximized')
    options.add_argument('--window-size = 1650, 900')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome('C:/WebDriver/chromedriver.exe', options=options)
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://www.macys.com/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    if driver.find_element(By.ID, 'tinybox'):
        close_link = driver.find_element(By.ID, 'closeButton')
        if close_link:
            close_link.click()
    driver.delete_all_cookies()
    yield driver
    driver.quit()

# @pytest.fixture
# def tearDown(get_webdriver):
#     driver = get_webdriver
#     driver.quit()
