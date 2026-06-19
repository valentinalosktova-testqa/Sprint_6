from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_answer_text(self, index):
        question_locator = (By.XPATH, f"//div[@id='accordion__heading-{index}']")
        answer_locator = (By.XPATH, f"//div[@id='accordion__panel-{index}']/p")

        question_element = self.find_element(question_locator)
        self.scroll_to_element(question_element)
        self.click_element(question_locator)

        answer_element = self.wait_for_visibility(answer_locator)
        return answer_element.text

    def click_order_button_top(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        button = self.find_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.scroll_to_element(button)
        button.click()

    def click_logo_scooter(self):
        self.click_element(MainPageLocators.LOGO_SCOOTER)

    def click_logo_yandex(self):
        self.click_element(MainPageLocators.LOGO_YANDEX)