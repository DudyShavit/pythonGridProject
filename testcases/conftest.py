import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import os
from webdriver_manager.firefox import GeckoDriverManager


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(params=["chrome","firefox"],scope="function")
def get_browser(request):
    remote_url = "http://localhost:4444/wd/hub"
    if request.param == "chrome":
        caps = {'browserName': os.getenv('BROWSER', 'chrome')}
        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=caps
        )

    if request.param == "firefox":
        caps = {'browserName': os.getenv('BROWSER', 'firefox')}
        driver = webdriver.Remote(
           command_executor='http://localhost:4444/wd/hub',
           desired_capabilities=caps
        )

    driver.get("http://facebook.com")
    driver.maximize_window()
    yield driver
    driver.quit()