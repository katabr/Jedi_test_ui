from selenium import webdriver
import pytest
#import allure

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

    # аутентификация
    # login = browser.find_element_by_css_selector('#username')
    # login.send_keys("")

    # button_enter = browser.find_element_by_xpath('//button[text()="Войти"]')
    # button_enter.click()

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

