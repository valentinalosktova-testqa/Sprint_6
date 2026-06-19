import pytest
from pages.main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait


class TestLogo:
    def test_logo_scooter_goes_to_main(self, driver):
        main_page = MainPage(driver)
        driver.get("https://qa-scooter.praktikum-services.ru/")
        main_page.click_logo_scooter()
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"

    def test_logo_yandex_opens_dzen(self, driver):
        main_page = MainPage(driver)
        driver.get("https://qa-scooter.praktikum-services.ru/")
        main_page.click_logo_yandex()

        driver.switch_to.window(driver.window_handles[1])

    # Ждём, пока URL загрузится и станет не пустым
        WebDriverWait(driver, 10).until(
            lambda d: d.current_url != "about:blank"
        )

        assert "dzen.ru" in driver.current_url or "yandex.ru" in driver.current_url