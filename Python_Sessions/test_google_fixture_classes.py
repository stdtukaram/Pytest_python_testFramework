from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager

import pytest

@pytest.fixture(scope = "class")
def init_chrome_driver(request):
    #ch_driver = webdriver.chrome(ChromeDriverManager().install())
    ch_driver = webdriver.Chrome(r'E:\Drive_DtoE_copy\Softwares\chromedriver.exe')
    request.cls.driver = ch_driver
    yield
    ch_driver.close()

@pytest.fixture(scope = "class")
def init_ff_driver(request):
    #ff_driver = webdriver.Firefox(executable_path = GeckoDriverManager().install())
    ff_driver = webdriver.Chrome(r'E:\Drive_DtoE_copy\Softwares\geckodriver.exe')
    request.cls.driver = ff_driver
    yield
    ff_driver.close()

@pytest.mark.usefixtures(init_chrome_driver)
class Base_Chrome_Test:
    pass
class Test_Google_Chrome(Base_Chrome_Test):
    # write test cases using chrome browser
    #TEST-01 verify the google title
    def test_google_title_chrome(self):
        self.driver.get("https://www.google.com")
        assert self.driver.title == "Google"
    def test_google_url_chrome(self):
        assert self.driver.current_url == "https://www.google.com"

@pytest.mark.usefixtures(init_ff_driver)
class Base_Firefox_Test:
    pass

class Test_Google_Firefox(Base_Firefox_Test):

    def test_google_title_firefox(self):
        self.driver.get("https://www.google.com")
        assert self.driver.title == "Googel"
