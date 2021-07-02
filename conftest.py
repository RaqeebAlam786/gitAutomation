# !/usr/bin/python
# --*-- coding:utf-8 --*--
from datetime import datetime

import pytest

# @pytest.yield_fixture(scope='session')
# def browser():
#     from selenium import webdriver
#     driver = webdriver.Chrome()
#     yield driver
#     driver.quit()

# from selenium import webdriver
# import pytest
# driver = None
#
#
# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#     Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
#     :param item:
#     """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::", "_")+".png"
#             _capture_screenshot(file_name)
#             if file_name:
#                 html = '<div><img src="file:/C:/SeleniumProject/Pytest_HTML_ScreenShot/ScreenShots/%s" alt="screenshot" style="width:600px;height:228px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>'%file_name
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#
#
# def _capture_screenshot(name):
#     driver.get_screenshot_as_file("C:\\SeleniumProject\\Pytest_HTML_ScreenShot\\ScreenShots\\"+name)
#     # driver.get_screenshot_as_file(name)
#
#
#
# @pytest.fixture(scope='session', autouse=True)
# def browser():
#     global driver
#     if driver is None:
#         driver = webdriver.Chrome()
#     yield driver
#     driver.quit()
#     return driver

import pytest
import webbrowser

from selenium.webdriver.chrome import options
from selenium import webdriver


@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome('resources//chromedriver.exe', options=options)
    driver.get('http://www.gogle.com')
    driver.implicitly_wait(5)

    return driver


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        # always add url to report
        extra.append(pytest_html.extras.url('http://www.dev.quicklly.com/'))
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            name = datetime.strftime(datetime.now(), '%m-%d_%H-%M-%S')
            extra.append(pytest_html.extras.image(
                "/var/lib/jenkins/workspace/Quicklly/screenshots"+f'screenshot{name}.png'))
            extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
        report.extra = extra
