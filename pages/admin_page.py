from .locators import AdminLocators

from .general import General
from .general import Helper

class AdminPage(General, Helper):

    def create_new_chat_a(self):
        selector = self.browser.find_element(*AdminLocators.BUTTON_CREATE_CHAT_A)
        selector.click()

    # def past_text_opinion(self):
    #     text = AdminLocators.TEXT_OPINION
    #     selector = self.browser.find_element(*AdminLocators.FIELD_OPINION)
    #     self.past_text(self,selector,text)

    def push_button_chat_a(self):
        selector = self.browser.find_element(*AdminLocators.BUTTON_CHAT_A)
        selector.click()

    def push_create_chat_with_user(self):
        selector = self.browser.find_element(*AdminLocators.BUTTON_CREATE_CHAT_WITH_USER)
        selector.click()

    # def push_button_opinion(self):
    #     selector = self.browser.find_element(*AdminLocators.BUTTON_OPINION)
    #     selector.click()
    #
    # def push_button_reaction(self):
    #     selector = self.browser.find_element(*AdminLocators.BUTTON_REACTION)
    #     selector.click()

    def should_be_header_chat_a(self):
        assert self.check_exists_element(*AdminLocators.TEXT_HEADER_CHAT), "Чаты не отображаются"

    def should_be_item_begin_chat(self):
        assert self.check_exists_element(*AdminLocators.TEXT_BEGIN_CHAT), "Новый чат не создан"

    # def should_be_header_reaction(self):
    #     assert self.check_exists_element(*AdminLocators.TEXT_HEADER_REACTION), "Оценка дисциплины не отображается"

