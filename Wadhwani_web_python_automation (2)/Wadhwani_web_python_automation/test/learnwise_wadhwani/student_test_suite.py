from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from Wadhwani_web_python_automation.main.tools import  selenium_base as base
from Wadhwani_web_python_automation.main.tools import json_helper as data_helper
from time import sleep
import os
url = data_helper.get_user_data("user_data", "url")

def test_LWS01(web_driver):
    base.get_url(url)
    base.get_element("xpath", "enter_username").send_keys(data_helper.get_user_data("user_data", "invalid_email_id"))
    # assertion
    check = base.get_element("xpath", "assert_disabled_next")
    print(check.is_enabled())

def test_LWS02(web_driver):
    base.get_url(url)
    base.get_element("xpath", "enter_username").send_keys(data_helper.get_user_data("user_data", "email_for_unregistered"))
    base.get_element("xpath", "next_btn").click()
    assert data_helper.get_user_data("user_data", "student_reg") in base.get_element("xpath","student_registration").text

def test_LWS03(web_driver):
    base.get_url(url)
    base.get_element("xpath", "enter_username").send_keys(data_helper.get_user_data("user_data", "valid_email_id"))
    base.get_element("xpath", "next_btn").click()
    base.get_element("xpath", "enter_password").send_keys(data_helper.get_user_data("user_data", "incorrect_password"))
    base.get_element("xpath", "sign_in_btn").click()
    assert data_helper.get_user_data("user_data", "error_message") in base.get_element("xpath","error_message").text

def test_LWS04(web_driver):
    base.get_url(url)
    base.get_element("xpath", "enter_username").send_keys(data_helper.get_user_data("user_data", "student_username"))
    base.get_element("xpath", "next_btn").click()
    base.get_element("xpath", "enter_password").send_keys(data_helper.get_user_data("user_data", "student_password"))
    base.get_element("xpath", "sign_in_btn").click()
    sleep(5)
    # assertion
    elem_1 = base.get_element("xpath", "list_of_available_batches")
    print(elem_1.text)

def test_LWS05(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "student_dashboard_header")
    base.get_element("xpath", "student_dashboard_header").click()
    sleep(2)
    assert data_helper.get_user_data("user_data", "assert_student_dashboard") in base.get_element("xpath","assert_student_dashboard").text

def test_LWS06(web_driver):
    base.get_url(url)
    sleep(5)
    base.get_element("xpath", "student_course_header").click()
    text_1 = base.get_element("xpath", "assert_enrolled_course").text
    base.get_element("xpath", "join_batch_btn").click()
    sleep(3)
    base.get_element("xpath", "click_on_yes_btn").click()
    sleep(11)
    text_2 = base.get_element("xpath", "assert_enrolled_course").text
    assert text_1 not in text_2

def test_LWS07(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "student_dashboard_header")
    base.get_element("xpath", "student_dashboard_header").click()
    sleep(2)
    list_batches = base.get_elements("xpath", "dashboard_batches")
    for batches_name in list_batches:
        print(batches_name.text)

def test_LWS08(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "student_dashboard_header")
    base.get_element("xpath", "student_dashboard_header").click()
    sleep(2)
    base.get_element("xpath", "click_on_start_btn").click()
    assert base.is_element_present("xpath", "next_button_for_green_tick")

def test_LWS09(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "student_dashboard_header")
    base.get_element("xpath", "student_dashboard_header").click()
    sleep(2)
    base.get_element("xpath", "click_on_resume_btn").click()
    assert base.is_element_present("xpath", "next_button_for_green_tick")

def test_LWS10(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "student_dashboard_header")
    base.get_element("xpath", "student_dashboard_header").click()
    base.wait_for_element_to_be_visibile(25, "xpath", "recent_activities")
    assert data_helper.get_user_data("user_data", "recent_activities_data") in base.get_element("xpath","recent_activities").text
    activities = base.get_elements("xpath", "assert_recent_activities")
    for div in activities:
        print(div.text)

