import allure
from seletools.actions import drag_and_drop

from utils.urls import URL
from pages.base_page import BasePage
from locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait


class MainPage(BasePage):
    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open_page(URL.MAIN_PAGE)

    @allure.step("Дождаться загрузки главной страницы")
    def wait_for_page_to_load(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)

    @allure.step("Проверить, что главная открыта")
    def is_main_page_opened(self):
        return self.get_current_url() == URL.MAIN_PAGE

    @allure.step("Кликнуть на Конструктор")
    def click_on_constructor_button(self):
        self.scroll_to_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.wait_for_element_clickable(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Кликнуть на Лента заказов")
    def click_on_feed_button(self):
        self.wait_for_element_hide(MainPageLocators.MODAL_CONTENT_BOX)
        self.click_on_element(MainPageLocators.FEED_BUTTON)

    @allure.step("Кликнуть по ингредиенту")
    def click_on_ingredient(self):
        self.scroll_to_element(MainPageLocators.FLUORESCENT_BUN)
        self.wait_for_element_clickable(MainPageLocators.FLUORESCENT_BUN)
        self.click_on_element(MainPageLocators.FLUORESCENT_BUN)

    @allure.step("Закрыть модальное окно")
    def close_ingredient_modal(self):
        self.click_on_element(MainPageLocators.MODAL_CLOSE_BUTTON)
        self.wait_for_element_hide(MainPageLocators.MODAL_WINDOW, timeout=30)

    @allure.step("Проверить, что модальное окно открыто")
    def is_modal_visible(self):
        return self.is_element_visible(MainPageLocators.MODAL_WINDOW)

    @allure.step("Проверить, что модальное окно закрыто")
    def is_modal_closed(self):
        WebDriverWait(self.driver, 1).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )
        elements = self.driver.find_elements(*MainPageLocators.MODAL_WINDOW)
        if not elements:
            return True
        return not elements[0].is_displayed()
    
    @allure.step("Подождать, пока оверлей исчезнет")
    def wait_for_overlay_close(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)

    @allure.step("Получить значение счётчика ингредиента")
    def get_ingredient_counter(self):
        count = self.get_text_of_element(MainPageLocators.INGREDIENT_COUNTER)
        return int(count)

    @allure.step("Перетащить булку в корзину")
    def drag_ingredient_bun_to_basket(self):
        source = self.wait_for_element_visible(MainPageLocators.FLUORESCENT_BUN)
        target = self.wait_for_element_visible(MainPageLocators.BASKET_LIST)
        self.wait_for_element_clickable(MainPageLocators.FLUORESCENT_BUN)
        
        WebDriverWait(self.driver, 20).until(
            lambda driver: source.is_displayed() and target.is_displayed()
        )
        self.drag_and_drop_element(source, target)

    @allure.step("Оформить заказ")
    def place_order(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY_ANIMATION)
        self.click_on_element(MainPageLocators.ORDER_BUTTON)

    @allure.step("Закрыть модальное окно успешного заказа")
    def close_order_success_modal(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY_ANIMATION)
        self.wait_for_overlay_close()
        self.wait_for_element_visible(MainPageLocators.ORDER_ID)
        self.click_on_element(MainPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step("Получить номер оформленного заказа")
    def get_order_number(self):
        self.wait_for_overlay_close()
        order = self.get_text_of_element(MainPageLocators.ORDER_ID)
        return int(order)