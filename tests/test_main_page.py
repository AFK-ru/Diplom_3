import allure
from data.urls import BASE_URL
from data.ingredients import DEFAULT_INGREDIENT
from pages.main_page import MainPage
from pages.feed_page import FeedPage


@allure.title("Тесты главной страницы (Конструктор)")
class TestMainPage:


    @allure.step("Проверка перехода по клику на 'Конструктор'")    
    def test_navigation_to_constructor_success(self, driver):

        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        feed_page.open_url(f"{BASE_URL}feed")
        feed_page.click_constructor_button()

        main_title = main_page.get_main_title_text()
        assert main_title == "Соберите бургер"


    @allure.step("Проверка перехода по клику на раздел 'Лента заказов'")
    def test_navigation_to_order_feed_success(self, driver):

        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        main_page.open_url(BASE_URL)
        main_page.click_order_feed_button()

        feed_title = feed_page.get_feed_title_text()
        assert feed_title == "Лента заказов"


    @allure.step("Проверка появления всплывающего окна с деталями при клике на ингредиент")
    def test_click_ingredient_opens_modal_details(self, driver):

        main_page = MainPage(driver)

        main_page.open_url(BASE_URL)
        main_page.click_ingredient_card()

        assert main_page.is_ingredient_modal_visible() is True

        ingredient_name_in_modal = main_page.get_ingredient_name_from_modal()
        assert ingredient_name_in_modal == DEFAULT_INGREDIENT


    @allure.step("Проверка закрытия всплывающего окна кликом по крестику")
    def test_close_ingredient_modal_by_click_cross_button(self, driver):

        main_page = MainPage(driver)

        main_page.open_url(BASE_URL)
        main_page.click_ingredient_card()
        
        main_page.is_ingredient_modal_visible()
        main_page.click_close_modal_button()

        assert main_page.is_ingredient_modal_invisible() is not False


    @allure.step("Проверка увеличения счётчика ингредиента при его добавлении в заказ")
    def test_ingredient_counter_increases_after_drag_and_drop(self, driver):

        main_page = MainPage(driver)

        main_page.open_url(BASE_URL)

        initial_counter = main_page.get_ingredient_counter_value()
        assert initial_counter == 0

        main_page.add_ingredient_to_constructor()

        new_counter = main_page.get_ingredient_counter_value()
        assert new_counter > initial_counter
