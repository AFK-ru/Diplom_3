from selenium.webdriver.common.by import By

class FeedPageLocators:

    # Главный заголовок страницы "Лента заказов"
    FEED_TITLE = (By.XPATH, "//h1[contains(@class, 'text_type_main-large') and text()='Лента заказов']")

    # Счетчик "Выполнено за всё время"
    TOTAL_ORDERS_COUNTER = (By.XPATH, "(//p[contains(@class, 'digits-large') or contains(@class, 'number')])[1]")

    # Счетчик "Выполнено за сегодня"
    TODAY_ORDERS_COUNTER = (By.XPATH, "(//p[contains(@class, 'digits-large') or contains(@class, 'number')])[2]")

    # Блок списка заказов "В работе"
    IN_PROGRESS_ORDERS_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]")

    # Карточки заказов в ленте
    ORDER_CARDS = (By.XPATH, "//div[contains(@class, 'OrderHistory_box')]")
