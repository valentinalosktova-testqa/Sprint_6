from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys


class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_order_form(self, data):
        # Ждём загрузки формы (появление поля "Имя")
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located(OrderPageLocators.NAME_INPUT))

        self.driver.find_element(*OrderPageLocators.NAME_INPUT).send_keys(data["name"])
        self.driver.find_element(*OrderPageLocators.SURNAME_INPUT).send_keys(data["surname"])
        self.driver.find_element(*OrderPageLocators.ADDRESS_INPUT).send_keys(data["address"])
        self.select_metro(data["metro"])
        self.driver.find_element(*OrderPageLocators.PHONE_INPUT).send_keys(data["phone"])

    def click_order_button(self):
        self.driver.find_element(*OrderPageLocators.ORDER_BUTTON_NEXT).click()

    def click_final_order_button(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderPageLocators.ORDER_BUTTON_FINAL)
        )
        self.driver.execute_script("arguments[0].click();", button)

    def get_success_message(self):
        wait = WebDriverWait(self.driver, 5)
        message = wait.until(EC.visibility_of_element_located(OrderPageLocators.SUCCESS_MESSAGE))
        return message.text 
   
    def select_metro(self, metro_name):
    # Кликаем по полю метро
        metro_input = self.driver.find_element(*OrderPageLocators.METRO_INPUT)
        metro_input.click()

    # Нажимаем стрелку вниз, чтобы открыть список
        metro_input.send_keys(Keys.ARROW_DOWN)

    # Нажимаем Enter, чтобы выбрать первую станцию
        metro_input.send_keys(Keys.ENTER)

        
    def fill_rental_form(self, date, period, color, comment):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(OrderPageLocators.DATE_INPUT))

        date_input = self.driver.find_element(*OrderPageLocators.DATE_INPUT)
        date_input.click()
        date_input.clear()
        date_input.send_keys(date)

    # Закрываем календарь (нажимаем ESC)
        date_input.send_keys(Keys.ESCAPE)

    # Теперь кликаем по "Срок аренды"
        self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD).click()
        self.driver.find_element(By.XPATH, f"//div[contains(@class, 'Dropdown-option') and text()='{period}']").click()
    
        if color == "black":
            self.driver.find_element(*OrderPageLocators.COLOR_BLACK).click()
        else:
            self.driver.find_element(*OrderPageLocators.COLOR_GREY).click()
    
        self.driver.find_element(*OrderPageLocators.COMMENT_INPUT).send_keys(comment)
        self.driver.find_element(*OrderPageLocators.ORDER_BUTTON_FINAL).click()


    def confirm_order(self):
        wait = WebDriverWait(self.driver, 10)
        confirm_button = wait.until(EC.element_to_be_clickable(OrderPageLocators.CONFIRM_BUTTON))
        self.driver.execute_script("arguments[0].click();", confirm_button)