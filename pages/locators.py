# Файл содержит наборы локаторов

from selenium.webdriver.common.by import By

class CommonLocators():
    BUTTON_ACCESS_YES = (By.XPATH, '//span[text()="Да"]')

    # BUTTON_BUY_CONTINUE = (By.XPATH, '//*[text()=" Продолжить оформление "]')
    # BUTTON_NEXT = (By.XPATH, '//*[text() = "Далее"]')
    # ERROR_401 = (By.XPATH, '//*[text() = " Ошибка при получении параметров персонального предложения "]')
    # FIELD_ENTER_KOD = (By.CSS_SELECTOR, 'input[autocomplete="one-time-code"]')
    # FIELD_ENTER_NUMBER = (By.CSS_SELECTOR, 'input[name="login"]')
    # STATUS_ACTIVE = (By.CSS_SELECTOR,'div[class="status active"]')
    # TEXT_ACCESS_REQUEST = (By.CSS_SELECTOR, 'h2.h2.getToTitle')

class GeneralLocators():
    CONFIRM_DEL_BUTTON = (By.CSS_SELECTOR, 'button.remove-icon.text-white.footer')
    # DOCUMENTS = (By.XPATH, '//span[text()="Документы"]')
    # TURN_PAGES = (By.XPATH, '//button[text()="›"]')

class StartLocators():
    BUTTON_CHAT = (By.XPATH, '//button[text()="Чаты"]')
    BUTTON_ENTER = (By.CSS_SELECTOR, '.el-button.login-page__button')
    BUTTON_LESSONS = (By.XPATH, '//button[text()="Предметы"]')
    BUTTON_OPINION = (By.XPATH, '//*[text()="Открытый отзыв"]')
    BUTTON_REACTION = (By.XPATH, '//button[text()="Оценить дисциплину"]')
    BUTTON_TASKS = (By.XPATH, '//button[text()="Занятия"]')
    BUTTON_TIMETABLE = (By.XPATH, '//button[text()="Расписание"]')
    FIELD_OPINION = (By.CSS_SELECTOR,'textarea.el-textarea__inner]')
    LOGIN = (By.CSS_SELECTOR,'.el-input__inner[type="text"]')
    PASSWORD = (By.CSS_SELECTOR,'.el-input__inner[type="password"]')
    TEXT_HEADER_CHAT = (By.XPATH, '//h1[text()="Чаты"]')
    TEXT_HEADER_LESSONS = (By.XPATH, '//h1[text()="Предметы"]')
    TEXT_HEADER_REACTION = (By.XPATH, '//h1[text()="Оценка дисциплины"]')
    TEXT_HEADER_TIMETABLE = (By.XPATH, '//h1[text()="Расписание"]')
    TEXT_OPINION = "Тестовый опрос"
