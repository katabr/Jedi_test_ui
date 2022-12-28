from selenium import webdriver
import pytest
#import allure

from pages.locators import PadavanLocators
from pages.general import Helper

@pytest.fixture()
def browser():
    #chromedriver = r'c:\chromedriver\chromedriver.exe'
    #chromedriver = r'.\selenium_env\chromedriver.exe'
    chromedriver = r'.\chromedriver.exe'
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')  # для открытия headless-браузера
    # browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
    browser = webdriver.Chrome(executable_path=chromedriver)
    # browser = webdriver.Chrome()
    browser.implicitly_wait(10)

    url = "http://localhost:3851/#/login"
    browser.get(url)

    # аутентификация
    login = browser.find_element(*PadavanLocators.LOGIN)
    login.send_keys("AnakinSkywalker")

    password = browser.find_element(*PadavanLocators.PASSWORD)
    password.send_keys("32432432")

    button_enter = browser.find_element(*PadavanLocators.BUTTON_ENTER)
    button_enter.click()

    # закрываем браузер
    yield browser
    browser.quit()

@pytest.fixture()
def clear_cookies(browser):
    browser.delete_all_cookies()
    # driver.get("chrome://settings/clearBrowserData");
    # cleanCacheIframe = By.xpath("//iframe[@src='chrome://settings-frame/clearBrowserData']");
    # driver.switchTo().frame(driver.findElement(cleanCacheIframe));
    #
    # driver.findElement(By.id("clear-browser-data-commit")).click();
    # обновить страницу
    browser.navigate().refresh()
    print("Куки очищены")

@pytest.fixture()
def browser_t():
    chromedriver = r'.\chromedriver.exe'
    browser = webdriver.Chrome(executable_path=chromedriver)
    # browser = webdriver.Chrome()
    browser.implicitly_wait(10)

    url = "http://localhost:3851/#/login"
    browser.get(url)

    # аутентификация преподаватель
    login = browser.find_element(*PadavanLocators.LOGIN)
    login.send_keys("Yoda1337")

    password = browser.find_element(*PadavanLocators.PASSWORD)
    password.send_keys("111111")

    button_enter = browser.find_element(*PadavanLocators.BUTTON_ENTER)
    button_enter.click()

    # закрываем браузер
    yield browser
    browser.quit()


@pytest.fixture()
def browser_a():
    chromedriver = r'.\chromedriver.exe'
    browser = webdriver.Chrome(executable_path=chromedriver)
    # browser = webdriver.Chrome()
    browser.implicitly_wait(10)

    url = "http://localhost:3851/#/login"
    browser.get(url)

    # аутентификация преподаватель
    login = browser.find_element(*PadavanLocators.LOGIN)
    login.send_keys("TechGuy")

    password = browser.find_element(*PadavanLocators.PASSWORD)
    password.send_keys("54321")

    button_enter = browser.find_element(*PadavanLocators.BUTTON_ENTER)
    button_enter.click()

    # закрываем браузер
    yield browser
    browser.quit()
