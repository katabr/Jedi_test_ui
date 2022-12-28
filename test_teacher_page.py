# Тест проверяет функции Use-cases роли Преподаватель

from pages.teacher_page import TeacherPage
from pages.general import Helper

import pytest

@pytest.mark.teacher()
class TestTeacherPage(Helper):

    @pytest.mark.TC_1()
    def test_check_timetable_t(self, browser_t):
        tcp = TeacherPage(browser_t)
        tcp.enter_timetable_t()
        tcp.should_be_header_timetable_t()

    @pytest.mark.TC_1()
    def test_check_use1_mission(self, browser_t):
        tcp = TeacherPage(browser_t)
        tcp.enter_timetable_t()
        tcp.push_button_mission_t()
        tcp.should_be_header_mission_t()

    @pytest.mark.TC_2()
    # @pytest.mark.skip()
    def test_check_chat(self, browser):
        tcp = TeacherPage(browser)
        tcp.push_button_chat()
        # pnp.enter_mail()
        tcp.should_be_header_chat()

    @pytest.mark.TC_2()
    # @pytest.mark.skip()
    def test_create_new_chat(self, browser):
        tcp = TeacherPage(browser)
        tcp.push_button_chat()
        tcp.create_new_chat()
        # tcp.enter_mail()
        #tcp.should_be_header_chat()

    @pytest.mark.TC_3()
    def test_check_use3_lessons(self, browser):
        tcp = TeacherPage(browser)
        tcp.push_button_lessons()
        tcp.should_be_header_lessons()

    @pytest.mark.TC_4()
    def test_check_use4_reaction(self, browser):
        tcp = TeacherPage(browser)
        tcp.push_button_reaction()
        tcp.push_button_opinion()
        # tcp.past_text_opinion()
        tcp.should_be_header_reaction()
