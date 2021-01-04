from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import pytest

driver = None
@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("========================================== set up =======================================")
    driver = webdriver.Chrome(r'E:\Drive_DtoE_copy\Softwares\chromedriver.exe')
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get('https://www.google.com')
    yield
    print("========================================= tear down ======================================")
    driver.quit()

# @pytest.mark.usefxtures('init_driver')
def test_google_title(init_driver):
    assert driver.title == "Google"
# @pytest.mark.usefixtures('init_driver')
def test_google_url(init_driver):
    assert driver.current_url == "Google"