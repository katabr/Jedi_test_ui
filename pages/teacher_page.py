from .locators import TeacherLocators

from .general import General
from .general import Helper

class TeacherPage(General, Helper):

    def create_new_chat(self):
        selector = self.browser.find_element(*TeacherLocators.BUTTON_CREATE_CHAT)
        selector.click()

    def enter_timetable_t(self):
        selector = self.browser.find_element(*TeacherLocators.BUTTON_TIMETABLE)
        selector.click()

    def past_text_opinion(self):
        text = TeacherLocators.TEXT_OPINION
        selector = self.browser.find_element(*TeacherLocators.FIELD_OPINION)
        self.past_text(self,selector,text)

    def push_button_chat(self):
        selector = self.browser.find_element(*TeacherLocators.BUTTON_CHAT)
        selector.click()

    def push_button_lessons(self):
        selector = self.browser.find_element(*TeacherLocators.BUTTON_LESSONS)
        selector.click()

    def push_button_mission_t(self):
        selector = self.browser.find_element(*TeacherLocators.BUTTON_MISSION)
        selector.click()


    def push_button_opinion(self):
        selector = self.browser.find_element(*TeacherLocators.BUTTON_OPINION)
        selector.click()

    def push_button_reaction(self):
        selector = self.browser.find_element(*TeacherLocators.BUTTON_REACTION)
        selector.click()

    def should_be_header_chat(self):
        assert self.check_exists_element(*TeacherLocators.TEXT_HEADER_CHAT), "Чаты не отображаются"

    def should_be_header_reaction(self):
        assert self.check_exists_element(*TeacherLocators.TEXT_HEADER_REACTION), "Оценка дисциплины не отображается"

    def should_be_header_timetable_t(self):
        assert self.check_exists_element(*TeacherLocators.TEXT_HEADER_TIMETABLE), "Расписание не отображается"

    def should_be_header_lessons(self):
        assert self.check_exists_element(*TeacherLocators.TEXT_HEADER_LESSONS), "Предметы не отображаются"

    def should_be_header_mission_t(self):
        assert self.check_exists_element(*TeacherLocators.TEXT_HEADER_MISSION), "Страница Миссии не отображается"
