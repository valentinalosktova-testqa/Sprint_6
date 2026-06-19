import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pages.locators import OrderPageLocators
from pages.base_page import BasePage

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Заполнить форму заказа")
    def fill_order_form(self, data):
        self.wait_for_visibility(OrderPageLocators.NAME_INPUT)
        self.send_keys_to_element(OrderPageLocators.NAME_INPUT, data["name"])
        self.send_keys_to_element(OrderPageLocators.SURNAME_INPUT, data["surname"])
        self.send_keys_to_element(OrderPageLocators.ADDRESS_INPUT, data["address"])
        self.select_metro(data["metro"])
        self.send_keys_to_element(OrderPageLocators.PHONE_INPUT, data["phone"])

    @allure.step("Клик по кнопке 'Далее'")
    def click_order_button(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON_NEXT)

    @allure.step("Клик по финальной кнопке 'Заказать'")
    def click_final_order_button(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderPageLocators.ORDER_BUTTON_FINAL)
        )
        self.driver.execute_script("arguments[0].click();", button)

    @allure.step("Получить сообщение об успешном заказе")
    def get_success_message(self):
        message = self.wait_for_visibility(OrderPageLocators.SUCCESS_MESSAGE)
        return message.text

    @allure.step("Выбрать станцию метро {metro_name}")
    def select_metro(self, metro_name):
        metro_input = self.find_element(OrderPageLocators.METRO_INPUT)
        metro_input.click()
        metro_input.send_keys(Keys.ARROW_DOWN)
        metro_input.send_keys(Keys.ENTER)

    @allure.step("Заполнить форму аренды")
    def fill_rental_form(self, date, period, color, comment):
        self.wait_for_visibility(OrderPageLocators.DATE_INPUT)

        date_input = self.find_element(OrderPageLocators.DATE_INPUT)
        date_input.click()
        date_input.clear()
        date_input.send_keys(date)
        date_input.send_keys(Keys.ESCAPE)

        self.click_element(OrderPageLocators.RENTAL_PERIOD)
        period_locator = (By.XPATH, f"//div[contains(@class, 'Dropdown-option') and text()='{period}']")
        self.click_element(period_locator)

        if color == "black":
            self.click_element(OrderPageLocators.COLOR_BLACK)
        else:
            self.click_element(OrderPageLocators.COLOR_GREY)

        self.send_keys_to_element(OrderPageLocators.COMMENT_INPUT, comment)
        self.click_element(OrderPageLocators.ORDER_BUTTON_FINAL)