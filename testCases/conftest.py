import pytest
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        # serv_obj = Service("C:\\WebDrivers\\chromedriver.exe")
        driver = webdriver.Chrome()  # service=serv_obj)
        print("launching chrome browser.............")
    elif browser == 'firefox':
        # serv_obj = Service("C:\\WebDrivers\\geckodriver.exe")
        driver = webdriver.Firefox()  # service=serv_obj)
        print("launching firefox browser.............")
    else:
        # serv_obj = Service("C:\\WebDrivers\\msedgedriver.exe")
        driver = webdriver.Edge()  # service=serv_obj)
        print("launching edge browser.............")

    return driver


def pytest_addoption(parser):  # this will get the value from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):          # this will return the browser value to the setup method
    return request.config.getoption("--browser")

# # ############### pytest html report ###########
#
# # it is hooking for adding environment info to HTML report
#
#
# def pytest_configure(config):
#     config.metadata['project name'] = 'nop Commerce'
#     config.metadata['Module name'] = 'customer'
#     config.metadata['tester'] = 'veeresh'
#
# # it is hooking for delete/modify environment info to HTML report
#
#
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop('JAVA_HOME', None)
#     metadata.pop('Plugins', None)