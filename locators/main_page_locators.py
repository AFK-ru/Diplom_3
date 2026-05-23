from selenium.webdriver.common.by import By

class MainPageLocators:

    # Главный заголовок страницы Конструктора "Соберите бургер"
    MAIN_TITLE = (By.XPATH, "//h1[contains(@class, 'text_type_main-large') and text()='Соберите бургер']")

    # Первый ингредиент в списке "Флуоресцентная булка"
    INGREDIENT_CARD = (By.XPATH, "(//section[contains(@class, 'BurgerIngredients_ingredients')]//a)[1]")

    # Счётчик конкретного ингредиента (внутри карточки Флуоресцентной булки)
    INGREDIENT_COUNTER = (By.XPATH, "(//section[contains(@class, 'BurgerIngredients_ingredients')]//a)[1]//p[contains(@class, 'counter')]")

    # Зона конструктора бургера
    BURGER_CONSTRUCTOR_SECTION = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")

    # Кнопка "Оформить заказ"
    CREATE_ORDER_BUTTON = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]//button")

    # Всплывающее окно с номером оформленного заказа
    ORDER_MODAL = (By.XPATH, "//*[contains(@class, 'opened') or contains(@class, 'Modal_modal_opened')]")
    
    # Номер заказа во всплывающем окне ORDER_MODAL
    ORDER_NUMBER_IN_MODAL = (By.XPATH, "//*[contains(@class, 'opened') or contains(@class, 'Modal_modal_opened')]//h2[contains(@class, 'digits')]")

    # Заголовок открытого модального окна деталей ингредиента
    INGREDIENT_MODAL_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")
    
    # Имя ингредиента внутри открытого модального окна
    INGREDIENT_MODAL_NAME = (By.XPATH, "//h2[text()='Детали ингредиента']/following-sibling::p")
    
    # Кнопка-крестик для закрытия модального окна деталей
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")

    # Блок авторизации (Email, Пароль, кнопка "Войти")
    LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")
