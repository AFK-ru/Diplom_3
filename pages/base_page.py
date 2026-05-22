import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from locators.header_locators import HeaderLocators

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10


    @allure.step("Открыть страницу по URL: {url}")
    def open_url(self, url):

        self.driver.get(url)


    @allure.step("Ожидать появление элемента в DOM-структуре: {locator}")
    def find_element(self, locator, time=None):

        t = time if time is not None else self.timeout
        return WebDriverWait(self.driver, t).until(EC.presence_of_element_error if hasattr(EC, 'presence_of_element_error') else EC.presence_of_element_located(locator))


    @allure.step("Ожидать, пока элемент станет видимым на экране: {locator}")
    def find_element_visible(self, locator, time=None):

        t = time if time is not None else self.timeout
        return WebDriverWait(self.driver, t).until(EC.visibility_of_element_located(locator))


    @allure.step("Ожидать, пока все элементы списка станут видимыми: {locator}")
    def find_elements_visible(self, locator, time=None):

        t = time if time is not None else self.timeout
        return WebDriverWait(self.driver, t).until(EC.visibility_of_all_elements_located(locator))
    

    @allure.step("Ожидать исчезновения элемента с экрана: {locator}")
    def find_element_invisible(self, locator, time=None):

        t = time if time is not None else self.timeout
        return WebDriverWait(self.driver, t).until(EC.invisibility_of_element_located(locator))


    @allure.step("Кликнуть по элементу для Chrome с локатором: {locator}")
    def click_element(self, locator):

        element = WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator))
        element.click()


    @allure.step("Кликнуть по элементу для Firefox с локатором: {locator}")
    def click_element_for_firefox(self, locator):

        element = WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click();", element)


    @allure.step("Считать видимый текст с элемента: {locator}")
    def get_element_text(self, locator):

        return self.find_element_visible(locator).text


    @allure.step("Перетащить элемент {locator_source} в область {locator_target}")
    def drag_and_drop_element(self, locator_source, locator_target):

        source = self.find_element_visible(locator_source)
        target = self.find_element_visible(locator_target)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()


    @allure.step("Перетащить элемент {locator_source} в область {locator_target} для Firefox")
    def drag_and_drop_for_firefox(self, locator_source, locator_target):

        source = self.find_element_visible(locator_source)
        target = self.find_element_visible(locator_target)
        
        js_script = """
        var src = arguments[0], trg = arguments[1];
        var dataTransfer = new DataTransfer();
        src.dispatchEvent(new DragEvent('dragstart', { bubbles: true, dataTransfer: dataTransfer }));
        trg.dispatchEvent(new DragEvent('drop', { bubbles: true, dataTransfer: dataTransfer }));
        src.dispatchEvent(new DragEvent('dragend', { bubbles: true, dataTransfer: dataTransfer }));
        """
        self.driver.execute_script(js_script, source, target)


    @allure.step("Перейти в раздел «Конструктор» через хедер")
    def click_constructor_button(self):

        if self.driver.name == "firefox":
            self.click_element_for_firefox(HeaderLocators.CONSTRUCTOR_BUTTON)
        else:
            self.click_element(HeaderLocators.CONSTRUCTOR_BUTTON)


    @allure.step("Перейти в раздел «Лента заказов» через хедер")
    def click_order_feed_button(self):

        if self.driver.name == "firefox":
            self.click_element_for_firefox(HeaderLocators.ORDER_FEED_BUTTON)
        else:
            self.click_element(HeaderLocators.ORDER_FEED_BUTTON)
