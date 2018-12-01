from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from Projec
from Wadhwani_web_python_automation.main.tools import json_helper as data_helper
from time import sleep
import os
url = data_helper.get_user_data("user_data", "url")

def test_LWF01(web_driver):
    base.get_url(url)
    base.get_element("xpath", "enter_username").send_keys(data_helper.get_user_data("user_data", "invalid_email_id"))
    # assertion
    check = base.get_element("xpath", "assert_disabled_next")
    print(check.is_enabled())

def test_LWF02(web_driver):
    base.get_url(url)
    base.get_element("xpath", "enter_username").send_keys(data_helper.get_user_data("user_data", "email_for_unregistered"))
    base.get_element("xpath", "next_btn").click()
    assert data_helper.get_user_data("user_data", "student_reg") in base.get_element("xpath","student_registration").text

def test_LWF03(web_driver):
    base.get_url(url)
    base.get_element("xpath", "enter_username").send_keys(data_helper.get_user_data("user_data", "valid_email_id"))
    base.get_element("xpath", "next_btn").click()
    base.get_element("xpath", "enter_password").send_keys(data_helper.get_user_data("user_data", "incorrect_password"))
    base.get_element("xpath", "sign_in_btn").click()
    assert data_helper.get_user_data("user_data", "error_message") in base.get_element("xpath","error_message").text

def test_LWF04(web_driver):
    base.get_url(url)
    base.get_element("xpath", "enter_username").send_keys(data_helper.get_user_data("user_data", "faculty_username"))
    base.get_element("xpath", "next_btn").click()
    base.get_element("xpath", "enter_password").send_keys(data_helper.get_user_data("user_data", "faculty_password"))
    base.get_element("xpath", "sign_in_btn").click()
    sleep(3)
    # assertion
    list_batches = base.get_elements("xpath", "dashboard_batches")
    for batches_name in list_batches:
        print(batches_name.text)




def test_LWF05(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_visibile(20, "xpath", "click_on_course_header")
    base.get_element("xpath", "click_on_course_header").click()
    base.wait_for_element_to_be_visibile(20, "xpath", "click on wfnen 102 course")
    base.get_element("xpath", "click on wfnen 102 course").click()
    sleep(5)
    base.wait_for_element_to_be_visibile(20, "xpath", "preview_course")
    assert base.get_element("xpath", "preview_course").is_displayed()




def test_LWF06(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_visibile(20, "xpath", "click_on_course_header")
    base.get_element("xpath", "click_on_course_header").click()
    base.wait_for_element_to_be_visibile(20, "xpath", "click on wfnen 102 course")
    base.get_element("xpath", "click on wfnen 102 course").click()
    base.wait_for_element_to_be_visibile(20, "xpath", "preview_course")
    base.get_element("xpath", "preview_course").click()
    base.wait_for_element_to_be_visibile(20, "xpath", "list_of_lesson")
    # assertion
    list = base.get_elements("xpath", "list_of_lesson")
    for lesson in list:
        print(lesson.text)

def test_LWF07(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_course_header")
    base.get_element("xpath", "click_on_course_header").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "create_batch_in_100")
    base.get_element("xpath", "create_batch_in_100").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_create_new_batch")
    base.get_element("xpath", "click_on_create_new_batch").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "enter_batch_name")
    base.get_element("xpath", "enter_batch_name").send_keys(data_helper.get_user_data("user_data", "enter_batch_name"))
    base.get_element("xpath", "number_of_student").send_keys(data_helper.get_user_data("user_data", "enter_num_of_students"))
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_date_picker")
    base.get_element("xpath", "click_on_date_picker").click()
    sleep(2)
    base.get_element("xpath", "select_date").click()
    sleep(2)
    base.get_element("xpath", "create_batch").click()
    sleep(9)
    base.wait_for_element_to_be_clickable(25, "xpath", "batch_created_text")
    assert  base.get_element("xpath", "batch_created_text").is_displayed()

def test_LWF08(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "course_tab")
    base.get_element("xpath", "course_tab").click()
    base.wait_for_element_to_be_clickable(20, "xpath", "create_Batch")
    base.get_element("xpath", "create_Batch").click()
    base.get_element("xpath", "Copy_Batch_Tab").click()
    text = base.get_element("xpath", "copy_batch_ass").text
    assert data_helper.get_user_data("user_data", "copy_batch") in text
def test_LWF09(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_course_header")
    base.get_element("xpath", "click_on_course_header").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_wfnen_101_course")
    base.get_element("xpath", "click_on_wfnen_101_course").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "create_batch_in_101")
    base.get_element("xpath", "create_batch_in_101").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_create_new_batch_101")
    base.get_element("xpath", "click_on_create_new_batch_101").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "enter_batch_name")
    base.get_element("xpath", "enter_batch_name").send_keys(data_helper.get_user_data("user_data", "enter_batch_name_for_101"))
    base.get_element("xpath", "number_of_student").send_keys(data_helper.get_user_data("user_data", "enter_num_of_students"))
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_date_picker")
    base.get_element("xpath", "click_on_date_picker").click()
    sleep(2)
    base.get_element("xpath", "select_date").click()
    sleep(2)
    base.get_element("xpath", "create_batch").click()
    sleep(10)
    base.wait_for_element_to_be_clickable(25, "xpath", "batch_created_text")
    assert base.get_element("xpath", "batch_created_text").is_displayed()
    sleep(2)
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_course_header")
    base.get_element("xpath", "click_on_course_header").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "create_batch_in_100")
    base.get_element("xpath", "create_batch_in_100").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_copy_batch")
    base.get_element("xpath", "click_on_copy_batch").click()
    # assertion
    list =  base.get_elements("xpath", "assert_copy_batch_list")
    for batches in list:
        print(batches.text)

def test_LWF10(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_manage_batches")
    base.get_element("xpath", "click_on_manage_batches").click()
    elem_1=base.get_driver().find_elements_by_xpath("//*[@ng-repeat='batch in batches.activeBatches']")
    print("count of active_batches :" + str(len(elem_1)))
    count_1 = str(len(elem_1))
    sleep(1)
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_course_header")
    base.get_element("xpath", "click_on_course_header").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "create_batch_in_100")
    base.get_element("xpath", "create_batch_in_100").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_copy_batch")
    base.get_element("xpath", "click_on_copy_batch").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "assert_copy_batch_list")
    base.get_element("xpath", "assert_copy_batch_list").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "enter_batch_name")
    base.get_element("xpath", "enter_batch_name").send_keys(data_helper.get_user_data("user_data", "enter_copy_batch"))
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_date_picker")
    base.get_element("xpath", "click_on_date_picker").click()
    sleep(2)
    base.get_element("xpath", "select_date").click()
    sleep(2)
    base.get_element("xpath", "star_mark_submit_btn").click()
    sleep(12)
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_manage_batches")
    base.get_element("xpath", "click_on_manage_batches").click()
    web_driver.refresh()
    elem_2 = base.get_driver().find_elements_by_xpath("//*[@ng-repeat='batch in batches.activeBatches']")
    print("count of active_batches :" + str(len(elem_2)))
    count_2 = str(len(elem_2))
    assert count_1 not in count_2

