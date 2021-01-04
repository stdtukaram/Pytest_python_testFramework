import pytest
from selenium import webdriver

"""
To run test in parally
-v  tun the rest in more clear
-s  for any print fnction
-n2 n - run the test paralaly 2 two workers (in two browser)
pytest test_fixture_params.py -v -s -n 2 --html=test_fixture_params_report.html


PYCHARM SHORTCUT COMMENTs
https://shortcutworld.com/PyCharm/win/JetBrains-PyCharm_Shortcuts
"""

# @pytest.fixture(params=["Chrome", "Firefox"], scope="class")
# def init_driver(request):
#     if request.param == "Chrome":
#         wb_driver = webdriver.Chrome(r'E:\Drive_DtoE_copy\Softwares\chromedriver.exe')
#     if request.param == "Firefox":
#         wb_driver = webdriver.Firefox(r'E:\Drive_DtoE_copy\Softwares\geckodriver.exe')
#
#     request.cls.driver = wb_driver
#     yield
#     wb_driver.quit()

@pytest.mark.usefixtures("init_driver")
class Base_Test:
    pass

class Test_Google(Base_Test):

    def test_google_title(self):
        self.driver.get("https://www.google.com")
        assert self.driver.title == "Google"

    def test_google_url(self):
        self.driver.get("https://www.google.com")
        assert self.driver.current_url == "google.com"
