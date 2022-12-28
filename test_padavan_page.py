# Тест проверяет функции Use-cases роли Падаван

from pages.padavan_page import PadavanPage
from pages.general import Helper

import pytest

# @pytest.mark.padavan()
class TestPadavanPage(Helper):

    @pytest.mark.TC_1()
    def test_check_timetable(self, browser):
        pnp = PadavanPage(browser)
        pnp.enter_timetable()
        # pnp.enter_tasks()
        pnp.should_be_header_timetable()

    @pytest.mark.TC_1()
    def test_check_use1_mission(self, browser):
        pnp = PadavanPage(browser)
        pnp.enter_timetable()
        pnp.push_button_mission()
        pnp.should_be_header_mission()

    @pytest.mark.TC_2()
    def test_check_chat(self, browser):
        pnp = PadavanPage(browser)
        pnp.push_button_chat()
        pnp.should_be_header_chat()

    @pytest.mark.TC_2()
    def test_create_new_chat(self, browser):
        pnp = PadavanPage(browser)
        pnp.push_button_chat()
        pnp.create_new_chat()
        pnp.push_create_chat_with_user()
        pnp.push_button_chat()
        pnp.should_be_item_begin_chat()

    @pytest.mark.TC_3()
    def test_check_lessons(self, browser):
        pnp = PadavanPage(browser)
        pnp.push_button_lessons()
        pnp.should_be_header_lessons()

    @pytest.mark.TC_4()
    def test_check_reaction(self, browser):
        pnp = PadavanPage(browser)
        pnp.push_button_lessons()
        pnp.push_button_reaction()
        #pnp.push_button_opinion()
        # pnp.past_text_opinion()
        pnp.should_be_header_reaction()

    @pytest.mark.TC_4()
    def test_check_opinion(self, browser):
        pnp = PadavanPage(browser)
        pnp.push_button_lessons()
        pnp.push_button_reaction()
        pnp.push_button_opinion()
        #pnp.past_text_opinion()
        pnp.should_be_area_opinion()

    @pytest.mark.TC_5()
    def test_check_output_task(self, browser):
        pnp = PadavanPage(browser)
        pnp.push_button_lessons()
        pnp.push_button_output_task()
        pnp.push_button_send_request()
        pnp.should_be_able_output_tasks()

    # @pytest.mark.TC_6()
    # def test_check_editing_profile(self, browser):
    #     pnp = PadavanPage(browser)
    #     pnp.push_button_profile()
    #     pnp.push_button_open_menu_profile()
    #     pnp.past_profile_test_text()
    #     # pnp.push_button_change()
    #     # pnp.should_be_able_output_tasks()

