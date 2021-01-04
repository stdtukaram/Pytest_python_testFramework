
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

import time

def test_Google():
    driver = webdriver.Chrome(r'E:\Drive_DtoE_copy\Softwares\chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get("https://www.google.com")
    assert driver.title == "Google"
    driver.quit()

def test_Facebook():
    driver = webdriver.Chrome(r'E:\Drive_DtoE_copy\Softwares\chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get("https://www.facebook.com")
    assert driver.title == "Facebook – log in or sign up"
    driver.quit()

def test_Gmail():
    driver = webdriver.Chrome(r'E:\Drive_DtoE_copy\Softwares\chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get("https://www.gmail.com")
    assert driver.title == "Gmail"
    driver.quit()

def test_Instagram():
    driver = webdriver.Chrome(r'E:\Drive_DtoE_copy\Softwares\chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get("https://www.Instagram.com")
    assert driver.title == "Instagram"
    driver.quit()

def test_Twitter():
    driver = webdriver.Chrome(r'E:\Drive_DtoE_copy\Softwares\chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get("https://www.twitter.com")
    assert driver.title == "Twitter. It’s what’s happening / Twitter"
    driver.quit()




