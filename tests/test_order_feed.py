import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.order_page import OrderPage
from pages.main_page import MainPage
from locators import OrderPageLocators, MainPageLocators

@allure.epic("Лента заказов")
@allure.feature("Счётчики и отображение заказов")
class TestOrdersFeed:

    @allure.title("Счётчики 'Выполнено за всё время' и 'за сегодня' увеличиваются после заказа")
    @allure.description(
        "Проверить, что при оформлении заказа счётчики на странице 'Лента заказов' увеличиваются"
    )
    @pytest.mark.parametrize('counter_type', ['total', 'today'])
    def test_upgrade_counter_orders(self, driver, login_user, counter_type):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.wait_for_page_to_load()
        main_page.click_on_feed_button()
        
        # Получаем значение счетчика в зависимости от типа
        if counter_type == 'total':
            prev_counter = order_page.get_total_orders_count()
        else:  # today
            prev_counter = order_page.get_today_orders_count()
            
        main_page.click_on_constructor_button()
        main_page.drag_ingredient_bun_to_basket()
        main_page.place_order()
        main_page.wait_for_element_visible(MainPageLocators.ORDER_ID)
        main_page.wait_for_overlay_close()
        main_page.close_order_success_modal()
        main_page.wait_for_element_hide(MainPageLocators.ORDER_ID)
        main_page.click_on_feed_button()
        
        wait = WebDriverWait(driver, 30)
        
        if counter_type == 'total':
            # Явно ждем, пока счетчик total изменится
            wait.until(
                lambda d: order_page.get_total_orders_count() != prev_counter
            )
            new_counter = order_page.get_total_orders_count()
        else:  # today
            # Явно ждем, пока счетчик today изменится
            wait.until(
                lambda d: order_page.get_today_orders_count() != prev_counter
            )
            new_counter = order_page.get_today_orders_count()
            
        assert new_counter > prev_counter

    @allure.title("Номер заказа появляется в разделе 'В работе'")
    @allure.description(
        "Проверить, что после оформления заказа его номер отображается в блоке 'В работе' на странице 'Лента заказов'"
    )
    def test_visible_order_number_in_progress(self, driver, login_user):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.wait_for_page_to_load()
        main_page.drag_ingredient_bun_to_basket()
        main_page.place_order()
        main_page.wait_for_element_visible(MainPageLocators.ORDER_ID)
        main_page.wait_for_overlay_close()
        order_number = main_page.get_order_number()
        main_page.close_order_success_modal()
        main_page.wait_for_element_hide(MainPageLocators.ORDER_ID)
        main_page.click_on_feed_button()
        order_page.wait_for_order_page_to_load()

        
        wait = WebDriverWait(driver, 40)
        # Ждем, пока номер заказа появится в разделе "В работе"
        wait.until(
            lambda d: order_number in order_page.get_order_number_in_progress_orders()
        )

        order_in_progress = order_page.get_order_number_in_progress_orders()
        assert order_number in order_in_progress