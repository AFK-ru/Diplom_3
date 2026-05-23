import allure
from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FeedPage(BasePage):

    @allure.step("Получить текст заголовка страницы ленты заказов")
    def get_feed_title_text(self):

        return self.get_element_text(FeedPageLocators.FEED_TITLE)


    @allure.step("Получить значение счётчика «Выполнено за всё время»")
    def get_total_orders_count(self):

        text_value = self.get_element_text(FeedPageLocators.TOTAL_ORDERS_COUNTER)
        return int(text_value.strip())


    @allure.step("Получить значение счётчика «Выполнено за сегодня»")
    def get_today_orders_count(self):

        text_value = self.get_element_text(FeedPageLocators.TODAY_ORDERS_COUNTER)
        return int(text_value.strip())


    @allure.step("Получить список номеров заказов, находящихся «В работе»")
    def get_in_progress_orders_numbers(self):

        locator = ("xpath", "/html/body/div/div/main/div/div/div/div[1]/ul[2]/li")
        elements = self.find_elements_visible(locator, time=15)
        return [element.text.strip() for element in elements if element.text.strip()]


    @allure.step("Проверить, появился ли номер заказа {order_number} в блоке «В работе»")
    def is_order_number_in_progress_block(self, order_number):

        self.find_element_visible(FeedPageLocators.FEED_TITLE, time=15)
        locator = FeedPageLocators.IN_PROGRESS_ORDERS_LIST
        expected_number_with_zero = "0" + str(order_number).strip()
        return WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(locator, expected_number_with_zero))
    