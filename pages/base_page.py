import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Найти элемент по локатору {locator}")
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step("Кликнуть по элементу {locator}")
    def click_element(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    @allure.step("Ввести текст '{text}' в элемент {locator}")
    def send_keys_to_element(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    @allure.step("Дождаться видимости элемента {locator}")
    def wait_for_visibility(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Дождаться, пока URL содержит текст '{text}'")
    def wait_for_url_contains(self, text, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.url_contains(text)
        )

    @allure.step("Прокрутить к элементу")
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Кликнуть через JavaScript по элементу {locator}")
    def click_element_js(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Переключиться на новое окно")
    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step("Дождаться, когда URL перестанет быть about:blank")
    def wait_for_url_not_blank(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.current_url != "about:blank"
        )

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url