def test_LWS11(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_resume_btn")
    base.get_element("xpath", "click_on_resume_btn").click()
    sleep(4)
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
    base.wait_for_element_to_be_clickable(25, "xpath", "student_dashboard_header")
    base.get_element("xpath", "student_dashboard_header").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_resume_btn")
    base.get_element("xpath", "click_on_resume_btn").click()
    base.wait_for_element_to_be_visibile(25, "xpath", "next_button_for_green_tick")
    base.get_element("xpath", "next_button_for_green_tick").click()
    sleep(2)
    web_driver.refresh()
    sleep(1)
    # Assertion
    assert base.is_element_present("xpath", "assert_green_tick")  # it should return True

def test_LWS12(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_visibile(25, "xpath", "previous_cycle_text")
    prev_text = base.get_element("xpath", "previous_cycle_text").text
    base.wait_for_element_to_be_clickable(25, "xpath", "course_name_link_wfnen_100")
    base.get_element("xpath", "course_name_link_wfnen_100").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_play_vdo_welcome")
    base.get_element("xpath", "click_on_play_vdo_welcome").click()
    sleep(3)
    if (base.is_element_present("xpath", "click_on_teaching_mode_btn")):
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
    sleep(1)
    web_driver.refresh()
    updated_text = prev_text = base.get_element("xpath", "previous_cycle_text").text
    assert prev_text in updated_text

def test_LWS13(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "student_dashboard_header")
    base.get_element("xpath", "student_dashboard_header").click()
    # assertion
    assert base.is_element_present("xpath", "final_assesment_disable_btn")  # it should return False

def test_LWS14(web_driver):
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

def test_LWS15(web_driver):
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

def test_LWS16(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25,"xpath", "course_name_link_wfnen_100")
    base.get_element("xpath", "course_name_link_wfnen_100").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_video_intro")
    base.get_element("xpath", "click_on_video_intro").click()
    prev_vdo_text = base.get_element("xpath", "prev_vdo_text").text
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_video")
    base.get_element("xpath", "click_on_video").click()
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "next_button_for_green_tick")
    base.get_element("xpath", "next_button_for_green_tick").click()
    sleep(2)
    next_vdo_text = base.get_element("xpath", "next_vdo_text").text
    assert prev_vdo_text not in next_vdo_text

def test_LWS17(web_driver):
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

def test_LWS18(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "course_name_link_wfnen_100")
    base.get_element("xpath", "course_name_link_wfnen_100").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_quizes")
    base.get_element("xpath", "click_on_quizes").click()
    sleep(2)
    assert data_helper.get_user_data("user_data", "assert_take_quiz") in base.get_element("xpath","click_on_take_quize").text

def test_LWS19(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "course_name_link_wfnen_100")
    base.get_element("xpath", "course_name_link_wfnen_100").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_quizes")
    base.get_element("xpath", "click_on_quizes").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_take_quize")
    base.get_element("xpath", "click_on_take_quize").click()
    assert base.is_element_present("xpath", "submit_ques")

def test_LWS20(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "course_name_link_wfnen_100")
    base.get_element("xpath", "course_name_link_wfnen_100").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_quizes")
    base.get_element("xpath", "click_on_quizes").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_take_quize")
    base.get_element("xpath", "click_on_take_quize").click()
    sleep(5)
    greenTickDisplayed = True
    while greenTickDisplayed:
        try:
            greenTickDisplayed = base.get_element("xpath", "submit_ques").is_displayed()
            base.get_element("xpath", "submit_ques").click()
            sleep(3)
        except Exception:
            greenTickDisplayed = False
    base.wait_for_element_to_be_clickable(5,"xpath", "yes_qiuz_btn")
    base.get_element("xpath", "yes_qiuz_btn").click()
    assert data_helper.get_user_data("user_data", "assert_quiz_result") in base.get_element("xpath","assert_quiz_result").text

def test_LWS21(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "course_name_link_wfnen_100")
    base.get_element("xpath", "course_name_link_wfnen_100").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_quizes")
    base.get_element("xpath", "click_on_quizes").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "view_results")
    base.get_element("xpath", "view_results").click()
    sleep(2)
    assert data_helper.get_user_data("user_data", "view_result_asssert") in base.get_element("xpath","view_results").text

