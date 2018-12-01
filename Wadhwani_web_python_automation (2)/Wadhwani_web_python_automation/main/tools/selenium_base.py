from selenium.webdriver.support.ui import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from main.tools import json_helper as json_data
import conftest

def get_url(url):
   return get_driver().get(url)

def get_driver():
    """
    method used to get initialized driver.

    :Usage:
       conftest.get_driver()

    :return: Web/Mobile driver
    """
    return conftest.get_driver()

def delete_history():
    return get_driver().delete_all_cookies()

def get_locator_value(locator_type, locator_name):
    """
    method used to get locator values from locators.py
    :param locator_type: xpath, Id, name, class_name..
    :param locator_name: key_name given to locator
    :return: locator value

    :Usage:
       driver.get_locator_value('id','password')

    """
    return json_data.get_locators(locator_type, locator_name)

def get_element(locator_type, locator_name):
    """
    method is used to get web element
    :param locator_type: xpath, Id, name, class_name..
    :param locator_name: key_name given to locator
    :return: WebElement

    :Usage:
       driver.get_element('xpath','password')

    """
    return get_driver().find_element(get_locator_type(locator_type), get_locator_value(locator_type, locator_name))


def get_elements(locator_type, locator_name):
    """
    method is used to get Web Elements
    :param locator_type: xpath, Id, name, class_name..
    :param locator_name: key_name given to locator
    :return: Web Elements

    :Usage:
       driver.get_elements('xpath','password')

    """
    return get_driver().find_elements(get_locator_type(locator_type), get_locator_value(locator_type, locator_name))

def is_element_present(locator_type, locator_name):
    """
    method is used to check is element present
    :param locator_type: xpath, Id, name, class_name..
    :param locator_name: key_name given to locator
    :return: True/False

    :Usage:
       driver.is_element_present('xpath','user_name')

    """
    try:
        get_element(locator_type, locator_name)
    except NoSuchElementException:
        return False
    return True


def wait_for_element_to_be_clickable(timeOut, locator_type, locator_value):
    """
    method is used to wait for element to be clickable
    :param timeOut: Amount of time to wait (in seconds)
    :param locator_type: xpath, Id, name, class_name..
    :param locator_name: key_name given to locator

    :Usage:
       driver.wait_for_element_to_be_clickable('xpath','user_name')
    """
    WebDriverWait(get_driver(), timeOut).until(
       expected_conditions.element_to_be_clickable(
                 (get_locator_type(locator_type), get_locator_value(locator_type, locator_value))))


def wait_for_element_to_be_visibile(timeOut,locator_type,locator_value):
    """
    method is used to wait for element visibility
    :param timeOut: Amount of time to wait (in seconds)
    :param locator_type: xpath, Id, name, class_name..
    :param locator_name: key_name given to locator
    :return: Element not visible string

    :Usage:
       driver.wait_for_element__to_be_visibility('xpath','user_name')

    """
    try:
        WebDriverWait(get_driver(), timeOut).until(
        expected_conditions.visibility_of_element_located((get_locator_type(locator_type),get_locator_value(locator_type,locator_value))))
    except TimeoutException:
        return "Element is not visible"


def get_locator_type(locator_type):
    """
    method is used to get locator type
    :param locator_type:
    :return: By.XPATH, By.ID, By.CLASS_NAME..

    :Usage: get_locator_type('xpath'), get_locator_type('id')..

    """
    if locator_type=='xpath': return By.XPATH
    elif locator_type=='id': return By.ID
    elif locator_type=='class_name': return By.CLASS_NAME
    elif locator_type=='css_selector': return By.CSS_SELECTOR
    elif locator_type=='name': return By.NAME



def navigate_to_url(url):
    get_driver().get(url)

