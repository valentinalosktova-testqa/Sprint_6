from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import MainPageLocators

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def get_answer_text(self, index):
        question_locator = (By.XPATH, f"//div[@id='accordion__heading-{index}']")
        answer_locator = (By.XPATH, f"//div[@id='accordion__panel-{index}']/p")

        question_element = self.driver.find_element(*question_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", question_element)

        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.element_to_be_clickable(question_locator)).click()

        answer_element = wait.until(EC.visibility_of_element_located(answer_locator))
        return answer_element.text
    
    def click_order_button_top(self):
        self.driver.find_element(*MainPageLocators.ORDER_BUTTON_TOP).click()

    def click_logo_scooter(self):
        self.driver.find_element(*MainPageLocators.LOGO_SCOOTER).click()

    def click_logo_yandex(self):
        self.driver.find_element(*MainPageLocators.LOGO_YANDEX).click()