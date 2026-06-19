import pytest
from pages.main_page import MainPage
from pages.urls import Urls
from data import TestData

class TestQuestions:
    @pytest.mark.parametrize("index, expected_text", TestData.QUESTIONS)
    def test_question(self, driver, index, expected_text):
        main_page = MainPage(driver)
        driver.get(Urls.MAIN_PAGE)
        answer = main_page.get_answer_text(index)
        assert answer == expected_text