def test_LWS22(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "course_name_link_wfnen_100")
    base.get_element("xpath", "course_name_link_wfnen_100").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_quizes")
    base.get_element("xpath", "click_on_quizes").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "view_results")
    base.get_element("xpath", "view_results").click()
    base.wait_for_element_to_be_visibile(25, "xpath", "assert_score")
    assert data_helper.get_user_data("user_data", "assert_score") in base.get_element("xpath","assert_score").text
    # Assertion
    current_date = base.get_element("xpath", "view_current_date").text
    print(current_date)

def test_LWS23(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "course_name_link_wfnen_100")
    base.get_element("xpath", "course_name_link_wfnen_100").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_quizes")
    base.get_element("xpath", "click_on_quizes").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "view_results")
    base.get_element("xpath", "view_results").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "view_results")
    base.get_element("xpath", "view_results").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "view_solution_btn")
    base.get_element("xpath", "view_solution_btn").click()
    sleep(9)
    base.wait_for_element_to_be_visibile(25, "xpath", "assert_feedback_video")
    assert data_helper.get_user_data("user_data", "assert_feedback_video") in base.get_element("xpath","assert_feedback_video").text
    base.wait_for_element_to_be_clickable(25, "xpath", "close_video")
    base.get_element("xpath", "close_video").click()

def test_LWS24(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "course_name_link_wfnen_100")
    base.get_element("xpath", "course_name_link_wfnen_100").click()
    sleep(2)
    num = {1,2,3}
    for i in num:
        base.wait_for_element_to_be_clickable(25, "xpath", "click_on_quizes")
        base.get_element("xpath", "click_on_quizes").click()
        base.wait_for_element_to_be_clickable(25, "xpath", "take_quize_3_times_lesson_5")
        base.get_element("xpath", "take_quize_3_times_lesson_5").click()
        sleep(3)
        greenTickDisplayed = True
        while greenTickDisplayed:
            try:
                greenTickDisplayed = base.get_element("xpath", "submit_ques").is_displayed()
                base.get_element("xpath", "submit_ques").click()
                sleep(3)
            except Exception:
                greenTickDisplayed = False
        base.wait_for_element_to_be_clickable(5, "xpath", "yes_qiuz_btn")
        base.get_element("xpath", "yes_qiuz_btn").click()
        sleep(1)
        web_driver.back()
    sleep(1)
    web_driver.refresh()
    sleep(2)
    # assertion
    status = base.is_element_present("xpath", "take_quize_3_times_lesson_5")  # it should return False
    print(status)

def test_LWS25(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "course_name_link_wfnen_100")
    base.get_element("xpath", "course_name_link_wfnen_100").click()
    sleep(2)
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_quizes")
    base.get_element("xpath", "click_on_quizes").click()
    sleep(2)
    base.wait_for_element_to_be_clickable(25, "xpath", "view_results_lesson_5")
    base.get_element("xpath", "view_results_lesson_5").click()
    # assertion
    elems = base.get_driver().find_elements_by_xpath("//*[text()='View Result']")
    print("count of view_results :" + str(len(elems)))
    for view_result in elems:
        print(view_result.text)

