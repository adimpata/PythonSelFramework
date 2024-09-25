import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

driver = None


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="firefox", help="Specify the browser name")


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service = ChromeService(executable_path="chromedriver.exe")
        driver = webdriver.Chrome(service=service)
    elif browser_name == "firefox":
        service = FirefoxService(executable_path="geckodriver.exe")
        driver = webdriver.Firefox(service=service)
    elif browser_name == "IE":
        print("IE driver not implemented yet.")
        raise ValueError("IE driver is not implemented yet. Please choose another browser.")
    else:
        raise ValueError(f"Browser {browser_name} is not supported")

    if driver:
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.maximize_window()
        request.cls.driver = driver

        yield
        driver.quit()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
