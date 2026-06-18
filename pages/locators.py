from selenium.webdriver.common.by import By

class MainPageLocators:
    # Верхняя кнопка "Заказать"
    ORDER_BUTTON_TOP = (By.XPATH, "(//button[text()='Заказать'])[1]")

    # Нижняя кнопка "Заказать"
    ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[text()='Заказать'])[2]")

     # Вопрос по индексу (0, 1, 2...)
    QUESTION = (By.XPATH, "//div[@id='accordion_heading-{}']")

    # Ответ по индексу (0, 1, 2...)
    ANSWER = (By.XPATH, "//div[@id='accordion_panel-{}']/p")

    LOGO_SCOOTER = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter__3lsAR')]")
    LOGO_YANDEX = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex__3TSOI')]")

class OrderPageLocators:
    # Поле "Имя"
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    
    # Поле "Фамилия"
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    
    # Поле "Адрес"
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    
    # Поле "Станция метро"
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    
    # Поле "Телефон"
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")

    # Кнопка "Далее" в форме
    ORDER_BUTTON_NEXT = (By.XPATH, "//button[contains(text(), 'Далее')]")

    # Вторая форма "Про аренду"
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.XPATH, "//div[contains(@class, 'Dropdown-control')]")
    RENTAL_OPTION = (By.XPATH, "//div[contains(@class, 'Dropdown-option')]")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON_FINAL = (By.XPATH, "//div[contains(@class, 'Order_Buttons__1xGrp')]//button[text()='Заказать']")

    CONFIRM_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Modal__YZ-d3')]//button[text()='Да']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader__3FDaJ') and contains(text(), 'Заказ оформлен')]")
