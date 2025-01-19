import pytest
from playwright.sync_api import sync_playwright
import os
import datetime

@pytest.fixture()
def setup():
    p=sync_playwright().start()
    browser = p.chromium.launch(headless=False)  # Set to True for headless execution
    page = browser.new_page()
    try:
        yield page
    finally:
        p.stop()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    if 'setup' in item.funcargs:
        page = item.funcargs['setup']
        pytest_html = item.config.pluginmanager.getplugin('html')
        extra = getattr(report, 'extra', [])
        if report.when == 'call' or report.when == "setup":
            xfail = hasattr(report, 'wasxfail')
            if (report.skipped and xfail) or (report.failed and not xfail):
                file_name = report.nodeid.replace("::", "@")
                file_name = file_name.replace("/", "@")
                file_list1 = file_name.split("@")
                date = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
                date = date.replace(' ', "_")
                date = date.replace(':', "_")
                date = date.replace(',', '_')
                date = date.replace('.', '_')
                file_path = os.getcwd() + "/reports/Screenshots/" + file_list1[-1] + file_list1[1] + date + '.png'
                page.screenshot(path=file_path)
                if file_path:
                    html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                           'onclick="window.open(this.src)" align="right"/></div>' % file_path.replace("%20",
                                                                                                       "%2520")
                    extra.append(pytest_html.extras.html(html))
                report.extra = extra