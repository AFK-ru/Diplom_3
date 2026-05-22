import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait

class MainPage(BasePage):

    @allure.step("Получить текст главного заголовка Конструктора")
    def get_main_title_text(self):

        return self.get_element_text(MainPageLocators.MAIN_TITLE)


    @allure.step("Кликнуть на карточку первого ингредиента (булки)")
    def click_ingredient_card(self):

        if self.driver.name == "firefox":
            self.click_element_for_firefox(MainPageLocators.INGREDIENT_CARD)
        else:
            self.click_element(MainPageLocators.INGREDIENT_CARD)


    @allure.step("Получить значение счётчика ингредиента")
    def get_ingredient_counter_value(self):

        try:
            text_value = self.find_element_visible(MainPageLocators.INGREDIENT_COUNTER, time=3).text
            return int(text_value.strip())
        except Exception:
            return 0


    @allure.step("Добавить ингредиент в заказ с помощью Drag and Drop")
    def add_ingredient_to_constructor(self):

        if self.driver.name == "firefox":
            self.drag_and_drop_for_firefox(MainPageLocators.INGREDIENT_CARD, MainPageLocators.BURGER_CONSTRUCTOR_SECTION)
        else:
            self.drag_and_drop_element(MainPageLocators.INGREDIENT_CARD, MainPageLocators.BURGER_CONSTRUCTOR_SECTION)


    @allure.step("Проверить, отображается ли модальное окно деталей ингредиента")
    def is_ingredient_modal_visible(self):

        try:
            return self.find_element_visible(MainPageLocators.INGREDIENT_MODAL_TITLE).is_displayed()
        except Exception:
            return False


    @allure.step("Получить имя ингредиента внутри модального окна")
    def get_ingredient_name_from_modal(self):

        return self.get_element_text(MainPageLocators.INGREDIENT_MODAL_NAME)


    @allure.step("Закрыть модальное окно кликом по крестику")
    def click_close_modal_button(self):

        self.click_element_for_firefox(MainPageLocators.MODAL_CLOSE_BUTTON)
        self.find_element_invisible(MainPageLocators.ORDER_MODAL)
        

    @allure.step("Проверить, что модальное окно деталей ингредиента закрылось")
    def is_ingredient_modal_invisible(self):

        try:
            return self.find_element_invisible(MainPageLocators.INGREDIENT_MODAL_TITLE)
        except Exception:
            return False


    @allure.step("Кликнуть на кнопку «Оформить заказ»")
    def click_create_order_button(self):

        if self.driver.name == "firefox":
            self.click_element_for_firefox(MainPageLocators.CREATE_ORDER_BUTTON)
        else:
            self.click_element(MainPageLocators.CREATE_ORDER_BUTTON)


    @allure.step("Получить номер созданного заказа из всплывающего окна подтверждения")
    def get_created_order_number(self):

        locator = ("xpath", "/html/body/div/div/section/div[1]/div/h2")
        WebDriverWait(self.driver, 15).until_not(lambda d: d.find_element(*locator).text.strip() == "9999" or d.find_element(*locator).text.strip() == "")
        order_text = self.get_element_text(locator)
        clean_number = "".join(filter(str.isdigit, order_text))
        return clean_number.strip()
    

    @allure.step("Авторизоваться под тестовым пользователем")
    def login_user(self, email="mamkin_tester@yandex.ru", password="qwertyuiop"):

        self.open_url("https://stellarburgers.education-services.ru/login")

        email_field = self.find_element_visible(MainPageLocators.LOGIN_EMAIL_INPUT)
        email_field.clear()
        email_field.send_keys(email)

        pass_field = self.find_element_visible(MainPageLocators.LOGIN_PASSWORD_INPUT)
        pass_field.clear()
        pass_field.send_keys(password)

        if self.driver.name == "firefox":
            self.click_element_for_firefox(MainPageLocators.LOGIN_SUBMIT_BUTTON)
        else:
            self.click_element(MainPageLocators.LOGIN_SUBMIT_BUTTON)

        self.find_element_visible(MainPageLocators.MAIN_TITLE)