def test_LWS26(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "course_name_link_wfnen_100")
    base.get_element("xpath", "course_name_link_wfnen_100").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_quizes")
    base.get_element("xpath", "click_on_quizes").click()
    sleep(2)
    take_quize_btn = True
    while take_quize_btn:
        try:
            take_quize_btn = base.get_element("xpath", "click_on_take_quize_btn").is_displayed()
            base.get_element("xpath", "click_on_take_quize_btn").click()
            sleep(3)
            submit_btn = True
            while submit_btn:
                try:
                    submit_btn = base.get_element("xpath", "submit_ques").is_displayed()
                    base.get_element("xpath", "submit_ques").click()
                    sleep(3)
                except Exception:
                    submit_btn = False
            base.wait_for_element_to_be_clickable(5, "xpath", "yes_qiuz_btn")
            base.get_element("xpath", "yes_qiuz_btn").click()
            web_driver.back()
            sleep(1)
            web_driver.refresh()
            sleep(1)
        except Exception:
            take_quize_btn = False
    sleep(2)
    base.wait_for_element_to_be_clickable(25, "xpath", "student_dashboard_header")
    base.get_element("xpath", "student_dashboard_header").click()
    sleep(2)
    assert base.is_element_present("xpath", "final_assesment_btn")
    base.wait_for_element_to_be_clickable(25, "xpath", "final_assesment_btn")
    base.get_element("xpath", "final_assesment_btn").click()
    sleep(3)
    submit_btn = True
    while submit_btn:
        try:
            submit_btn = base.get_element("xpath", "submit_ques").is_displayed()
            base.get_element("xpath", "submit_ques").click()
            sleep(3)
        except Exception:
            submit_btn = False
    base.wait_for_element_to_be_clickable(5, "xpath", "yes_qiuz_btn")
    base.get_element("xpath", "yes_qiuz_btn").click()
    sleep(2)
    assert data_helper.get_user_data("user_data", "assert_your_score") in base.get_element("xpath", "assert_your_score").text
    sleep(3)
    base.wait_for_element_to_be_clickable(25, "xpath", "student_dashboard_header")
    base.get_element("xpath", "student_dashboard_header").click()
    sleep(2)
    # assertion
    status = base.is_element_present("xpath", "final_assesment_enable_btn")  # it should return False
    print(status)

def test_LWS27(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "ecell_button")
    base.get_element("xpath", "ecell_button").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_activity")
    base.get_element("xpath", "click_on_activity").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "assert_activity")
    base.get_element("xpath", "assert_activity").click()
    sleep(1)
    assert base.is_element_present("xpath", "click_on_add_btn")
    elem_2 = base.get_driver().find_elements_by_xpath("//*[@ng-click='activityDetail(activity)']")
    print("count of activities :" + str(len(elem_2)))

def test_LWS28(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "ecell_button")
    base.get_element("xpath", "ecell_button").click()
    sleep(1)
    base.get_element("xpath", "click_to_edit_photos").click()
    sleep(2)
    os.system('C:\\Users\\User\\Desktop\\auto2.exe')
    sleep(2)
    base.get_element("xpath", "click_on_done_btn").click()
    sleep(1)
    assert data_helper.get_user_data("user_data", "assert_cover_pic") in base.get_element("xpath", "assert_cover_pic").text

def test_LWS29(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "ecell_button")
    base.get_element("xpath", "ecell_button").click()
    sleep(1)
    base.get_element("xpath", "click_on_edit_cover_photos").click()
    sleep(4)
    os.system("C:\\Users\\User\\Desktop\\auto2.exe")
    sleep(5)
    base.get_element("xpath", "click_on_done_btn").click()
    sleep(1)
    assert data_helper.get_user_data("user_data", "assert_cover_pic") in base.get_element("xpath", "assert_cover_pic").text

def test_LWS30(web_driver):
    base.get_url(url)
    sleep(5)
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

def test_LWS31(web_driver):
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
    sleep(2)
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_date_picker")
    base.get_element("xpath", "click_on_date_picker").click()
    # base.get_driver().find_element_by_xpath("//*[@class='md-datepicker-triangle-button md-icon-button md-button']").click()
    # sleep(5)
    base.get_element("xpath", "date_for_future").click()
    sleep(1)
    base.get_element("xpath", "time_activities").click()
    # base.get_driver().find_element_by_xpath("(//*[@class='ui-timepicker-pm'])[19]").click()
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

def test_LWS32(web_driver):
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

def test_LWS33(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "ecell_button")
    base.get_element("xpath", "ecell_button").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_activity")
    base.get_element("xpath", "click_on_activity").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "select_any_upcoming_activities")
    base.get_element("xpath", "select_any_upcoming_activities").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_attend_btn")
    base.get_element("xpath", "click_on_attend_btn").click()
    sleep(5)
    assert base.is_element_present("xpath", "click_on_withdraw_btn")

