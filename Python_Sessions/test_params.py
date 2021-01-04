import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# IMPORT webdrivers from "conftest" method
@pytest.mark.usefixtures("init_driver")
# Write base class
class BaseTest():
    pass

# Inherit the Bsase class and write test cases for different username and password
class TestHumSpot(BaseTest):

    @pytest.mark.parametrize(
                               "username, password",
                                [
                                   ("admin@gmail.com", "admin123"),
                                   ("naveen@gmail.com", "naveen123")
                                ]
                             )
    def test_login(self, username, password):
        """
        This method is used to login Hubspot using different logins i.e. username and password
        :param username:
        :param password:
        :return:
        """
        self.driver.get("https://app.hubspot.com/login")
        self.driver.find_element(By.ID, "username").send_key(username)
        time.sleep(3)
        self.driver.find_element(By.ID, "password").send_key(password)
        time.sleep(3)

