from selenium.webdriver.common.by import By

class HeaderLocators:
        
    # Кнопка перехода в раздел «Конструктор»
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText')][text()='Конструктор']")
    
    # Кнопка перехода в раздел «Лента заказов»
    ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText')][text()='Лента Заказов']")
    
    # Логотип Stellar Burgers в центре шапки
    HEADER_LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")
    
    # Кнопка «Личный кабинет»
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText')][text()='Личный Кабинет']")