def test_LWS34(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "ecell_button")
    base.get_element("xpath", "ecell_button").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_activity")
    base.get_element("xpath", "click_on_activity").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "select_any_upcoming_activities")
    base.get_element("xpath", "select_any_upcoming_activities").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_withdraw_btn")
    base.get_element("xpath", "click_on_withdraw_btn").click()
    sleep(1)
    base.get_element("xpath", "click_on_yes_btn").click()
    sleep(5)
    assert base.is_element_present("xpath", "click_on_attend_btn")

def test_LWS35(web_driver):
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

def test_LWS36(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "ecell_button")
    base.get_element("xpath", "ecell_button").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_activity")
    base.get_element("xpath", "click_on_activity").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_ongoing_activities")
    base.get_element("xpath", "click_on_ongoing_activities").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "select_any_ongoing_activities")
    base.get_element("xpath", "select_any_ongoing_activities").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_attend_btn")
    base.get_element("xpath", "click_on_attend_btn").click()
    sleep(5)
    assert base.is_element_present("xpath", "assert_go_live")

def test_LWS37(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "ecell_button")
    base.get_element("xpath", "ecell_button").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_activity")
    base.get_element("xpath", "click_on_activity").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_ongoing_activities")
    base.get_element("xpath", "click_on_ongoing_activities").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "select_any_ongoing_activities")
    base.get_element("xpath", "select_any_ongoing_activities").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "assert_go_live")
    base.get_element("xpath", "assert_go_live").click()
    sleep(5)
    assert base.is_element_present("xpath", "assert_i_am_live")

def test_LWS38(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "ecell_button")
    base.get_element("xpath", "ecell_button").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_activity")
    base.get_element("xpath", "click_on_activity").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_ongoing_activities")
    base.get_element("xpath", "click_on_ongoing_activities").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "select_any_ongoing_activities")
    base.get_element("xpath", "select_any_ongoing_activities").click()
    sleep(3)
    base.get_element("xpath", "check_edit_activities").click()
    sleep(5)
    # base.get_driver().find_element_by_xpath("//*[@class='md-datepicker-triangle-button md-icon-button md-button']").click()
    base.get_element("xpath", "click_on_date_picker").click()
    sleep(2)
    base.get_element("xpath", "date_for_past").click()
    sleep(1)
    base.get_element("xpath", "click_on_update").click()
    sleep(3)
    base.get_element("xpath", "click_on_yes_btn").click()
    sleep(1)
    base.get_element("xpath", "rating_for_closed_batches").click()
    base.get_element("xpath", "star_mark_submit_btn").click()
    sleep(2)
    assert data_helper.get_user_data("user_data", "submitted_successfully") in base.get_element("xpath","submitted_successfully").text

def test_LWS39(web_driver):
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
    # sleep(2)
    # base.get_driver().find_element_by_xpath("//*[@class='md-datepicker-triangle-button md-icon-button md-button']").click()
    # base.wait_for_element_to_be_clickable(30, "xpath", "select_date")
    # base.get_element("xpath", "select_date").click()
    # sleep(1)
    # base.get_element("xpath", "time_activities").click()
    # base.get_driver().find_element_by_xpath("(//*[@class='ui-timepicker-pm'])[19]").click()
    # sleep(1)
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

def test_LWS40(web_driver):
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
    base.wait_for_element_to_be_clickable(25, "xpath", "assert_publish_draft")
    base.get_element("xpath", "assert_publish_draft").click()
    sleep(1)
    assert data_helper.get_user_data("user_data", "assert_published_activities") in base.get_element("xpath","assert_published_activities").text

