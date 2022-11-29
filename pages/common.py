import time

from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC

from .locators import NumberLocators
from .locators import CommonLocators
from .general import General
from .general import Helper

class MocksUrls(General, Helper):
    def active_kion(self,browser):
            active_kion = "https://personal-test.eland.mts-corp.ru/kion?haveActiveProduct=1"
            browser.get(active_kion)

class Common(General, Helper):

    def access_request(self):
        selector = self.browser.find_element(*CommonLocators.TEXT_ACCESS_REQUEST)
        #time.sleep(1)
        WDW(self.browser, 5).until(EC.visibility_of_element_located((selector)))
        selector = self.browser.find_element(*CommonLocators.BUTTON_ACCESS_YES)
        selector.click()

    def autorization(self):
        self.enter_number1()
        self.enter_kod1()
        # self.should_be_success_autorisation()

    def enter_kod(self):
        selector = CommonLocators.FIELD_ENTER_KOD
        text = NumberLocators.KOD_EVA_1
        self.past_text(self, selector, text)

    def enter_number(self):
        selector = CommonLocators.FIELD_ENTER_NUMBER
        text = NumberLocators.NUMBER_EVA_1
        self.past_text(self, selector, text)
        selector = self.browser.find_element(*CommonLocators.BUTTON_NEXT)
        selector.click()

    def push_button_continue_checkout(self):
        selector = self.browser.find_element(*CommonLocators.BUTTON_BUY_CONTINUE)
        WDW(self.browser, 5).until(EC.element_to_be_clickable((selector))).click()

    def shoul_be_button_continue_checkout(self):
        #time.sleep(0.5)
        selector = self.browser.find_element(*CommonLocators.BUTTON_BUY_CONTINUE)
        WDW(self.browser, 5).until(EC.element_to_be_clickable((selector))) #.click()
        assert self.check_exists_element(*CommonLocators.BUTTON_BUY_CONTINUE), "Кнопка 'Продолжить оформление' не отображается"

    def should_be_error_personal_offer(self):
        text_error = " Ошибка при получении параметров персонального предложения "
        selector = self.browser.find_element(*CommonLocators.ERROR_401)
        error = selector.get_attribute('text')
        assert error==text_error , "Ошибка авторизации"

    # def should_be_success_autorisation(self):
        #assert условие , "Ошибка авторизации"