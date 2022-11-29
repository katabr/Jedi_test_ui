#Тест проверяет функции лендинга Музыка
from conftest import browser, start_music
from pages.start_page_music import StartPageMusic
from pages.general import Helper

import pytest

@pytest.mark.TC_2()
@pytest.mark.start_page_music()
#@pytest.mark.skip()
class TestStartPageMusic(Helper):

    @pytest.fixture()
    def music_success_user(self, browser):
        #success_user = "http://localhost:4200/music?msisdn=76340030961"
        # 76340007871- от Юрия подключение
        success_user = "http://localhost:4200/music?msisdn=76340007871"
        #success_user = "http://localhost:4200/music?useMocks=1&haveActiveProduct=1"
        browser.get(success_user)

    #@pytest.mark.skip()
    def test_check_FAQ(self, browser, start_music):
        spm = StartPageMusic(browser)
        spm.check_item_question()
        spm.should_be_item_question_show()

    #@pytest.mark.skip()
    def test_link_music(self, browser, start_music):
        spm = StartPageMusic(browser)
        spm.click_link_music()
        spm.should_be_open_music_webcite()

   #@pytest.mark.skip()
    def test_link_more_information(self, browser, start_music):
        spm = StartPageMusic(browser)
        spm.click_link_more_information()
        spm.should_be_open_music_webcite()

