from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from main.tools import  selenium_base as base
from main.tools import json_helper as data_helper
from time import sleep
import os
url = data_helper.get_user_data("user_data", "url")
def test_LWF03(web_driver):
    base.get_url(url)
    base.get_element("xpath", "enter_username").send_keys(data_helper.get_user_data("user_data", "faculty_username"))
    base.get_element("xpath", "next_btn").click()
    base.get_element("xpath", "enter_password").send_keys(data_helper.get_user_data("user_data", "faculty_password"))
    base.get_element("xpath", "sign_in_btn").click()
    base.wait_for_element_to_be_visibile(20, "xpath", "click_on_course_header")
    base.get_element("xpath", "click_on_course_header").click()
    base.wait_for_element_to_be_visibile(20, "xpath", "click on wfnen 102 course")
    base.get_element("xpath", "click on wfnen 102 course").click()
    base.wait_for_element_to_be_visibile(20, "xpath", "preview_course")
    assert base.get_element("xpath", "preview_course").is_displayed()

def test_LWF64(web_driver):
    base.get_url(url)
    base.get_element("xpath", "enter_username").send_keys(data_helper.get_user_data("user_data", "faculty_username"))
    base.get_element("xpath", "next_btn").click()
    base.get_element("xpath", "enter_password").send_keys(data_helper.get_user_data("user_data", "faculty_password"))
    base.get_element("xpath", "sign_in_btn").click()
    base.wait_for_element_to_be_visibile(25, "xpath", "ecell_button")
    base.get_element("xpath", "ecell_button").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_practicum")
    base.get_element("xpath", "click_on_practicum").click()
    sleep(2)
    base.get_element("xpath", "practicum_advanced").click()
    base.get_element("xpath","click_advanced_file").click()
    text = base.get_element("xpath", "veiw_pdf_file").text
    assert data_helper.get_user_data("user_data", "pdf_view_option") in text

def test_LWF39(web_driver):
    base.get_url(url)
    base.get_element("xpath", "enter_username").send_keys(data_helper.get_user_data("user_data", "faculty_username"))
    base.get_element("xpath", "next_btn").click()
    base.get_element("xpath", "enter_password").send_keys(data_helper.get_user_data("user_data", "faculty_password"))
    base.get_element("xpath", "sign_in_btn").click()
    base.wait_for_element_to_be_visibile(30, "xpath", "click_on_manage_batches")
    base.get_element("xpath", "click_on_manage_batches").click()
    # base.wait_for_element_to_be_clickable(25, "xpath", "edit_icon")
    base.get_element("xpath", "edit_icon1").click()
    sleep(5)
    # base.wait_for_element_to_be_visibile(10, "xpath", "edit_batches")
    # base.get_element("xpath", "edit_batches1").click()
    # sleep(5)
    # base.wait_for_element_to_be_visibile(10, "xpath", "enter_batch_name")
    # base.get_element("xpath", "enter_batch_name").clear()
    # sleep(1)
    # base.get_element("xpath", "enter_batch_name").send_keys(data_helper.get_user_data("user_data", "edit_batch_name"))
    # sleep(1)
    # base.get_element("xpath", "number_of_student").clear()
    # sleep(1)
    # base.get_element("xpath", "number_of_student").send_keys(data_helper.get_user_data("user_data", "edit_students_number"))
    # sleep(2)
    # base.get_element("xpath", "click_on_update").click()
    # sleep(9)
    # base.wait_for_element_to_be_clickable(25, "xpath", "batch_created_text")
    # assert base.get_element("xpath", "batch_created_text").is_displayed()


def test_LWF34(web_driver):
    base.get_url(url)
    base.get_url(url)
    base.get_element("xpath", "enter_username").send_keys(data_helper.get_user_data("user_data", "faculty_username"))
    base.get_element("xpath", "next_btn").click()
    base.get_element("xpath", "enter_password").send_keys(data_helper.get_user_data("user_data", "faculty_password"))
    base.get_element("xpath", "sign_in_btn").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_start_lw_33")
    base.get_element("xpath", "click_on_start_lw_33").click()
    sleep(2)
    if (base.is_element_present("xpath", "click_on_teaching_mode_btn")):
        base.wait_for_element_to_be_clickable(25, "xpath", "click_on_teaching_mode_btn")
        base.get_element("xpath", "click_on_teaching_mode_btn").click()
        sleep(2)
        base.get_element("xpath", "full_screen").click()
    sleep(2)
    greenTickDisplayed = True
    while greenTickDisplayed:
        try:
            greenTickDisplayed = base.get_element("xpath", "next_button_for_green_tick").is_displayed()
            base.get_element("xpath", "next_button_for_green_tick").click()
            sleep(3)
        except Exception:
            greenTickDisplayed = False
    sleep(2)
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_lesson")
    base.get_element("xpath", "click_on_lesson").click()
    sleep(5)
    # base.wait_for_element_to_be_clickable(25, "xpath", "click_on_resumen")
    base.get_element("xpath", "click_on_resumen").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_dashboard")
    base.get_element("xpath", "click_on_dashboard").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_resume_btn")
    base.get_element("xpath", "click_on_resume_btn").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_chapter_title")
    base.get_element("xpath", "click_on_chapter_title").click()
    sleep(2)
    web_driver.refresh()
    sleep(1)
    # Assertion
    green_tick = base.is_element_present("xpath", "assert_green_tick")  # it should return True
    print(green_tick)

def test_LWF08(web_driver):
    base.get_url(url)
    base.get_element("xpath", "enter_username").send_keys(data_helper.get_user_data("user_data", "faculty_username"))
    base.get_element("xpath", "next_btn").click()
    base.get_element("xpath", "enter_password").send_keys(data_helper.get_user_data("user_data", "faculty_password"))
    base.get_element("xpath", "sign_in_btn").click()
    base.get_element("xpath", "course_tab").click()
    base.get_element("xpath", "create_Batch").click()
    base.get_element("xpath", "Copy_Batch_Tab").click()
    text = base.get_element("xpath", "copy_batch_ass").text
    assert data_helper.get_user_data("user_data", "copy_batch") in text

def test_LW41(web_driver):
    base.get_url(url)

    base.get_element("xpath", "enter_username").send_keys(data_helper.get_user_data("user_data", "faculty_username"))
    base.get_element("xpath", "next_btn").click()
    base.get_element("xpath", "enter_password").send_keys(data_helper.get_user_data("user_data", "faculty_password"))
    base.get_element("xpath", "sign_in_btn").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_course_plan")
    base.get_element("xpath", "click_on_course_plan").click()
    base.wait_for_element_to_be_visibile(25, "xpath", "assert_course_plan")
    assert data_helper.get_user_data("user_data", "assert_course_plan") in base.get_element("xpath",
                                                                                            "assert_course_plan").text
    base.get_element("xpath", "Mark_as_complete").click()
    sleep(2)
    base.get_element("xpath", "click_on_yes_btn").click()
    base.get_element("xpath", "star_rating_mark_as_completed").click()
    base.get_element("xpath", "star_mark_submit_btn").click()
    sleep(9)
    # assertion
    feedback_rating = base.is_element_present("xpath", "feedback_submit_rating_lesson_5")  # it shoud return True
    print(feedback_rating)
    # base.wait_for_element_to_be_visibile(10, "xpath", "edit_std_ass")
    # text = base.get_element("xpath", "edit_std_ass").text
    # print(text)
    # assert data_helper.get_user_data("user_data", "batch_name_copy") in base.get_element("xpath", "edit_std_ass").text














