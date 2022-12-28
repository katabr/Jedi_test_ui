# Тест проверяет функции Use-cases роли Падаван

from pages.padavan_page import PadavanPage
from pages.general import Helper

import pytest

# @pytest.mark.padavan()
class TestPadavanPage(Helper):

    @pytest.mark.TC_1()
    # @pytest.mark.skip()
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
    # @pytest.mark.skip()
    def test_check_chat(self, browser):
        pnp = PadavanPage(browser)
        pnp.push_button_chat()
        # pnp.enter_mail()
        pnp.should_be_header_chat()

    @pytest.mark.TC_2()
    # @pytest.mark.skip()
    def test_create_new_chat(self, browser):
        pnp = PadavanPage(browser)
        pnp.push_button_chat()
        pnp.create_new_chat()
        # pnp.enter_mail()
        #pnp.should_be_header_chat()



    @pytest.mark.TC_3()
    def test_check_use3_lessons(self, browser):
        pnp = PadavanPage(browser)
        pnp.push_button_lessons()
        pnp.should_be_header_lessons()

    @pytest.mark.TC_4()
    def test_check_use4_reaction(self, browser):
        pnp = PadavanPage(browser)
        pnp.push_button_reaction()
        pnp.push_button_opinion()
        # pnp.past_text_opinion()
        pnp.should_be_header_reaction()