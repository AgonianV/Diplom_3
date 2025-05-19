from pages.base_page import BasePageBurger
from locators.feed_locators import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import allure


class FeedPage(BasePageBurger):
    first_ingredient = [By.XPATH, ingredient]
    exit_popup_button = [By.XPATH, exit_popup]
    exit_ingredient_popup = [By.XPATH, exit_popup_ingredient]
    popup_check = [By.CLASS_NAME, popup]
    ingredient_main_page = [By.CLASS_NAME, ingredient_main]
    burger_bucket = [By.CLASS_NAME, busket]
    ingredient_counter = [By.CLASS_NAME, counter]
    order_popup_user = [By.CLASS_NAME, order_popup]
    order_number_main_page = [By.CLASS_NAME, order_number_main]
    find_order_list = [By.CLASS_NAME, find_order]
    complete_for_all_time = [By.XPATH, complete_all]
    complete_for_today = [By.XPATH, complete_today]
    order_in_work = [By.XPATH, in_work]

    def __init__(self, driver):
        self.driver = driver

    @allure.title("Получаем значение заказа из Заказы в Работе")
    def return_number_completed_orders_in_work(self):
        num = self.driver.find_element(*self.order_in_work)
        return num.text

    @allure.title("Получаем значение заказа из выполнено за сегодня")
    def return_number_completed_orders_for_today(self):
        num = self.driver.find_element(*self.complete_for_today)
        return num.text

    @allure.title("Получаем значение заказа из выполнено за все время")
    def return_number_completed_orders_for_all_time(self):
        num = self.driver.find_element(*self.complete_for_all_time)
        return num.text

    @allure.title("Ожидаем загрузки заказов")
    def wait_for_load_orders(self, order_number):
        element = [By.XPATH, f"//div[contains(@class, 'OrderHistory_textBox__3lgbs')]//p[contains(text(), '{order_number}')]"]
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element))

    @allure.title("Ожидаем присваивания номера заказа")
    def wait_order_number(self):
        WebDriverWait(self.driver, 10).until_not(
            lambda d: d.find_element(*self.order_number_main_page).text.strip() == "9999"
        )

    @allure.title("Ожидаем загрузки заказа в разделе В работе")
    def wait_order_number_in_work(self):
        WebDriverWait(self.driver, 10).until_not(
            lambda d: d.find_element(*self.order_in_work).text.strip() == "Все текущие заказы готовы!"
        )

    @allure.title("Находим соответствующий заказ в фиде")
    def find_order_list_page(self, order_number):
        order = self.driver.find_element(By.XPATH,
    f"//div[contains(@class, 'OrderHistory_textBox__3lgbs')]//p[contains(text(), '{order_number}')]")
        return order.text

    @allure.title("Получаем номер заказа на главной странице")
    def return_order_number_main_page(self):
        num = self.driver.find_element(*self.order_number_main_page)
        return num.text

    @allure.title("Получаем номер заказа на странице Истории заказов")
    def return_order_number_history_page(self):
        num = self.driver.find_element(*self.order_number_main_page)
        return num.text

    @allure.title("Закрываем попап деталки ингредиента")
    def close_ingredient_popup(self):
        self.driver.find_element(*self.exit_ingredient_popup).click()

    @allure.title("Проверяем попап заказа")
    def check_order_popup(self):
        popup = self.driver.find_element(*self.order_popup_user)
        return popup

    @allure.title("Драг-н-дроп ингредиента в корзину")
    def drug_and_drop_ingredient(self):
        ingredient = self.driver.find_element(*self.ingredient_main_page)
        busket = self.driver.find_element(*self.burger_bucket)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(ingredient, busket).perform()

    @allure.title("Нажатие на ингредиент")
    def click_on_ingredient(self):
        self.driver.find_element(*self.ingredient_main_page).click()

    @allure.title("Получаем количество ингредиентов добавленных в корзину")
    def return_count_ingredient(self):
        ingredient = self.driver.find_element(*self.ingredient_counter)
        return ingredient.text

    @allure.title("Проверяем попап")
    def check_popup(self):
        popup = self.driver.find_element(*self.popup_check)
        return popup

    @allure.title("Нажимаем на ингредиент")
    def click_on_first_ingredient(self):
        self.driver.find_element(*self.first_ingredient).click()

    @allure.title("Нажимаем на кнопку закрыть")
    def click_on_close_button(self):
        self.driver.find_element(*self.exit_popup_button).click()