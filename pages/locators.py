# Файл содержит наборы локаторов

from selenium.webdriver.common.by import By

class CommonLocators():
    BUTTON_ACCESS_YES = (By.XPATH, '//span[text()="Да"]')
    BUTTON_BUY_CONTINUE = (By.XPATH, '//*[text()=" Продолжить оформление "]')
    BUTTON_NEXT = (By.XPATH, '//*[text() = "Далее"]')
    ERROR_401 = (By.XPATH, '//*[text() = " Ошибка при получении параметров персонального предложения "]')
    FIELD_ENTER_KOD = (By.CSS_SELECTOR, 'input[autocomplete="one-time-code"]')
    FIELD_ENTER_NUMBER = (By.CSS_SELECTOR, 'input[name="login"]')
    STATUS_ACTIVE = (By.CSS_SELECTOR,'div[class="status active"]')
    TEXT_ACCESS_REQUEST = (By.CSS_SELECTOR, 'h2.h2.getToTitle')

class GeneralLocators():
    CONFIRM_DEL_BUTTON = (By.CSS_SELECTOR, 'button.remove-icon.text-white.footer')
    DOCUMENTS = (By.XPATH, '//span[text()="Документы"]')
    TURN_PAGES = (By.XPATH, '//button[text()="›"]')

class StartLocators():
    # BUTTON_BUY_UP = (By.CSS_SELECTOR, 'button.btn.btn-primary.btn-hero')
    # BUTTON_DISCOUNT = (By.CSS_SELECTOR, '[ng-reflect-gtm-button = "get-personal-discount"]')
    # BUTTON_END = (By.XPATH, '//*[text() = "Завершить"]')
    # BUTTON_LISTEN_IN_APPLICATION = (By.XPATH, '//*[text()[contains(.," Слушать")]]')
    # BUTTON_PAY = (By.XPATH, '//*[text() = "Оплатить"]')
    # CHOOSE_BANK_BOOK = (By.XPATH, '//*[text()[contains(.,"Счёт ")]]')
    # CHOOSE_CARD = (By.XPATH, '//*[text()[contains(.,"MIR")]]')
    # FAQUESTION1 = (By.CSS_SELECTOR, '[data-target="#collapseItem1"]')
    # STATUS_PAID = (By.XPATH, '//*[text() = "Оплачено"]')
    # TEXT_ACTIVE = (By.XPATH, '//*[text() = " Активна "]')
    # TEXT_FAQUESTION1 = (By.CSS_SELECTOR, 'div.faq__collapse-text')
    # TEXT_NO_PERSONAL_OFFER = (By.XPATH, '//*[text()[contains(.,"  Персонального предложения для вас пока нет. ")]]')
    # BUTTON_MORE_INFORMATION_MUSIC = (By.CSS_SELECTOR, 'section[class="footer"]>div>div>div>a[target="_blank"]')
    #BUTTON_MORE_INFORMATION_MUSIC = (By.XPATH, '//*[contains(@text,"Подробнее об"]')
    #BUTTON_MUSIC = (By.XPATH, '//span[contains(@text,"МТС"]')
    BUTTON_MUSIC = (By.CSS_SELECTOR, 'section[class="footer__application"]>div>div>div>a[target="_blank"]>img')
