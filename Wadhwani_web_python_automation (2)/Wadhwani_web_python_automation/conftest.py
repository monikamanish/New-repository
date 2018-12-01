import pytest
from main.tools import json_helper as data_reader
from selenium import webdriver
# from appium import webdriver as mobiledriver
# import allure
# from allure.constants import AttachmentType

driver = None

@pytest.fixture(scope='module')   # if you will remove this modules then browser will launch every time (scope='module')
def web_driver(request):

   """
   Fixture is used to setup and tear down web driver for browser

   :Usage: web_driver()

   """
   browser_type= data_reader.get_user_data('user_data','browser_name').upper()
   url=data_reader.get_user_data('user_data','url')

   if browser_type=="CHROME":
       browser_driver= webdriver.Chrome(data_reader.get_user_data('user_data','chrome_driver_path'))
   elif browser_type=="MOZILLA":
       browser_driver= webdriver.Firefox(data_reader.get_user_data('user_data','gecko_driver_path'))
   elif browser_type=="IE":
       browser_driver= webdriver.Ie(data_reader.get_user_data('user_data','Ie_driver_path'))
   elif browser_type=="SAFARI":
       browser_driver= webdriver.Safari(data_reader.get_user_data('user_data','safari_driver_path'))
   else:
       browser_driver = None
       print("Invalid browser name")
   browser_driver.implicitly_wait(10) # seconds
   browser_driver.maximize_window()
   browser_driver.get(url) # Needs to initiate while calling from test case
   set_driver(browser_driver)

   def teardown():
       print('\nresources_a_teardown()')
       browser_driver.quit()
   request.addfinalizer(teardown)

   return browser_driver

@pytest.fixture(scope='module')
def mobile_driver(request):
   """
   Fixture is used to setup and tear down appium driver for mobile apps

   :Usage: mobile_driver()

   """
   print("\nEntered mobile_driver fixture")
   caps = {}
   caps["platformName"] = data_reader.get_user_data('user_data','platformName')
   caps["platformVersion"] = data_reader.get_user_data('user_data','platformVersion')
   caps["deviceName"] = data_reader.get_user_data('user_data','deviceName')
   caps["udid"] = data_reader.get_user_data('user_data','udid')
   caps["app"] = data_reader.get_user_data('user_data','app')
  # android_driver = mobiledriver.Remote("http://localhost:4723/wd/hub", caps)
   #android_driver.implicitly_wait(60) # seconds
   # set_driver(android_driver)

   def teardown():
       print('\nresources_a_teardown()')
       # android_driver.quit()

   request.addfinalizer(teardown)

   #return android_driver

def set_driver(driver_instance):
   """
   Method is used to set web driver instance
   :param browser_driver: webdriver

   :Usage: set_web_driver(webdriver)

   """
   global driver
   driver=driver_instance

def get_driver():
   """
   Method is used to get driver

   :Usage: get_driver()
   :return: driver (webdriver/mobile driver)
   """
   return driver


def delete_history(browser_driver):
   browser_driver.delete_all_cookies()

'''
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport():
   """
   Method will be called incase of test case failure, screenshots will be captured and
   and will be attached to allure reports
   """
   outcome = yield
   rep = outcome.get_result()
   if rep.failed:
       allure.attach('.', driver.get_screenshot_as_png(), type=AttachmentType.PNG)

'''

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

