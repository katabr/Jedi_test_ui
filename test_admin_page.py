# Тест проверяет функции Use-cases роли Администратор

from pages.admin_page import AdminPage
from pages.general import Helper

import pytest

@pytest.mark.admin()
class TestAdminPage(Helper):

    @pytest.mark.TC_2()
    def test_check_chat_a(self, browser_a):
        amp = AdminPage(browser_a)
        amp.push_button_chat_a()
        amp.should_be_header_chat_a()

    @pytest.mark.TC_2()
    def test_create_new_chat_a(self, browser_a):
        amp = AdminPage(browser_a)
        amp.push_button_chat_a()
        amp.create_new_chat_a()
        amp.push_create_chat_with_user()
        amp.push_button_chat_a()
        amp.should_be_item_begin_chat()

    @pytest.mark.TC_2()
    def test_create_new_chat_t(self, browser):
        tcp = TeacherPage(browser)
        tcp.push_button_chat()
        tcp.create_new_chat()
        tcp.push_create_chat_with_user()
        tcp.push_button_chat()
        tcp.should_be_item_begin_chat()



    # @pytest.mark.TC_3()
    # def test_check_use3_lessons(self, browser):
    #     tcp = TeacherPage(browser)
    #     tcp.push_button_lessons()
    #     tcp.should_be_header_lessons()
    #
    # @pytest.mark.TC_4()
    # def test_check_use4_reaction(self, browser):
    #     tcp = TeacherPage(browser)
    #     tcp.push_button_reaction()
    #     tcp.push_button_opinion()
    #     # tcp.past_text_opinion()
    #     tcp.should_be_header_reaction()