def test_LWF11(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_visibile(25, "xpath", "click_on_course_header")
    base.get_element("xpath", "click_on_course_header").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "create_batch_in_100")
    base.get_element("xpath", "create_batch_in_100").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_copy_batch")
    base.get_element("xpath", "click_on_copy_batch").click()
    base.get_element("xpath", "search_copy_batch").send_keys(data_helper.get_user_data("user_data", "search_copy_batch"))
    base.wait_for_element_to_be_clickable(25, "xpath", "copy_batch_search_icon")
    base.get_element("xpath", "copy_batch_search_icon").click()
    try:
        list = base.get_elements("xpath", "assert_copy_batch_list")
        for batches in list:
            print(batches.text)
    except NoSuchElementException:
        print("BATCH NOT FOUND")

def test_LWF12(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_course_header")
    base.get_element("xpath", "click_on_course_header").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_start_course")
    base.get_element("xpath", "click_on_start_course").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_ok")
    base.get_element("xpath", "click_on_ok").click()
    base.wait_for_element_to_be_visibile(20, "xpath", "list_of_lesson")
    # assertion
    list = base.get_elements("xpath", "list_of_lesson")
    for lesson in list:
        print(lesson.text)

def test_LWF13(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_course_header")
    base.get_element("xpath", "click_on_course_header").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_start_course")
    base.get_element("xpath", "click_on_start_course").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_ok")
    base.get_element("xpath", "click_on_ok").click()
    Select(web_driver.find_element_by_id('user-batch-switch')).select_by_index(1)
    sleep(3)
    assert base.get_element("xpath", "click_on_ok").is_displayed()

def test_LWF14(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_dashboard")
    base.get_element("xpath", "click_on_dashboard").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "course_name_link_wfnen_100")
    base.get_element("xpath", "course_name_link_wfnen_100").click()
    base.wait_for_element_to_be_visibile(20, "xpath", "list_of_lesson")
    # assertion
    list = base.get_elements("xpath", "list_of_lesson")
    for lesson in list:
        print(lesson.text)

def test_LWF15(web_driver):
    '''
    this test case needs to logout.
    '''
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "course_name_link_wfnen_100")
    base.get_element("xpath", "course_name_link_wfnen_100").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_video_intro")
    base.get_element("xpath", "click_on_video_intro").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_video")
    base.get_element("xpath", "click_on_video").click()
    sleep(3)
    base.is_element_present("xpath", "click_on_teaching_mode_btn")
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_teaching_mode_btn")
    base.get_element("xpath", "click_on_teaching_mode_btn").click()
    sleep(2)
    assert base.is_element_present("xpath", "assert_full_screen")
    base.get_element("xpath", "full_screen").click()
    sleep(4)
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_toggle")
    base.get_element("xpath", "click_on_toggle").click()
    base.get_element("xpath", "click_on_logout").click()

def test_LWF16(web_driver):
    """
    this tc needs to login again.
    """
    base.get_url(url)
    base.get_element("xpath", "enter_username").send_keys(data_helper.get_user_data("user_data", "faculty_username"))
    base.get_element("xpath", "next_btn").click()
    base.get_element("xpath", "enter_password").send_keys(data_helper.get_user_data("user_data", "faculty_password"))
    base.get_element("xpath", "sign_in_btn").click()
    sleep(5)
    base.wait_for_element_to_be_clickable(25,"xpath", "course_name_link_wfnen_100")
    base.get_element("xpath", "course_name_link_wfnen_100").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_video_intro")
    base.get_element("xpath", "click_on_video_intro").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_video")
    base.get_element("xpath", "click_on_video").click()
    sleep(2)
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_preparation_mode_btn")
    base.get_element("xpath", "click_on_preparation_mode_btn").click()
    sleep(2)
    assert base.get_element("xpath", "assert_normal_screen")

def test_LWF17(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25,"xpath", "course_name_link_wfnen_100")
    base.get_element("xpath", "course_name_link_wfnen_100").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_video_intro")
    base.get_element("xpath", "click_on_video_intro").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_video")
    base.get_element("xpath", "click_on_video").click()
    sleep(3)
    if (base.is_element_present("xpath", "click_on_teaching_mode_btn")):
        base.wait_for_element_to_be_clickable(25, "xpath", "click_on_teaching_mode_btn")
        base.get_element("xpath", "click_on_teaching_mode_btn").click()
        sleep(2)
        base.get_element("xpath", "full_screen").click()
    sleep(3)
    # Assertions
    web_driver.execute_script("jwplayer().pause()")
    sleep(2)
    web_driver.execute_script("jwplayer().play()")
    sleep(2)
    web_driver.execute_script("jwplayer().seek(120)")

def test_LWF18(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "course_name_link_wfnen_100")
    base.get_element("xpath", "course_name_link_wfnen_100").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_video_intro")
    base.get_element("xpath", "click_on_video_intro").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_video")
    base.get_element("xpath", "click_on_video").click()
    sleep(3)
    if (base.is_element_present("xpath", "click_on_teaching_mode_btn")):
        base.wait_for_element_to_be_clickable(25, "xpath", "click_on_teaching_mode_btn")
        base.get_element("xpath", "click_on_teaching_mode_btn").click()
        sleep(2)
        base.get_element("xpath", "full_screen").click()
    sleep(3)
    base.get_element("xpath", "click_on_next_button").click()
    sleep(2)
    assert base.is_element_present("xpath", "click_on_video")

def test_LWF19(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "course_name_link_wfnen_100")
    base.get_element("xpath", "course_name_link_wfnen_100").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_course_info")
    base.get_element("xpath", "click_on_course_info").click()
    # assertion
    base.wait_for_element_to_be_clickable(25, "xpath", "list_course_info")
    course_info_list = base.get_elements("xpath", "list_course_info")
    for courses in course_info_list:
        print(courses.text)

# def test_LWF20(web_driver):
#     base.get_url(url)
#     sleep(5)
#     base.wait_for_element_to_be_clickable(25, "xpath", "course_name_link_wfnen_100")
#     base.get_element("xpath", "course_name_link_wfnen_100").click()
#     base.wait_for_element_to_be_clickable(25, "xpath", "click_on_quizes")
#     base.get_element("xpath", "click_on_quizes").click()
#     sleep(2)
#     assert data_helper.get_user_data("user_data", "assert_take_quiz") in base.get_element("xpath","click_on_take_quize").text
#
# def test_LWF21(web_driver):
#     base.get_url(url)
#     sleep(5)
#     base.wait_for_element_to_be_clickable(25, "xpath", "course_name_link_wfnen_100")
#     base.get_element("xpath", "course_name_link_wfnen_100").click()
#     base.wait_for_element_to_be_clickable(25, "xpath", "click_on_quizes")
#     base.get_element("xpath", "click_on_quizes").click()
#     base.wait_for_element_to_be_clickable(25, "xpath", "click_on_take_quize")
#     base.get_element("xpath", "click_on_take_quize").click()
#     assert base.is_element_present("xpath", "submit_ques")
#
# def test_LWF22(web_driver):
#     base.get_url(url)
#     sleep(5)
#     base.wait_for_element_to_be_clickable(25, "xpath", "course_name_link_wfnen_100")
#     base.get_element("xpath", "course_name_link_wfnen_100").click()
#     base.wait_for_element_to_be_clickable(25, "xpath", "click_on_quizes")
#     base.get_element("xpath", "click_on_quizes").click()
#     base.wait_for_element_to_be_clickable(25, "xpath", "click_on_take_quize")
#     base.get_element("xpath", "click_on_take_quize").click()
#     sleep(5)
#     greenTickDisplayed = True
#     while greenTickDisplayed:
#         try:
#             greenTickDisplayed = base.get_element("xpath", "submit_ques").is_displayed()
#             base.get_element("xpath", "submit_ques").click()
#             sleep(3)
#         except Exception:
#             greenTickDisplayed = False
#     base.wait_for_element_to_be_clickable(5,"xpath", "yes_qiuz_btn")
#     base.get_element("xpath", "yes_qiuz_btn").click()
#     assert data_helper.get_user_data("user_data", "assert_quiz_result") in base.get_element("xpath","assert_quiz_result").text
#
# def test_LWF23(web_driver):
#     base.get_url(url)
#     sleep(5)
#     base.wait_for_element_to_be_clickable(25, "xpath", "course_name_link_wfnen_100")
#     base.get_element("xpath", "course_name_link_wfnen_100").click()
#     base.wait_for_element_to_be_clickable(25, "xpath", "click_on_quizes")
#     base.get_element("xpath", "click_on_quizes").click()
#     base.wait_for_element_to_be_clickable(25, "xpath", "view_results")
#     base.get_element("xpath", "view_results").click()
#     sleep(2)
#     assert data_helper.get_user_data("user_data", "view_result_asssert") in base.get_element("xpath","view_results").text
#
# def test_LWF24(web_driver):
#     base.get_url(url)
#     sleep(5)
#     base.wait_for_element_to_be_clickable(25, "xpath", "course_name_link_wfnen_100")
#     base.get_element("xpath", "course_name_link_wfnen_100").click()
#     base.wait_for_element_to_be_clickable(25, "xpath", "click_on_quizes")
#     base.get_element("xpath", "click_on_quizes").click()
#     base.wait_for_element_to_be_clickable(25, "xpath", "view_results")
#     base.get_element("xpath", "view_results").click()
#     base.wait_for_element_to_be_visibile(25, "xpath", "assert_score")
#     assert data_helper.get_user_data("user_data", "assert_score") in base.get_element("xpath","assert_score").text
#     # Assertion
#     current_date = base.get_element("xpath", "view_current_date").text
#     print(current_date)
#
# def test_LWF25(web_driver):
#     base.get_url(url)
#     sleep(5)
#     base.wait_for_element_to_be_clickable(25, "xpath", "course_name_link_wfnen_100")
#     base.get_element("xpath", "course_name_link_wfnen_100").click()
#     base.wait_for_element_to_be_clickable(25, "xpath", "click_on_quizes")
#     base.get_element("xpath", "click_on_quizes").click()
#     base.wait_for_element_to_be_clickable(25, "xpath", "view_results")
#     base.get_element("xpath", "view_results").click()
#     base.wait_for_element_to_be_clickable(25, "xpath", "view_results")
#     base.get_element("xpath", "view_results").click()
#     base.wait_for_element_to_be_clickable(25, "xpath", "view_solution_btn")
#     base.get_element("xpath", "view_solution_btn").click()
#     sleep(9)
#     base.wait_for_element_to_be_visibile(25, "xpath", "assert_feedback_video")
#     assert data_helper.get_user_data("user_data", "assert_feedback_video") in base.get_element("xpath","assert_feedback_video").text
#     base.wait_for_element_to_be_clickable(25, "xpath", "close_video")
#     base.get_element("xpath", "close_video").click()
#     sleep(2)
#
# def test_LWF26(web_driver):
#     base.get_url(url)
#     sleep(5)
#     base.wait_for_element_to_be_clickable(25, "xpath", "course_name_link_wfnen_100")
#     base.get_element("xpath", "course_name_link_wfnen_100").click()
#     sleep(2)
#     num = {1,2,3}
#     for i in num:
#         base.wait_for_element_to_be_clickable(25, "xpath", "click_on_quizes")
#         base.get_element("xpath", "click_on_quizes").click()
#         base.wait_for_element_to_be_clickable(25, "xpath", "take_quize_3_times_lesson_5")
#         base.get_element("xpath", "take_quize_3_times_lesson_5").click()
#         sleep(3)
#         greenTickDisplayed = True
#         while greenTickDisplayed:
#             try:
#                 greenTickDisplayed = base.get_element("xpath", "submit_ques").is_displayed()
#                 base.get_element("xpath", "submit_ques").click()
#                 sleep(3)
#             except Exception:
#                 greenTickDisplayed = False
#         base.wait_for_element_to_be_clickable(5, "xpath", "yes_qiuz_btn")
#         base.get_element("xpath", "yes_qiuz_btn").click()
#         sleep(1)
#         web_driver.back()
#     sleep(1)
#     web_driver.refresh()
#     sleep(2)
#     # assertion
#     status = base.is_element_present("xpath", "take_quize_3_times_lesson_5")  # it should return False
#     print(status)
#
# def test_LWF27(web_driver):
#     base.get_url(url)
#     sleep(5)
#     base.wait_for_element_to_be_clickable(25, "xpath", "course_name_link_wfnen_100")
#     base.get_element("xpath", "course_name_link_wfnen_100").click()
#     sleep(2)
#     base.wait_for_element_to_be_clickable(25, "xpath", "click_on_quizes")
#     base.get_element("xpath", "click_on_quizes").click()
#     sleep(2)
#     base.wait_for_element_to_be_clickable(25, "xpath", "view_results_lesson_5")
#     base.get_element("xpath", "view_results_lesson_5").click()
#     # assertion
#     elems = base.get_driver().find_elements_by_xpath("//*[text()='View Result']")
#     print("count of view_results :" + str(len(elems)))
#     for view_result in elems:
#         print(view_result.text)
#
# def test_LWF28(web_driver):
#     base.get_url(url)
#     sleep(5)
#     base.wait_for_element_to_be_clickable(25, "xpath", "course_name_link_wfnen_100")
#     base.get_element("xpath", "course_name_link_wfnen_100").click()
#     base.wait_for_element_to_be_clickable(25, "xpath", "click_on_quizes")
#     base.get_element("xpath", "click_on_quizes").click()
#     sleep(2)
#     take_quize_btn = True
#     while take_quize_btn:
#         try:
#             take_quize_btn = base.get_element("xpath", "click_on_take_quize_btn").is_displayed()
#             base.get_element("xpath", "click_on_take_quize_btn").click()
#             sleep(3)
#             submit_btn = True
#             while submit_btn:
#                 try:
#                     submit_btn = base.get_element("xpath", "submit_ques").is_displayed()
#                     base.get_element("xpath", "submit_ques").click()
#                     sleep(3)
#                 except Exception:
#                     submit_btn = False
#             base.wait_for_element_to_be_clickable(5, "xpath", "yes_qiuz_btn")
#             base.get_element("xpath", "yes_qiuz_btn").click()
#             web_driver.back()
#             sleep(1)
#             web_driver.refresh()
#             sleep(1)
#         except Exception:
#             take_quize_btn = False
#     sleep(2)
#     base.wait_for_element_to_be_clickable(25, "xpath", "click_on_dashboard")
#     base.get_element("xpath", "click_on_dashboard").click()
#     sleep(2)
#     assert base.is_element_present("xpath", "final_assesment_btn")
#     base.wait_for_element_to_be_clickable(25, "xpath", "final_assesment_btn")
#     base.get_element("xpath", "final_assesment_btn").click()
#     sleep(3)
#     submit_btn = True
#     while submit_btn:
#         try:
#             submit_btn = base.get_element("xpath", "submit_ques").is_displayed()
#             base.get_element("xpath", "submit_ques").click()
#             sleep(3)
#         except Exception:
#             submit_btn = False
#     base.wait_for_element_to_be_clickable(5, "xpath", "yes_qiuz_btn")
#     base.get_element("xpath", "yes_qiuz_btn").click()
#     sleep(2)
#     assert data_helper.get_user_data("user_data", "assert_your_score") in base.get_element("xpath", "assert_your_score").text
#     sleep(3)
#     base.wait_for_element_to_be_clickable(25, "xpath", "click_on_dashboard")
#     base.get_element("xpath", "click_on_dashboard").click()
#     sleep(2)
#     # assertion
#     status = base.is_element_present("xpath", "final_assesment_enable_btn")  # it should return False
#     print(status)

def test_LWF29(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_course_plan")
    base.get_element("xpath", "click_on_course_plan").click()
    assert data_helper.get_user_data("user_data", "assert_course_plan") in base.get_element("xpath", "assert_course_plan").text
    courses = base.get_elements("xpath", "course_plan_lessons")
    for lessons in courses:
        print(lessons.text)

def test_LWF30(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_course_plan")
    base.get_element("xpath", "click_on_course_plan").click()
    base.wait_for_element_to_be_visibile(25, "xpath", "assert_course_plan")
    assert data_helper.get_user_data("user_data", "assert_course_plan") in base.get_element("xpath", "assert_course_plan").text
    base.get_element("xpath", "Mark_as_complete").click()
    sleep(2)
    assert data_helper.get_user_data("user_data", "assert_yes_text") in base.get_element("xpath","click_on_yes_btn").text

def test_LWF31(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_course_plan")
    base.get_element("xpath", "click_on_course_plan").click()
    base.wait_for_element_to_be_visibile(25, "xpath", "assert_course_plan")
    assert data_helper.get_user_data("user_data", "assert_course_plan") in base.get_element("xpath", "assert_course_plan").text
    base.get_element("xpath", "select_date_for_lesson_1").click()
    sleep(2)
    # assertion
    assert base.is_element_present("xpath", "assert_current_date")
   # print(current_date)

def test_LWF32(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_course_plan")
    base.get_element("xpath", "click_on_course_plan").click()
    base.wait_for_element_to_be_visibile(25, "xpath", "assert_course_plan")
    assert data_helper.get_user_data("user_data", "assert_course_plan") in base.get_element("xpath", "assert_course_plan").text
    base.get_element("xpath", "Mark_as_complete").click()
    sleep(2)
    base.get_element("xpath", "click_on_yes_btn").click()
    base.get_element("xpath", "star_rating_mark_as_completed").click()
    base.get_element("xpath", "star_mark_submit_btn").click()
    sleep(9)
    # assertion
    feedback_rating = base.is_element_present("xpath", "feedback_submit_rating_lesson_5")  # it shoud return True
    print(feedback_rating)

def test_LWF33(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_course_header")
    base.get_element("xpath", "click_on_course_header").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "create_batch_in_100")
    base.get_element("xpath", "create_batch_in_100").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_create_new_batch")
    base.get_element("xpath", "click_on_create_new_batch").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "enter_batch_name")
    base.get_element("xpath", "enter_batch_name").send_keys(data_helper.get_user_data("user_data", "enter_batch_name"))
    base.get_element("xpath", "number_of_student").send_keys(data_helper.get_user_data("user_data", "enter_num_of_students"))
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_date_picker")
    base.get_element("xpath", "click_on_date_picker").click()
    sleep(2)
    base.get_element("xpath", "select_date").click()
    sleep(2)
    base.get_element("xpath", "create_batch").click()
    sleep(9)
    base.wait_for_element_to_be_clickable(25, "xpath", "batch_created_text")
    assert base.get_element("xpath", "batch_created_text").is_displayed()
    base.get_element("xpath", "click_on_dashboard").click()
    sleep(3)
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_start_lw_33")
    base.get_element("xpath", "click_on_start_lw_33").click()
    sleep(3)
    if (base.is_element_present("xpath", "click_on_teaching_mode_btn")):
        base.wait_for_element_to_be_clickable(25, "xpath", "click_on_teaching_mode_btn")
        base.get_element("xpath", "click_on_teaching_mode_btn").click()
        sleep(2)
        base.get_element("xpath", "full_screen").click()
    sleep(2)
    # assertion
    web_driver.execute_script("jwplayer().pause()")
    sleep(2)
    web_driver.execute_script("jwplayer().play()")
    sleep(2)

def test_LWF34(web_driver):
    base.get_url(url)
    sleep(5)
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
    sleep(5)
    # base.wait_for_element_to_be_clickable(25, "xpath", "click_on_lesson")
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


def test_LWF35(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_resume_btn")
    base.get_element("xpath", "click_on_resume_btn").click()
    sleep(2)
    if (base.is_element_present("xpath", "click_on_teaching_mode_btn")):
        base.wait_for_element_to_be_clickable(25, "xpath", "click_on_teaching_mode_btn")
        base.get_element("xpath", "click_on_teaching_mode_btn").click()
        sleep(2)
        base.get_element("xpath", "full_screen").click()
    sleep(2)
    assert base.is_element_present("xpath", "next_button_for_green_tick")

def test_LWF36(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_visibile(25, "xpath", "previous_cycle_text")
    prev_text = base.get_element("xpath", "previous_cycle_text").text
    print(prev_text)
    base.wait_for_element_to_be_clickable(25, "xpath", "course_name_link_wfnen_100")
    base.get_element("xpath", "course_name_link_wfnen_100").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_play_vdo_welcome")
    base.get_element("xpath", "click_on_play_vdo_welcome").click()
    sleep(3)
    if( base.is_element_present("xpath", "click_on_teaching_mode_btn")):
        base.wait_for_element_to_be_clickable(25, "xpath", "click_on_teaching_mode_btn")
        base.get_element("xpath", "click_on_teaching_mode_btn").click()
        sleep(2)
        base.get_element("xpath", "full_screen").click()
    sleep(3)
    web_driver.execute_script("jwplayer().seek(200)")
    sleep(1)
    web_driver.execute_script("jwplayer().seek(242)")
    sleep(9)
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_dashboard")
    base.get_element("xpath", "click_on_dashboard").click()
    web_driver.refresh()
    updated_text = prev_text = base.get_element("xpath", "previous_cycle_text").text
    print(updated_text)
    assert prev_text in updated_text

def test_LWF37(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_visibile(25, "xpath", "recent_activities")
    assert data_helper.get_user_data("user_data", "recent_activities_data") in base.get_element("xpath", "recent_activities").text
    activities = base.get_elements("xpath", "assert_recent_activities")
    for div in activities:
        print(div.text)

def test_LWF38(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_manage_batches")
    base.get_element("xpath", "click_on_manage_batches").click()
    base.wait_for_element_to_be_visibile(25, "xpath", "assert_manage_batches")
    # assertion
    elems = base.get_driver().find_elements_by_xpath("//*[@ng-repeat='batch in batches.activeBatches']")
    print("count of active_batches :" + str(len(elems)))

def test_LWF39(web_driver):
    base.get_url(url)
    base.get_element("xpath", "click_on_manage_batches").click()
    sleep(5)
    base.get_element("xpath", "click_on_manage_batches").click()
    base.get_element("xpath", "Edit_batch").click()
    base.wait_for_element_to_be_visibile(10, "xpath", "edit_manage_std_tab")
    base.get_element("xpath", "edit_manage_std_tab").click()
    base.wait_for_element_to_be_visibile(10, "xpath", "edit_manage_std_tf")
    edit = base.get_element("xpath", "edit_manage_std_tf")
    edit.clear()
    sleep(5)
    edit.send_keys(data_helper.get_user_data("user_data", "batch_name_copy"))
    base.wait_for_element_to_be_visibile(10, "xpath", "click_on_update")
    base.get_element("xpath", "click_on_update").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "batch_created_text")
    assert base.get_element("xpath", "batch_created_text").is_displayed()

def test_LWF40(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_visibile(25, "xpath", "click_on_manage_batches")
    base.get_element("xpath", "click_on_manage_batches").click()
    elem_1 = base.get_driver().find_elements_by_xpath("//*[@ng-repeat='batch in batches.activeBatches']")
    print("count of active_batches :" + str(len(elem_1)))
    count_1 = str(len(elem_1))
    base.get_element("xpath", "delete_batch_icon").click()
    sleep(2)
    base.get_element("xpath", "click_on_yes_btn").click()
    sleep(15)
    elem_2 = base.get_driver().find_elements_by_xpath("//*[@ng-repeat='batch in batches.activeBatches']")
    print("count of active_batches :" + str(len(elem_2)))
    count_2 = str(len(elem_2))
    assert count_1 not in count_2

def test_LWF41(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_visibile(25, "xpath", "click_on_manage_batches")
    base.get_element("xpath", "click_on_manage_batches").click()
    elem_1 = base.get_driver().find_elements_by_xpath("//*[@ng-repeat='batch in batches.activeBatches']")
    print("count of active_batches :" + str(len(elem_1)))
    count_1 = str(len(elem_1))
    base.wait_for_element_to_be_visibile(25, "xpath", "click_on_delete_batch_tab")
    base.get_element("xpath", "click_on_delete_batch_tab").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "cilck_on_restore_batch_btn")
    base.get_element("xpath", "cilck_on_restore_batch_btn").click()
    sleep(1)
    base.get_element("xpath", "click_on_yes_btn").click()
    sleep(15)
    elem_2 = base.get_driver().find_elements_by_xpath("//*[@ng-repeat='batch in batches.activeBatches']")
    print("count of active_batches :" + str(len(elem_2)))
    count_2 = str(len(elem_2))
    assert count_1 not in count_2

def test_LWF42(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_visibile(25, "xpath", "click_on_manage_batches")
    base.get_element("xpath", "click_on_manage_batches").click()
    base.wait_for_element_to_be_visibile(10, "xpath", "chat_message_icon")
    base.get_element("xpath", "chat_message_icon").click()
    base.get_element("xpath", "type_chat_message").send_keys(data_helper.get_user_data("user_data", "type_chat_message"))
    base.get_element("xpath", "send_chat_message").click()
    sleep(2)
    assert base.is_element_present("xpath", "assert_chat_message")

def test_LWF43(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_visibile(25, "xpath", "click_on_manage_batches")
    base.get_element("xpath", "click_on_manage_batches").click()
    base.wait_for_element_to_be_visibile(25, "xpath", "click_on_no_upcoming_module")
    base.get_element("xpath", "click_on_no_upcoming_module").click()
    assert data_helper.get_user_data("user_data", "assert_course_plan") in base.get_element("xpath","assert_course_plan").text

def test_LWF44(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_visibile(25, "xpath", "click_on_manage_batches")
    base.get_element("xpath", "click_on_manage_batches").click()
    base.wait_for_element_to_be_visibile(25, "xpath", "click_on_manage_students")
    base.get_element("xpath", "click_on_manage_students").click()
    base.get_element("xpath", "enter_student_name").send_keys(data_helper.get_user_data("user_data", "enter_student_name"))
    base.get_element("xpath", "click_on_green_tick").click()
    sleep(9)
    assert base.is_element_present("xpath", "assert_student_name")

def test_LWF45(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_visibile(25, "xpath", "click_on_manage_batches")
    base.get_element("xpath", "click_on_manage_batches").click()
    base.wait_for_element_to_be_visibile(25, "xpath", "click_on_manage_students")
    base.get_element("xpath", "click_on_manage_students").click()
    base.get_element("xpath", "enter_student_name").send_keys(data_helper.get_user_data("user_data", "enter_student_name"))
    base.get_element("xpath", "click_on_green_tick").click()
    sleep(9)
    assert base.is_element_present("xpath", "assert_student_name")
    base.wait_for_element_to_be_clickable(25, "xpath", "block_btn")
    base.get_element("xpath", "block_btn").click()
    sleep(1)
    base.get_element("xpath", "click_on_yes_btn").click()
    sleep(5)
    assert data_helper.get_user_data("user_data", "assert_unblock_btn") in base.get_element("xpath", "assert_unblock_btn").text

def test_LWF46(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_visibile(25, "xpath", "click_on_manage_batches")
    base.get_element("xpath", "click_on_manage_batches").click()
    base.wait_for_element_to_be_visibile(25, "xpath", "click_on_manage_students")
    base.get_element("xpath", "click_on_manage_students").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "assert_unblock_btn")
    base.get_element("xpath", "assert_unblock_btn").click()
    sleep(1)
    base.get_element("xpath", "click_on_yes_btn").click()
    sleep(5)
    assert data_helper.get_user_data("user_data", "assert_block_text") in base.get_element("xpath", "block_btn").text

def test_LWF47(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_visibile(25, "xpath", "click_on_manage_batches")
    base.get_element("xpath", "click_on_manage_batches").click()
    base.wait_for_element_to_be_visibile(25, "xpath", "click_on_manage_students")
    base.get_element("xpath", "click_on_manage_students").click()
    base.get_element("xpath", "enter_student_name").send_keys(data_helper.get_user_data("user_data", "enter_student_name"))
    base.get_element("xpath", "click_on_green_tick").click()
    sleep(9)
    assert base.is_element_present("xpath", "assert_student_name")
    elem_1 = base.get_driver().find_elements_by_xpath("//*[@class='student_card ng-scope']")
    print("count of students :" + str(len(elem_1)))
    count_1 = str(len(elem_1))
    base.get_element("xpath", "click_on_release_tab").click()
    sleep(1)
    base.get_element("xpath", "click_on_yes_btn").click()
    sleep(5)
    web_driver.refresh()
    elem_2 = base.get_driver().find_elements_by_xpath("//*[@class='student_card ng-scope']")
    print("count of students :" + str(len(elem_2)))
    count_2 = str(len(elem_2))
    assert count_1 not in count_2

def test_LWF48(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_visibile(25, "xpath", "click_on_manage_batches")
    base.get_element("xpath", "click_on_manage_batches").click()
    base.wait_for_element_to_be_visibile(25, "xpath", "click_on_manage_students")
    base.get_element("xpath", "click_on_manage_students").click()
    base.get_element("xpath", "enter_student_name").send_keys(data_helper.get_user_data("user_data", "enter_student_name"))
    base.get_element("xpath", "click_on_green_tick").click()
    sleep(5)
    base.get_element("xpath", "edit_link").click()
    base.get_element("xpath", "enter_edit_text").clear()
    base.get_element("xpath", "enter_edit_text").send_keys(data_helper.get_user_data("user_data", "manage_std_name_edit"))
    base.get_element("xpath", "click_on__edit_green_tick").click()
    sleep(5)
    assert base.is_element_present("xpath", "assert_edit_text")

def test_LWF49(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_visibile(25, "xpath", "click_on_manage_batches")
    base.get_element("xpath", "click_on_manage_batches").click()
    base.wait_for_element_to_be_visibile(25, "xpath", "click_on_manage_students")
    base.get_element("xpath", "click_on_manage_students").click()
    base.get_element("xpath", "delete_manage_students").click()
    sleep(1)
    base.get_element("xpath", "click_on_yes_btn").click()
    sleep(5)
    web_driver.refresh()
    # asssrtion
    elem_2 = base.get_driver().find_elements_by_xpath("//*[@class='Student_detail_text ng-binding']")
    print("observe num of students :" + str(len(elem_2)))

def test_LWF50(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_visibile(25, "xpath", "click_on_manage_batches")
    base.get_element("xpath", "click_on_manage_batches").click()
    base.get_element("xpath", "run_lesson_tab").click()
    sleep(2)
    # assertion
    list = base.get_elements("xpath", "list_of_lesson")
    for lesson in list:
        print(lesson.text)

def test_LWF51(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_visibile(25, "xpath", "click_on_manage_batches")
    base.get_element("xpath", "click_on_manage_batches").click()
    elem_1 = base.get_driver().find_elements_by_xpath("//*[@ng-repeat='batch in batches.activeBatches']")
    print("count of active_batches :" + str(len(elem_1)))
    count_1 = str(len(elem_1))
    sleep(2)
    base.wait_for_element_to_be_visibile(25, "xpath", "click_on_close_batch_tab")
    base.get_element("xpath", "click_on_close_batch_tab").click()
    sleep(2)
    base.get_element("xpath", "click_on_yes_btn").click()
    base.get_element("xpath", "rating_for_closed_batches").click()
    base.get_element("xpath", "star_mark_submit_btn").click()
    sleep(15)
    elem_2 = base.get_driver().find_elements_by_xpath("//*[@ng-repeat='batch in batches.activeBatches']")
    print("count of active_batches :" + str(len(elem_2)))
    count_2 = str(len(elem_2))
    assert count_1 not in count_2

def test_LWF52(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_visibile(25, "xpath", "click_on_manage_batches")
    base.get_element("xpath", "click_on_manage_batches").click()
    elem_1 = base.get_driver().find_elements_by_xpath("//*[@ng-repeat='batch in batches.activeBatches']")
    print("count of active_batches :" + str(len(elem_1)))
    count_1 = str(len(elem_1))
    base.wait_for_element_to_be_visibile(25, "xpath", "reopen_the_batches")
    base.get_element("xpath", "reopen_the_batches").click()
    sleep(1)
    base.get_element("xpath", "click_on_yes_btn").click()
    sleep(15)
    elem_2 = base.get_driver().find_elements_by_xpath("//*[@ng-repeat='batch in batches.activeBatches']")
    print("count of active_batches :" + str(len(elem_2)))
    count_2 = str(len(elem_2))
    assert count_1 not in count_2

def test_LWF53(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "ecell_button")
    base.get_element("xpath", "ecell_button").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_activity")
    base.get_element("xpath", "click_on_activity").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "assert_activity")
    base.get_element("xpath", "assert_activity").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_add_btn")
    base.get_element("xpath", "click_on_add_btn").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "schedule_event_btn")
    base.get_element("xpath", "schedule_event_btn").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_date_picker")
    base.get_element("xpath", "click_on_date_picker").click()
    # sleep(5)
    # base.wait_for_element_to_be_clickable(30, "xpath", "select_date")
    # base.get_element("xpath", "select_date").click()
    # base.get_element("xpath", "time_activities").click()
    # base.wait_for_element_to_be_clickable(20,"xpath","select_time_schedule")
    # base.get_element("xpath", "select_time_schedule").click()
    sleep(2)
    # base.get_driver().find_element_by_xpath("//*[@class='md-datepicker-triangle-button md-icon-button md-button']").click()
    base.wait_for_element_to_be_clickable(30, "xpath", "select_date")
    base.get_element("xpath", "select_date").click()
    sleep(1)
    base.get_element("xpath", "time_activities").click()
    base.get_driver().find_element_by_xpath("(//*[@class='ui-timepicker-pm'])[19]").click()
    base.get_element("xpath", "enter_days").send_keys(data_helper.get_user_data("user_data", "enter_days"))
    sleep(2)
    base.get_element("xpath", "enter_seats").send_keys(data_helper.get_user_data("user_data", "enter_seats"))
    sleep(2)
    base.get_element("xpath", "enter_vanue").send_keys(data_helper.get_user_data("user_data", "enter_vanue_text"))
    sleep(2)
    base.get_element("xpath", "done_btn").click()
    sleep(1)
    assert data_helper.get_user_data("user_data", "assert_done_creativities") in base.get_element("xpath", "assert_done_activities").text

# def test_LWF54(web_driver):
#     base.get_url(url)
#     sleep(5)
#     base.wait_for_element_to_be_clickable(25, "xpath", "ecell_button")
#     base.get_element("xpath", "ecell_button").click()
#     sleep(1)
#     base.get_element("xpath", "click_to_edit_photos").click()
#     sleep(1)
#     os.system("C:\\Users\\User\\Desktop\\auto2.exe")
#     sleep(1)
#     base.get_element("xpath", "click_on_done_btn").click()
#     sleep(1)
#     assert data_helper.get_user_data("user_data", "assert_cover_pic") in base.get_element("xpath", "assert_cover_pic").text

def test_LWF55(web_driver):
    base.get_url(url)
    base.wait_for_element_to_be_clickable(25, "xpath", "ecell_button")
    base.get_element("xpath", "ecell_button").click()
    sleep(3)
    base.get_element("xpath", "edit_ecell_info").click()
    sleep(1)
    base.get_element("xpath", "enter_edit_name").clear()
    sleep(1)
    base.get_element("xpath", "enter_edit_name").send_keys(data_helper.get_user_data("user_data", "enter_edit_name_text"))
    base.get_element("xpath", "click_on_save").click()
    sleep(9)
    assert base.is_element_present("xpath", "assert_name_text")

def test_LWF56(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "ecell_button")
    base.get_element("xpath", "ecell_button").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_activity")
    base.get_element("xpath", "click_on_activity").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "assert_activity")
    base.get_element("xpath", "assert_activity").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_add_btn")
    base.get_element("xpath", "click_on_add_btn").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "schedule_event_btn")
    base.get_element("xpath", "schedule_event_btn").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_date_picker")
    base.get_element("xpath", "click_on_date_picker").click()
    sleep(1)
    # sleep(5)
    # base.get_driver().find_element_by_xpath("//*[@class='md-datepicker-triangle-button md-icon-button md-button']").click()
    sleep(2)
    base.get_element("xpath", "date_for_future").click()
    sleep(1)
    base.get_element("xpath", "time_activities").click()
    base.get_element("xpath", "select_time_schedule").click()
    sleep(2)
    base.get_element("xpath", "enter_days").send_keys(data_helper.get_user_data("user_data", "enter_days"))
    sleep(2)
    base.get_element("xpath", "enter_seats").send_keys(data_helper.get_user_data("user_data", "enter_seats"))
    sleep(2)
    base.get_element("xpath", "enter_vanue").send_keys(data_helper.get_user_data("user_data", "enter_vanue_text"))
    sleep(2)
    base.get_element("xpath", "done_btn").click()
    sleep(1)
    assert data_helper.get_user_data("user_data", "assert_done_creativities") in base.get_element("xpath","assert_done_activities").text

def test_LWF57(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "ecell_button")
    base.get_element("xpath", "ecell_button").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_activity")
    base.get_element("xpath", "click_on_activity").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "assert_activity")
    base.get_element("xpath", "assert_activity").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_add_btn")
    base.get_element("xpath", "click_on_add_btn").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "schedule_event_btn")
    base.get_element("xpath", "schedule_event_btn").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_date_picker")
    base.get_element("xpath", "click_on_date_picker").click()
    sleep(1)
    base.get_element("xpath", "select_date").click()
    sleep(1)
    base.get_element("xpath", "time_activities").click()
    base.get_element("xpath", "select_time_schedule").click()
    sleep(2)
    base.get_element("xpath", "enter_days").send_keys(data_helper.get_user_data("user_data", "enter_days"))
    sleep(2)
    base.get_element("xpath", "enter_seats").send_keys(data_helper.get_user_data("user_data", "enter_seats"))
    sleep(2)
    base.get_element("xpath", "enter_vanue").send_keys(data_helper.get_user_data("user_data", "enter_vanue_text"))
    sleep(2)
    base.get_element("xpath", "done_btn").click()
    sleep(1)
    assert data_helper.get_user_data("user_data", "assert_done_creativities") in base.get_element("xpath","assert_done_activities").text
    base.get_element("xpath", "click_on_ongoing_activities").click()

def test_LWF58(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "ecell_button")
    base.get_element("xpath", "ecell_button").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_activity")
    base.get_element("xpath", "click_on_activity").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "assert_activity")
    base.get_element("xpath", "assert_activity").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_add_btn")
    base.get_element("xpath", "click_on_add_btn").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "schedule_event_btn")
    base.get_element("xpath", "schedule_event_btn").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_date_picker")
    base.get_element("xpath", "click_on_date_picker").click()
    sleep(2)
    base.get_element("xpath", "date_for_past").click()
    sleep(1)
    base.get_element("xpath", "time_activities").click()
    base.get_element("xpath", "select_time_schedule").click()
    sleep(2)
    base.get_element("xpath", "enter_days").send_keys(data_helper.get_user_data("user_data", "enter_days"))
    sleep(2)
    base.get_element("xpath", "enter_seats").send_keys(data_helper.get_user_data("user_data", "enter_seats"))
    sleep(2)
    base.get_element("xpath", "enter_vanue").send_keys(data_helper.get_user_data("user_data", "enter_vanue_text"))
    sleep(2)
    base.get_element("xpath", "done_btn").click()
    sleep(1)
    assert data_helper.get_user_data("user_data", "assert_done_creativities") in base.get_element("xpath","assert_done_activities").text
    base.get_element("xpath", "completed_activities").click()

def test_LWF59(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "ecell_button")
    base.get_element("xpath", "ecell_button").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_activity")
    base.get_element("xpath", "click_on_activity").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "assert_activity")
    base.get_element("xpath", "assert_activity").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_add_btn")
    base.get_element("xpath", "click_on_add_btn").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "schedule_event_btn")
    base.get_element("xpath", "schedule_event_btn").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_date_picker")
    base.get_element("xpath", "click_on_date_picker").click()
    sleep(1)
    base.get_element("xpath", "select_date").click()
    sleep(1)
    base.get_element("xpath", "time_activities").click()
    base.get_element("xpath", "select_time_schedule").click()
    sleep(1)
    base.get_element("xpath", "enter_days").send_keys(data_helper.get_user_data("user_data", "enter_days"))
    sleep(1)
    base.get_element("xpath", "enter_seats").send_keys(data_helper.get_user_data("user_data", "enter_seats"))
    sleep(1)
    base.get_element("xpath", "enter_vanue").send_keys(data_helper.get_user_data("user_data", "enter_vanue_text"))
    sleep(1)
    base.get_element("xpath", "save_ad_draft").click()
    sleep(1)
    base.get_element("xpath", "done_btn").click()
    sleep(1)
    assert data_helper.get_user_data("user_data", "assert_activities_draft") in base.get_element("xpath","assert_activities_draft").text

def test_LWF60(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "ecell_button")
    base.get_element("xpath", "ecell_button").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_activity")
    base.get_element("xpath", "click_on_activity").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "assert_activity")
    base.get_element("xpath", "assert_activity").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_draft")
    base.get_element("xpath", "click_on_draft").click()
    # assertion
    elem_1 = base.get_driver().find_elements_by_xpath("//*[@ng-repeat='activity in draftsActivities']")
    print("count of draft_activities :" + str(len(elem_1)))

def test_LWF61(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "ecell_button")
    base.get_element("xpath", "ecell_button").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_activity")
    base.get_element("xpath", "click_on_activity").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "assert_activity")
    base.get_element("xpath", "assert_activity").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_add_btn")
    base.get_element("xpath", "click_on_add_btn").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "schedule_event_btn")
    base.get_element("xpath", "schedule_event_btn").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_date_picker")
    base.get_element("xpath", "click_on_date_picker").click()
    sleep(1)
    base.get_element("xpath", "select_date").click()
    sleep(1)
    base.get_element("xpath", "time_activities").click()
    base.get_element("xpath", "select_time_schedule").click()
    sleep(1)
    base.get_element("xpath", "enter_days").send_keys(data_helper.get_user_data("user_data", "enter_days"))
    sleep(1)
    base.get_element("xpath", "enter_seats").send_keys(data_helper.get_user_data("user_data", "enter_seats"))
    sleep(1)
    base.get_element("xpath", "enter_vanue").send_keys(data_helper.get_user_data("user_data", "enter_vanue_text"))
    sleep(1)
    base.get_element("xpath", "assert_invite_only").click()
    sleep(1)
    base.get_element("xpath", "done_btn").click()
    sleep(1)
    assert data_helper.get_user_data("user_data", "assert_invite_only_text") in base.get_element("xpath","assert_invite_only_text").text

def test_LWF62(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_visibile(25, "xpath", "ecell_button")
    base.get_element("xpath", "ecell_button").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_team")
    base.get_element("xpath", "click_on_team").click()
    sleep(2)
    # assertion
    team_members = base.get_elements("xpath", "team_members")
    for list in team_members:
        print(list.text)

def test_LWF63(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_visibile(25, "xpath", "ecell_button")
    base.get_element("xpath", "ecell_button").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_practicum")
    base.get_element("xpath", "click_on_practicum").click()
    sleep(2)
    # assertion
    practicum = base.get_elements("xpath", "practicum_contents")
    for list in practicum:
        print(list.text)

def test_LWF64(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_visibile(25, "xpath", "ecell_button")
    base.get_element("xpath", "ecell_button").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_practicum")
    base.get_element("xpath", "click_on_practicum").click()
    sleep(2)
    base.get_element("xpath", "practicum_advanced").click()
    base.get_element("xpath", "click_advanced_file").click()
    text = base.get_element("xpath", "veiw_pdf_file").text
    assert data_helper.get_user_data("user_data", "pdf_view_option") in text

def test_LWF65(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_visibile(25, "xpath", "ecell_button")
    base.get_element("xpath", "ecell_button").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_practicum")
    base.get_element("xpath", "click_on_practicum").click()
    sleep(2)
    base.get_element("xpath", "click_on_practicum_basic").click()
    base.wait_for_element_to_be_visibile(10, "xpath", "search_pdf_file")
    search = base.get_element("xpath", "search_pdf_file")
    search.send_keys(data_helper.get_user_data("user_data", "pdf_file_name"))
    base.get_element("xpath", "click_on_search_icon").click()
    sleep(1)
    assert data_helper.get_user_data("user_data", "pdf_file_name") in base.get_element("xpath", "assert_pdf_name").text
    try:
        list = base.get_elements("xpath", "search_pdf_details")
        for pdf_details in list:
            print(pdf_details.text)
    except NoSuchElementException:
        print("BATCH NOT FOUND")

def test_LWF66(web_driver):
    base.get_url(url)
    sleep(3)
    window_before = web_driver.window_handles[0]
    base.get_element("xpath", "user_guide_tab").click()
    window_after = web_driver.window_handles[1]
    web_driver.switch_to_window(window_after)
    assert data_helper.get_user_data("user_data", "assert_learnwise_platform") in base.get_element("xpath", "assert_learnwise_platform").text
    web_driver.switch_to_window(window_before)

def test_LWF67(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_visibile(20, "xpath", "assert_feedback_video")
    base.get_element("xpath", "assert_feedback_video").click()
    base.wait_for_element_to_be_visibile(10, "xpath", "feedback_supports")
    assert base.is_element_present("xpath", "feedback_supports")

def test_LWF68(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_visibile(20, "xpath", "assert_feedback_video")
    base.get_element("xpath", "assert_feedback_video").click()
    sleep(1)
    assert base.is_element_present("xpath", "feedback_and_supports")

def test_LWF69(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_toggle")
    base.get_element("xpath", "click_on_toggle").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "profile_icon")
    base.get_element("xpath", "profile_icon").click()
    base.wait_for_element_to_be_visibile(10, "xpath", "edit_profile_account")
    base.get_element("xpath", "edit_profile_account").click()
    sleep(1)
    base.get_element("xpath", "edit_first_name").clear()
    sleep(1)
    base.get_element("xpath", "edit_first_name").send_keys(data_helper.get_user_data("user_data", "edit_first_name"))
    sleep(1)
    base.get_element("xpath", "edit_last_name").clear()
    sleep(1)
    base.get_element("xpath", "edit_last_name").send_keys(data_helper.get_user_data("user_data", "edit_last_name"))
    sleep(1)
    base.wait_for_element_to_be_visibile(10, "xpath", "save_changes")
    base.get_element("xpath", "save_changes").click()
    sleep(1)
    assert data_helper.get_user_data("user_data", "profile_updated") in base.get_element("xpath","profile_updated").text

def test_LWF70(web_driver):
    base.get_url(url)
    sleep(5)
    base.get_element("xpath", "click_on_toggle").click()
    base.get_element("xpath", "click_on_logout").click()
    sleep(2)
    assert data_helper.get_user_data("user_data", "assert_logout_text") in base.get_element("xpath", "assert_logout_button").text