def test_LWS41(web_driver):
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
    sleep(10)
    base.get_element("xpath", "select_date").click()
    sleep(1)
    base.get_element("xpath", "time_activities").click()
    base.get_element("xpath", "select_time_schedule").click()
    sleep(1)
    # sleep(2)
    # base.get_driver().find_element_by_xpath( "//*[@class='md-datepicker-triangle-button md-icon-button md-button']").click()
    # base.wait_for_element_to_be_clickable(30, "xpath", "select_date")
    # base.get_element("xpath", "select_date").click()
    # sleep(1)
    # base.get_element("xpath", "time_activities").click()
    # base.get_driver().find_element_by_xpath("(//*[@class='ui-timepicker-pm'])[19]").click()
    # sleep(1)
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

def test_LWS42(web_driver):
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

def test_LWS43(web_driver):
    base.get_url(url)
    sleep(5)
    base.get_element("xpath", "ecell_button").click()
    base.wait_for_element_to_be_clickable(10, "xpath", "click_on_team")
    base.get_element("xpath", "click_on_team").click()
    base.wait_for_element_to_be_clickable(10, "xpath", "click_on_leader")
    base.get_element("xpath", "click_on_leader").click()
    base.wait_for_element_to_be_clickable(10, "xpath", "select_role")
    base.get_element("xpath", "select_role").click()
    base.wait_for_element_to_be_clickable(10, "xpath", "select_any_one_role")
    base.get_element("xpath", "select_any_one_role").click()
    element = base.get_element("xpath", "select_a_student")
    sleep(1)
    ActionChains(web_driver) \
        .key_down(Keys.TAB) \
        .click(element) \
        .perform()
    sleep(1)
    base.wait_for_element_to_be_clickable(10, "xpath", "select_any_one_student")
    base.get_element("xpath", "select_any_one_student").click()
    base.wait_for_element_to_be_clickable(10, "xpath", "click_on_done_btn")
    base.get_element("xpath", "click_on_done_btn").click()
    sleep(5)
    assert data_helper.get_user_data("user_data", "assert_eleader_activities") in base.get_element("xpath", "assert_eleader_activities").text
    # Assertions
    list = base.get_elements("xpath", "assert_team_list")
    for team in list:
        print(team.text)

def test_LWS44(web_driver):
    base.get_url(url)
    sleep(5)
    base.get_element("xpath", "ecell_button").click()
    base.wait_for_element_to_be_clickable(10, "xpath", "click_on_team")
    base.get_element("xpath", "click_on_team").click()
    base.wait_for_element_to_be_clickable(10, "xpath", "click_on_student_eleader")
    base.get_element("xpath", "click_on_student_eleader").click()
    base.wait_for_element_to_be_clickable(10, "xpath", "remove_from_ecell")
    base.get_element("xpath", "remove_from_ecell").click()
    sleep(1)
    base.get_element("xpath", "click_on_yes_btn").click()
    sleep(1)
    assert data_helper.get_user_data("user_data", "assert_removed_ecell") in base.get_element("xpath", "assert_removed_ecell").text
    # Assertions
    list = base.get_elements("xpath", "assert_team_list")
    for team in list:
        print(team.text)

def test_LWS45(web_driver):
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

