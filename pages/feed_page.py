from pages.base_page import BasePageBurger
from locators.feed_locators import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from urls import *

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
    order_hystory_button = [By.XPATH, order_history]
    order_number_main_page = [By.CLASS_NAME, order_number_main]
    find_order_list = [By.CLASS_NAME, find_order]
    complete_for_all_time = [By.XPATH, complete_all]
    complete_for_today = [By.XPATH, complete_today]
    order_in_work = [By.XPATH, in_work]
    costructor_button = [By.XPATH, costructor]
    lenta_button = [By.XPATH, lenta]
    modal_overlay_x2ZCr = overlay_x2ZCr
    order_button = [By.CLASS_NAME, order_button]
    personal_account_button = [By.XPATH, personal_account]
    find_user_order = user_order
    def __init__(self, driver):
        super().__init__(driver)

    @allure.title("Нажатие на конструктор")
    def click_on_costructor(self):
        self.click_on_element(self.costructor_button)

    @allure.title("Ожидание загрузки кнопки оформить заказ")
    def wait_order_button(self):
        self.wait_element_for_clickable(self.order_button)
    @allure.title("Ожидание появления ингредиента")
    def wait_for_load_first_ingredient(self):
        self.wait_element_for_clickable(self.first_ingredient)
    @allure.title("Нажатие на Лента Заказов")
    def click_on_lenta(self):
        self.click_on_element(self.lenta_button)
    @allure.title("Получаем значение заказа из Заказы в Работе")
    def return_number_completed_orders_in_work(self):
        num = self.get_element_from_text(self.order_in_work)
        return num

    @allure.title("Получаем значение заказа из выполнено за сегодня")
    def return_number_completed_orders_for_today(self):
        num = self.get_element_from_text(self.complete_for_today)
        return num

    @allure.title("Ожидание загрузки элементов в разделе Выполнено за сегодня")
    def wait_for_load_complete_for_today(self):
        self.wait_visibility_of_element(self.complete_for_today)


    @allure.title("Ожидание открытия главной страницы")
    def wait_for_load_main_page(self):
        self.wait_for_load_page(main_page)

    @allure.title("Получаем значение заказа из выполнено за все время")
    def return_number_completed_orders_for_all_time(self):
        num = self.get_element_from_text(self.complete_for_all_time)
        return num

    @allure.step('Убрать оверлей _x2ZCr')
    def put_away_overlay_x2ZCr(self):
        self.put_away_overlay(self.modal_overlay_x2ZCr)

    @allure.step('Ожидание загрузки Попапа')
    def wait_load_order_popup(self):
        self.wait_visibility_of_element(self.order_popup_user)

    @allure.title("Ожидаем загрузки заказов")
    def wait_for_load_order(self, order_number):
        self.wait_for_load_orders(self.find_user_order,order_number)


    @allure.step('Нажатие на История Заказов')
    def click_on_order_hystory(self):
        self.click_on_element(self.order_hystory_button)

    @allure.step('Ожидаем зугрузки страницы История заказов')
    def wait_for_load_order_history_page(self):  # Ожидаем пока главная страница не прогрузится
        self.wait_for_load_page(order_story_page)

    @allure.step('Ожидание загрузки страницы профиля')
    def wait_for_load_profile_page(self):
        self.wait_for_load_page(profile_page)

    @allure.title("Ожидаем присваивания номера заказа")
    def wait_order_number(self):
        self.wait_for_order_number(self.order_number_main_page)

    @allure.title("Ожидаем загрузки заказа в разделе В работе")
    def wait_order_number_in_work(self):
        self.wait_order_in_work(self.order_in_work)

    @allure.title("Находим соответствующий заказ в фиде")
    def find_order_list_page(self, order_number):
        order = self.find_orders(self.find_user_order, order_number)
        return order

    @allure.title("Ожидание загрузки элементов в разделе Выполнено за все время")
    def wait_for_load_complete_for_all_time(self):
        self.wait_visibility_of_element(self.complete_for_all_time)


    @allure.title("Получаем номер заказа на главной странице")
    def return_order_number_main_page(self):
        num = self.get_element_from_text(self.order_number_main_page)
        return num

    @allure.title("Получаем номер заказа на странице Истории заказов")
    def return_order_number_history_page(self):
        num = self.driver.find_element(*self.order_number_main_page)
        return num.text

    @allure.title("Закрываем попап деталки ингредиента")
    def close_ingredient_popup(self):
        self.click_on_element(self.exit_ingredient_popup)


    def wait_for_close_order_popup_user(self):
        self.wait_unvisibility_of_element(self.order_popup_user)

    @allure.step('нажимаем Личный кабинет')
    def click_on_personal_account_button(self):
        self.driver.find_element(*self.personal_account_button).click()

    @allure.title("Проверяем попап заказа")
    def check_order_popup(self):
        popup = self.get_element(self.order_popup_user)
        return popup

    @allure.title("Ожидание страницы фида")
    def wait_for_load_feed_page(self):
        self.wait_for_load_page(feed_page)

    @allure.title("Ожидание закрытия попапа")
    def wait_for_close_popup(self):
        self.wait_unvisibility_of_element(self.order_popup_user)

    @allure.title("Драг-н-дроп ингредиента в корзину")
    def drug_and_drop_ingredient(self):
        self.drug_and_drop_ingredients(self.ingredient_main_page, self.burger_bucket)

    @allure.title("Ожидание появления кнопки закрытия попапа")
    def wait_for_load_exit_ingredient_popup(self):
        self.wait_element_for_clickable(self.exit_ingredient_popup)

    @allure.title("Нажатие на Оформить заказ")
    def click_order_button(self):
        self.click_on_element(self.order_button)
    @allure.title("Нажатие на ингредиент")
    def click_on_ingredient(self):
        self.click_on_element(self.ingredient_main_page)

    @allure.title("Получаем количество ингредиентов добавленных в корзину")
    def return_count_ingredient(self):
        ingredient = self.get_element_from_text(self.ingredient_counter)
        return ingredient

    @allure.title("Проверяем попап")
    def check_popup(self):
        popup = self.get_element(self.popup_check)
        return popup

    @allure.title("Нажимаем на ингредиент")
    def click_on_first_ingredient(self):
        self.click_on_element(self.first_ingredient)

    @allure.title("Нажимаем на кнопку закрыть")
    def click_on_close_button(self):
        self.click_on_element(self.exit_popup_button)