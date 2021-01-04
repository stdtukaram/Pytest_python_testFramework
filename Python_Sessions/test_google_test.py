from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = None
def setup_module(module):
    global driver
    driver = webdriver.Chrome(r'E:\Drive_DtoE_copy\Softwares\chromedriver.exe')
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get('http://www.google.com')

def teardown_module(module):
    driver.quit()

def test_google_title():
    assert driver.title == "Google"

def test_google_url():
    assert driver.current_url == "Google"
