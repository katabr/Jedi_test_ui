import time
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC

from .locators import PadavanLocators

from .general import General
from .general import Helper

class PadavanPage(General, Helper):

    def create_new_chat(self):
        selector = self.browser.find_element(*PadavanLocators.BUTTON_CREATE_CHAT)
        selector.click()

    def enter_timetable(self):
        selector = self.browser.find_element(*PadavanLocators.BUTTON_TIMETABLE)
        selector.click()

    # def enter_tasks(self):
    #     selector = self.browser.find_element(*PadavanLocators.BUTTON_TASKS)
    #     selector.click()

    def past_text_opinion(self):
        text = PadavanLocators.TEXT_OPINION
        selector = self.browser.find_element(*PadavanLocators.FIELD_OPINION)
        self.past_text(self,selector,text)

    def push_button_chat(self):
        selector = self.browser.find_element(*PadavanLocators.BUTTON_CHAT)
        selector.click()

    def push_button_lessons(self):
        selector = self.browser.find_element(*PadavanLocators.BUTTON_LESSONS)
        selector.click()

    def push_button_mission(self):
        selector = self.browser.find_element(*PadavanLocators.BUTTON_MISSION)
        selector.click()

    def push_create_chat_with_user(self):
        selector = self.browser.find_element(*PadavanLocators.BUTTON_CREATE_CHAT_WITH_USER)
        selector.click()

    def push_button_opinion(self):
        selector = self.browser.find_element(*PadavanLocators.BUTTON_OPINION)
        selector.click()

    def push_button_output_task(self):
        selector = self.browser.find_element(*PadavanLocators.BUTTON_OUTPUT_TASK)
        selector.click()

    def push_button_send_request(self):
        selector = self.browser.find_element(*PadavanLocators.BUTTON_SEND_REQUEST)
        selector.click()

    def push_button_reaction(self):
        selector = self.browser.find_element(*PadavanLocators.BUTTON_REACTION)
        selector.click()

    def should_be_able_output_tasks(self):
        assert self.check_exists_element(*PadavanLocators.TEXT_ABLE_OUTPUT_TASKS), "Доступные выпускные задания не отображаются"

    def should_be_area_opinion(self):
        assert self.check_exists_element(*PadavanLocators.TEXT_AREA_OPINION), "Отзыв не отображается"
    def should_be_header_chat(self):
        assert self.check_exists_element(*PadavanLocators.TEXT_HEADER_CHAT), "Чаты не отображаются"

    def should_be_item_begin_chat(self):
        assert self.check_exists_element(*PadavanLocators.TEXT_BEGIN_CHAT), "Новый чат не создан"

    def should_be_header_reaction(self):
        assert self.check_exists_element(*PadavanLocators.TEXT_HEADER_REACTION), "Оценка дисциплины не отображается"

    def should_be_header_timetable(self):
        assert self.check_exists_element(*PadavanLocators.TEXT_HEADER_TIMETABLE), "Расписание не отображается"

    def should_be_header_lessons(self):
        assert self.check_exists_element(*PadavanLocators.TEXT_HEADER_LESSONS), "Предметы не отображаются"

    def should_be_header_mission(self):
        assert self.check_exists_element(*PadavanLocators.TEXT_HEADER_MISSION), "Страница Миссии не отображается"
