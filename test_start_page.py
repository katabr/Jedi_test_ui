# Тест проверяет функции Use-cases

from pages.start_page import StartPage
from pages.general import Helper

import pytest

@pytest.mark.TC_1()
# @pytest.mark.skip()
class TestStartPage(Helper):

    @pytest.mark.TC_1()
    # @pytest.mark.skip()
    def test_check_use1_timetable(self, browser):
        spg = StartPage(browser)
        spg.enter_timetable()
        # spg.enter_tasks()
        spg.should_be_header_timetable()

    @pytest.mark.TC_2()
    # @pytest.mark.skip()
    def test_check_use2_chat(self, browser):
        spg = StartPage(browser)
        spg.push_button_chat()
        # spg.enter_mail()
        spg.should_be_header_chat()

    @pytest.mark.TC_3()
    def test_check_use3_lessons(self, browser):
        spg = StartPage(browser)
        spg.push_button_lessons()
        spg.should_be_header_lessons()

    @pytest.mark.TC_4()
    def test_check_use4_reaction(self, browser):
        spg = StartPage(browser)
        spg.push_button_reaction()
        spg.push_button_opinion()
        # spg.past_text_opinion()
        spg.should_be_header_reaction()