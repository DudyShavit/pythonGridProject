import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import os


# caps = {'browserName': os.getenv('BROWSER', 'firefox')}
# browser = webdriver.Remote(
#     command_executor='http://localhost:4444/wd/hub',
#     desired_capabilities=caps
# )

from selenium import webdriver

capabilities = {
    "browserName": "firefox",
    "browserVersion": "92.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": True
    }
}

browser = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    desired_capabilities=capabilities)
browser.get("https://www.google.com")
time.sleep(3)
browser.maximize_window()

title = browser.title

print(title)

assert "Google" == title

browser.close()

#browser.quit()