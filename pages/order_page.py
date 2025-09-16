import allure

from utils.urls import URL
from pages.base_page import BasePage
from locators import OrderPageLocators


class OrderPage(BasePage):
    @allure.step("Открыть страницу Лента заказов")
    def open_order_page(self):
        self.open_page(URL.ORDER_PAGE)

    @allure.step("Проверить, что открыта страница Лента заказов")
    def is_order_page_opened(self):
        return self.get_current_url() == URL.ORDER_PAGE

    @allure.step("Подождать, пока оверлей исчезнет")
    def wait_for_overlay_close(self):
        self.wait_for_element_hide(OrderPageLocators.OVERLAY, timeout=30)

    @allure.step("Получить количество заказов Выполнено за всё время")
    def get_total_orders_count(self):
        self.wait_for_overlay_close()
        count = self.get_text_of_element(OrderPageLocators.TOTAL_ORDERS)
        return int(count)

    @allure.step("Получить количество заказов Выполнено за сегодня")
    def get_today_orders_count(self):
        self.wait_for_overlay_close()
        count = self.get_text_of_element(OrderPageLocators.TODAY_ORDERS)
        return int(count)

    @allure.step("Подождать появления заказа в разделе В работе")
    def wait_for_orders_in_progress(self):
        self.wait_for_attribute(OrderPageLocators.IN_PROGRESS_ORDERS, 'class', 'text text_type_digits-default mb-2')

    @allure.step("Получить все номера заказов в разделе В работе")
    def get_order_number_in_progress_orders(self):
        """Получить список всех номеров заказов в разделе 'В работе'"""
        self.wait_for_overlay_close()
        
        order_elements = self.driver.find_elements(*OrderPageLocators.IN_PROGRESS_ORDERS)
        order_numbers = []
        
        if order_elements:
            for element in order_elements:
                text = element.text.strip()
                # Проверяем, что текст является числом
                if text.isdigit():
                    order_numbers.append(int(text))
        
        return order_numbers

    @allure.step("Дождаться загрузки страницы Лента заказов")
    def wait_for_order_page_to_load(self, timeout=30):
        """Ожидание загрузки страницы ленты заказов"""
    # Просто ждем появления счетчиков
        self.wait_for_element_visible(OrderPageLocators.TOTAL_ORDERS, timeout=timeout)