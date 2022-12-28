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
    def test_check_mission_t(self, browser_t):
        tcp = TeacherPage(browser_t)
        tcp.enter_timetable_t()
        tcp.push_button_mission_t()
        tcp.should_be_header_mission_t()

    @pytest.mark.TC_2()
    def test_check_chat_t(self, browser_t):
        tcp = TeacherPage(browser_t)
        tcp.push_button_chat()
        tcp.should_be_header_chat()

    @pytest.mark.TC_2()
    def test_create_new_chat_t(self, browser_t):
        tcp = TeacherPage(browser_t)
        tcp.push_button_chat()
        tcp.create_new_chat()
        tcp.push_create_chat_with_user()
        tcp.push_button_chat()
        tcp.should_be_item_begin_chat()
