from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure
from selenium.webdriver import ActionChains



class BasePageBurger:

    def __init__(self, driver, wait_time=10):
        self.driver = driver
        self.wait_time = wait_time

    @allure.step('Открытие страницы')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Ожидаем пока элемент не станет кликабельным')
    def wait_element_for_clickable(self, element):
        return WebDriverWait(self.driver, self.wait_time).until(EC.element_to_be_clickable(element))

    @allure.title("Ожидаем загрузки заказа в разделе В работе")
    def wait_order_in_work(self, element):
        return WebDriverWait(self.driver, 10).until_not(
            lambda d: d.find_element(*element).text.strip() == "Все текущие заказы готовы!"
        )
    @allure.step('Ожидаем появления элемента')
    def wait_visibility_of_element(self, element):
        return WebDriverWait(self.driver, self.wait_time).until(EC.visibility_of_element_located(element))

    @allure.step('Ожидаем появления заказа')
    def wait_for_load_orders(self, elements,order_number):
        element = [By.XPATH, f"{elements}//p[contains(text(), '{order_number}')]"]
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element))

    @allure.step('Поиск заказа пользователя')
    def find_orders(self,elements,order_number,):
        element = [By.XPATH, f"{elements}//p[contains(text(), '{order_number}')]"]
        element = self.driver.find_element(*element)
        return element.text

    @allure.step('Ожидаем пока элемент пропадет')
    def wait_unvisibility_of_element(self, element):
        return WebDriverWait(self.driver, self.wait_time).until(EC.invisibility_of_element_located(element))


    @allure.step('жидаем пока загрузится страница')
    def wait_for_load_page(self, url):
        return WebDriverWait(self.driver, self.wait_time).until(EC.url_to_be(url))

    @allure.step('Получаем текст из элемента')
    def get_element_from_text(self, element):
        element = self.driver.find_element(*element)
        return element.text

    @allure.step('Находим элемент')
    def get_element(self,element):
        return self.driver.find_element(*element)

    @allure.step('Ожидаем пока определится номер заказа')
    def wait_for_order_number(self, element):
        WebDriverWait(self.driver, 10).until_not(
            lambda d: d.find_element(*element).text.strip() == "9999"
        )
    @allure.step('Заполняем поле')
    def set_field(self, element, text):
        self.driver.find_element(*element).send_keys(text)

    @allure.step('Нажимаем на элемент')
    def click_on_element(self, element):
        self.driver.find_element(*element).click()

    @allure.step('Получаем атрибут элемента')
    def get_field_attribute(self, element, attribute):
        return self.driver.find_element(*element).get_attribute(attribute)

    @allure.step('Получаем нынешний адрес сайта')
    def get_current_url(self):
        return self.driver.current_url

    @allure.title("Драг-н-дроп ингредиента в корзину")
    def drug_and_drop_ingredients(self, ingredient_main_page, burger_bucket):
        ingredient = self.driver.find_element(*ingredient_main_page)
        busket = self.driver.find_element(*burger_bucket)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(ingredient, busket).perform()

    @allure.step('Убираем оверлей')
    def put_away_overlay(self, element):
        self.driver.execute_script(
            f"let overlays = document.querySelectorAll('{element}'); overlays.forEach(el => el.remove());")


