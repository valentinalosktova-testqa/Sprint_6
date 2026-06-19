import pytest
from pages.main_page import MainPage

class TestLogo:
    def test_logo_scooter_goes_to_main(self, driver):
        main_page = MainPage(driver)
        driver.get("https://qa-scooter.praktikum-services.ru/")
        main_page.click_logo_scooter()
        assert main_page.get_current_url() == "https://qa-scooter.praktikum-services.ru/"

    def test_logo_yandex_opens_dzen(self, driver):
        main_page = MainPage(driver)
        driver.get("https://qa-scooter.praktikum-services.ru/")
        main_page.click_logo_yandex()

        main_page.switch_to_new_window()
        main_page.wait_for_url_not_blank()

        current_url = main_page.get_current_url()
        assert "dzen.ru" in current_url or "yandex.ru" in current_url