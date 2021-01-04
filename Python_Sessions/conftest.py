import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(params = ["Chrome", "Firefox"], scope = "class")
def init_driver(request):
    if request.param == "Chrome":
        wb_driver = webdriver.Chrome(ChromeDriverManager().install())
        # wb_driver = webdriver.Chrome(r'E:\Drive_DtoE_copy\Softwares\chromedriver\chromedriver.exe')
    if request.param == "Firefox":
        wb_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        # wb_driver = webdriver.Firefox(r'E:\Drive_DtoE_copy\Softwares\geckodriver\geckodriver.exe')
    request.cls.driver = wb_driver

    yield

    wb_driver.close()
