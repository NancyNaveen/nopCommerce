from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="H:\\Python\\Drivers\\chromedriver.exe")
        print("Launching Chrome browser..............")
    elif browser == 'ie':
        driver = webdriver.Ie(executable_path="H:\\Python\\Drivers\\IEDriverServer.exe")
        print("Launching Internet Explorer browser ................")
    else:
        driver = webdriver.Edge(executable_path="H:\\Python\\Drivers\\msedgedriver.exe")
        print("Launching Microsoft Edge browser ................")
    return driver


# To get the browser name from CLI/hook
def pytest_addoption(parser):
    parser.addoption("--browser")


# Returns browser value to setup method
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


##### PyTest HTML Report #####

# This is hook for Adding Environment Info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Nancy'

# Ths is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA HOME", None)
    metadata.pop("Plugins", None)
