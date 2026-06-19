import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage

class TestOrder:
    @pytest.mark.parametrize("order_data", [
        {"name": "Иван", "surname": "Иванов", "address": "Пушкина 1", "metro": "Лубянка", "phone": "+79998887766",
         "date": "22.06.2026", "period": "сутки", "color": "black", "comment": "Быстрее пожалуйста"},
        {"name": "Петр", "surname": "Петров", "address": "Ленина2", "metro": "Охотный Ряд", "phone": "+79998887755",
         "date": "22.06.2026", "period": "двое суток", "color": "grey", "comment": "Позвоните за час"}
    ])
    def test_order_scooter(self, driver, order_data):
        main_page = MainPage(driver)
        driver.get("https://qa-scooter.praktikum-services.ru/")
        main_page.click_order_button_top()

        order_page = OrderPage(driver)
        order_page.fill_order_form(order_data)
        order_page.click_order_button()

        order_page.fill_rental_form(
            order_data["date"],
            order_data["period"],
            order_data["color"],
            order_data["comment"]
        )
        order_page.click_final_order_button()

        message = order_page.get_success_message()
        assert "Заказ оформлен" in message