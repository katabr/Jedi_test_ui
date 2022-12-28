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
    def test_create_new_chat_a(self, browser_a):
        amp = AdminPage(browser_a)
        amp.push_button_chat_a()
        amp.create_new_chat_a()
        amp.push_create_chat_with_user()
        amp.push_button_chat_a()
        amp.should_be_item_begin_chat()
