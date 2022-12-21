import time
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC

from .locators import StartLocators

from .general import General
from .general import Helper

class StartPage(General, Helper):

    def enter_timetable(self):
        selector = self.browser.find_element(*StartLocators.BUTTON_TIMETABLE)
        selector.click()

    # def enter_tasks(self):
    #     selector = self.browser.find_element(*StartLocators.BUTTON_TASKS)
    #     selector.click()

    def should_be_header_timetable(self):
        assert self.check_exists_element(*StartLocators.TEXT_HEADER_TIMETABLE), "Расписание не отображается"


    # def active_kion(self):
    #     active_kion = "https://personal-test.eland.mts-corp.ru/kion?haveActiveProduct=1"
    #     self.browser.get(active_kion)
    #
    # def check_item_change_price(self):
    #     self.scroll()
    #     selector = self.browser.find_element(*StartKionLocators.FAQUESTION1)
    #     self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     WDW(self.browser,5).until(EC.element_to_be_clickable((selector))).click()
    #
    # def click_link_kion(self):
    #     self.scroll()
    #     selector = self.browser.find_element(*StartKionLocators.BUTTON_KION)
    #     selector.click()
    #
    # def get_name_film_you_tube(self):
    #     selector = self.browser.find_element(*StartKionLocators.YOU_TUBE_FILM_NAME)
    #     film_name = selector.get_attribute('text')
    #     return film_name
    #
    # def get_name_first_modal(self):
    #     self.scroll()
    #     selector = self.browser.find_elements(*StartKionLocators.MODALS_FILM_NAME)
    #     film_name = selector[0].get_attribute('text')
    #     return film_name
    #
    # def get_personal_discount(self):
    #     selector = self.browser.find_element(*StartKionLocators.BUTTON_DISCOUNT)
    #     selector.click()
    # def push_button_buy_up(self):
    #     selector = self.browser.find_element(*StartKionLocators.BUTTON_BUY_UP)
    #     WDW(self.browser, 5).until(EC.element_to_be_clickable((selector))).click()
    #
    # def push_button_buy_down(self):
    #     self.scroll()
    #     selector = self.browser.find_element(*StartKionLocators.BUTTON_BUY_DOWN)
    #     WDW(self.browser, 5).until(EC.element_to_be_clickable((selector))).click()
    #
    # def push_first_modal(self):
    #     self.scroll()
    #     selector = self.browser.find_elements(*StartKionLocators.BUTTONS_OF_MODALS)
    #     selector[0].click()
    #
    # def should_be_button_bye_199(self):
    #     selector = self.browser.find_element(*StartKionLocators.BUTTON_BUY_199)
    #     WDW(self.browser, 5).until(EC.element_to_be_clickable((selector))).click()
    #     assert self.check_exists_element(*StartKionLocators.BUTTON_BUY_199), "Кнопка 'Купить за 199р' не отображается"
    #
    #
    # def should_be_item_change_price_show(self):
    #     time.sleep(0.5)
    #     assert self.check_exists_element(*StartKionLocators.TEXT_FAQUESTION1), "Вкладка 'Часто задаваемые вопросы' не открывается"
    #
    # # def shoul_be_active_status(self):
    #
    # def should_be_open_description_film_window(self,film_name):
    #     # handle = self.browser.current_window_handle
    #     # self.browser.switch_to.window(handle)
    #     name_you_tube = self.get_name_film_you_tube()
    #     assert film_name == name_you_tube, "Не работает модальное окно перехода на YouTube"
    #
    # def should_be_open_kion_webcite(self):
    #     handle = self.browser.window_handles
    #     self.browser.switch_to.window(handle[1])
    #     url = self.browser.current_url
    #     self.browser.close()
    #     assert "kion.ru" in url, "Не работает ссылка на сайт КИОН"
    #
    # def should_be_active_kion(self):
    #     self.active_kion()
    #     #selector = self.browser.find_element(*StartKionLocators.TEXT_ACTIVE)
    #     assert self.check_exists_element(*StartKionLocators.TEXT_ACTIVE), "Статус подписки 'Активна' не отображается"
    #
    # def should_be_no_offer_kion(self):
    #     no_offer_kion = "https://personal-test.eland.mts-corp.ru/kion?haveActiveProduct=1"
    #     self.browser.get(no_offer_kion)
    #     selector = self.browser.find_element(*StartKionLocators.TEXT_NO_PERSONAL_OFFER)
    #     WDW(self.browser, 5).until(EC.visibility_of((selector)))
    #     assert self.check_exists_element(*StartKionLocators.TEXT_NO_PERSONAL_OFFER), "Сообщение 'Персонального предложения пока нет' не отображается"
    #
