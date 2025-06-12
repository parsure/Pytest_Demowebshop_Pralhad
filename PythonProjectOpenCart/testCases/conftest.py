import datetime
import os
import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pageObjects.homePage import HomePage
from pageObjects.landingPage import LandingPage
from pageObjects.loginPage import LoginPage
from utilities.customLogger import LogGenerator
from utilities.readProperties import config, ReadProperties


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="browser selection")


logger=LogGenerator.get_logger("Fixture")
@pytest.fixture(scope="class")
def set_up(request):
    browser_name=request.config.getoption("--browser_name")
    logger.info("***invoking the browser***")
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        driver=webdriver.Chrome()
    elif browser_name== "firefox":
        options = webdriver.FirefoxOptions()
        driver=webdriver.Firefox()
    elif browser_name=="edge":
        options = webdriver.EdgeOptions()
        driver=webdriver.Edge(options=options)

    driver.delete_all_cookies()
    driver.maximize_window()
    driver.implicitly_wait(5)
    logger.info("***browser invoked***")
    yield driver
    logger.info("***logging out the app***")
    home_page_object = HomePage(driver)
    time.sleep(3)
    try:
        home_page_object.click_logout_button()
    except:
        driver.quit()
    logger.info("***successfully logged out***")
    logger.info("***closing the browser***")
    driver.quit()
    logger.info("***browser closed***")

@pytest.fixture(scope="class")
def login_to_app(set_up):
    driver = set_up
    logger.info("***hitting url in browser***")
    url=ReadProperties.get_base_url()

    driver.get(url)

    LandingPage(driver).click_on_log_in_link()
    logger.info("***clicked on login link***")
    login_page_object=LoginPage(driver)
    email=ReadProperties.get_user_name()
    password=ReadProperties.get_user_password()
    login_page_object.setUserName(email)
    login_page_object.setUserPwd(password)
    login_page_object.setLoginButton()
    logger.info("***clicked on login button***")
    yield driver




@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    reports_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "reports")
    os.makedirs(reports_dir, exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = f"report_{timestamp}.html"
    config.option.htmlpath = os.path.join(reports_dir, report_file)

# ✅ Add metadata to the HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata["Project Name"] = "Demo Web Shop"
    metadata["Module Name"] = "Account Registration"
    metadata["Tester"] = "Pralhad"


'''@pytest.mark.optionalhook
def pytest_metadata(metadata):
    config._metadata["Project Name"] = "Demo Web shop"
    config._metadata["Module Name"] = "Account Registration"
    config._metadata["Tester"] = "Pralhad"

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlPath=os.path.join(os.path.dirname(os.path.dirname(__file__)), "reports", "report.html")'''