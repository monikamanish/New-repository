from main.requirements import locators as locator_path
from main.requirements import user_data as user_data_path

file_path= None


def set_file_path(file_path_value):
    """
    Method is used to set file path for data reader
    :param file_path_value: file_path
    """
    global file_path
    file_path=file_path_value

def get_file_path():
    """
    Method is used to get path file of data reader
    :return: file path
    """
    return file_path


def get_locators(locator_type, locator_name):
    """
    Method is used to get locators value from locators.py file
    :param locator_type: xpath, id, name..
    :param locator_name: key value
    :return: locator value

    :Usage: get_locators('xpath','connect')
    """
    return locator_path.locators.get(locator_type).get(locator_name)

def get_user_data(data_key):
    """
    Method is used to get user data from user_data.py file
    :param data_key: data key
    :return: data value


    :Usage: get_user_data('connect')
    """
    return user_data_path.user_dict.get('user_data').get(data_key)

def get_user_data(node_name,data_key):
    """
    Method is used to get user data from user_data.py file
    :param node_name: node name
    :param data_key: data key
    :return: data value

    :Usage: get_user_data('user_data','connect')
    """
    return user_data_path.user_dict.get(node_name).get(data_key)