def test_LWS46(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_visibile(25, "xpath", "ecell_button")
    base.get_element("xpath", "ecell_button").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_practicum")
    base.get_element("xpath", "click_on_practicum").click()
    sleep(2)
    base.get_element("xpath", "click_on_practicum_basic").click()
    # if (base.is_element_present("xpath", "click_on_subfolder_of_basic")):
    #     base.wait_for_element_to_be_clickable(25, "xpath", "click_on_subfolder_of_basic")
    #     base.get_element("xpath", "click_on_subfolder_of_basic").click()
    sleep(2)
    base.get_element("xpath", "veiw_pdf_file").click()
    sleep(2)
    assert data_helper.get_user_data("user_data", "assert_pdf_view") in base.get_element("xpath", "assert_pdf_view").text

def test_LWS47(web_driver):
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

def test_LWS48(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_visibile(25, "xpath", "student_course_header")
    base.get_element("xpath", "student_course_header").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_batch_name")
    base.get_element("xpath", "click_on_batch_name").click()
    base.wait_for_element_to_be_visibile(20, "xpath", "list_of_lesson")
    # assertion
    list = base.get_elements("xpath", "list_of_lesson")
    for lesson in list:
        print(lesson.text)

def test_LWS49(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_visibile(25, "xpath", "student_course_header")
    base.get_element("xpath", "student_course_header").click()
    base.wait_for_element_to_be_visibile(10, "xpath", "click_on_student_batch_chat")
    base.get_element("xpath", "click_on_student_batch_chat").click()
    base.get_element("xpath", "type_chat_message").send_keys(data_helper.get_user_data("user_data", "type_chat_message"))
    base.get_element("xpath", "send_chat_message").click()
    sleep(2)
    assert base.is_element_present("xpath", "assert_chat_message")

def test_LWS50(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_visibile(25, "xpath", "student_course_header")
    base.get_element("xpath", "student_course_header").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_student_number")
    base.get_element("xpath", "click_on_student_number").click()
    sleep(1)
    assert base.is_element_present("xpath", "assert_participates")

def test_LWS51(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_visibile(25, "xpath", "student_course_header")
    base.get_element("xpath", "student_course_header").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_student_number")
    base.get_element("xpath", "click_on_student_number").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_student_name")
    base.get_element("xpath", "click_on_student_name").click()
    sleep(1)
    assert base.is_element_present("xpath", "assert_student_details")

def test_LWS52(web_driver):
    base.get_url(url)
    sleep(5)
    base.get_element("xpath", "student_course_header").click()
    text_1 = base.get_element("xpath", "assert_enrolled_course").text
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_leave_batch")
    base.get_element("xpath", "click_on_leave_batch").click()
    sleep(1)
    base.get_element("xpath", "click_on_yes_btn").click()
    sleep(9)
    web_driver.refresh()
    text_2 = base.get_element("xpath", "assert_enrolled_course").text
    assert text_1 not in text_2

def test_LWS53(web_driver):
    base.get_url(url)
    sleep(5)
    window_before = web_driver.window_handles[0]
    base.get_element("xpath", "user_guide_tab").click()
    window_after = web_driver.window_handles[1]
    web_driver.switch_to_window(window_after)
    assert data_helper.get_user_data("user_data", "assert_learnwise_platform") in base.get_element("xpath", "assert_learnwise_platform").text
    web_driver.switch_to_window(window_before)

def test_LWS54(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_visibile(20, "xpath", "assert_feedback_video")
    base.get_element("xpath", "assert_feedback_video").click()
    base.wait_for_element_to_be_visibile(10, "xpath", "feedback_supports")
    assert base.is_element_present("xpath", "feedback_supports")

def test_LWS55(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_visibile(20, "xpath", "assert_feedback_video")
    base.get_element("xpath", "assert_feedback_video").click()
    sleep(1)
    assert base.is_element_present("xpath", "feedback_and_supports")

def test_LWS56(web_driver):
    base.get_url(url)
    sleep(5)
    base.wait_for_element_to_be_clickable(25, "xpath", "click_on_toggle")
    base.get_element("xpath", "click_on_toggle").click()
    base.wait_for_element_to_be_clickable(25, "xpath", "student_profile_icon")
    base.get_element("xpath", "student_profile_icon").click()
    sleep(1)
    base.get_element("xpath", "student_edit_icon").click()
    sleep(1)
    base.get_element("xpath", "edit_first_name").clear()
    sleep(1)
    base.get_element("xpath", "edit_first_name").send_keys(data_helper.get_user_data("user_data", "edit_first_name"))
    sleep(1)
    base.wait_for_element_to_be_visibile(10, "xpath", "save_changes")
    base.get_element("xpath", "save_changes").click()
    sleep(2)
    assert data_helper.get_user_data("user_data", "profile_updated") in base.get_element("xpath","profile_updated").text

def test_LWS57(web_driver):
    base.get_url(url)
    sleep(5)
    base.get_element("xpath", "click_on_toggle").click()
    base.get_element("xpath", "click_on_logout").click()
    sleep(2)
    assert data_helper.get_user_data("user_data", "assert_logout_text") in base.get_element("xpath", "assert_logout_button").text
