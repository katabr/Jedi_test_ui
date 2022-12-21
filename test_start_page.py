#Тест проверяет функции Use-cases

from pages.start_page import StartPage
from pages.general import Helper

import pytest

@pytest.mark.TC_1()
#@pytest.mark.skip()
class TestStartPage(Helper):
    #@pytest.mark.skip()
    def test_check_use1_timetable(self, browser):
        spg = StartPage(browser)
        spg.enter_timetable()
        #spg.enter_tasks()
        spg.should_be_header_timetable()
