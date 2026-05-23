import allure
from data.urls import BASE_URL
from pages.main_page import MainPage
from pages.feed_page import FeedPage


@allure.title("Тесты раздела 'Лента заказов'")
class TestFeedPage:


    @allure.step("Проверка увеличения счётчика 'Выполнено за всё время' при создании нового заказа")
    def test_total_orders_counter_increases(self, driver):

        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        main_page.login_user()

        feed_page.open_url(f"{BASE_URL}feed")
        initial_count = feed_page.get_total_orders_count()

        feed_page.click_constructor_button() 
        main_page.add_ingredient_to_constructor()
        main_page.click_create_order_button()
        
        main_page.get_created_order_number()
        main_page.click_close_modal_button()

        main_page.click_order_feed_button()
        new_count = feed_page.get_total_orders_count()

        assert new_count > initial_count


    @allure.step("Проверка увеличения счётчика 'Выполнено за сегодня' при создании нового заказа")
    def test_today_orders_counter_increases(self, driver):

        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        main_page.login_user()

        feed_page.open_url(f"{BASE_URL}feed")
        initial_today_count = feed_page.get_today_orders_count()

        feed_page.click_constructor_button()
        main_page.add_ingredient_to_constructor()
        main_page.click_create_order_button()
        
        main_page.get_created_order_number()
        main_page.click_close_modal_button()

        main_page.click_order_feed_button()
        new_today_count = feed_page.get_today_orders_count()

        assert new_today_count > initial_today_count


    @allure.step("Проверка отображения номера нового заказа в разделе 'В работе'")
    def test_new_order_appears_in_progress_block(self, driver):

        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        main_page.login_user()

        main_page.open_url(BASE_URL)
        main_page.add_ingredient_to_constructor()
        main_page.click_create_order_button()

        created_order_number = main_page.get_created_order_number()
        main_page.click_close_modal_button()
        main_page.click_order_feed_button()
        
        is_displayed = feed_page.is_order_number_in_progress_block(created_order_number)
    
        assert is_displayed is True
