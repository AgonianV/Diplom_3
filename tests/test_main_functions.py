from selenium import webdriver
from pages.feed_page import FeedPage
from urls import *
import pytest
import allure
from conftest import driver_init

@pytest.mark.usefixtures("driver_init")
class TestMainFunctions:

    @allure.title("Проверка перехода по клику на «Конструктор»")
    def test_main_page_after_constructor_button(self):
        self.driver.get(login_page)

        main = FeedPage(self.driver)
        self.driver.execute_script("""
                          let overlays = document.querySelectorAll('.Modal_modal_overlay__x2ZCr');
                          overlays.forEach(el => el.remove());
                        """) # Иным способом Firefox перекрывает другие элементы. Пробовал ожидать и тд, не выходит
        main.click_on_costructor()

        assert self.driver.current_url == main_page

    @allure.title("Проверка перехода по клику на «Лента Заказов»")
    def test_feed_page_after_lenta_button(self):
        self.driver.get(login_page)

        main = FeedPage(self.driver)
        self.driver.execute_script("""
                          let overlays = document.querySelectorAll('.Modal_modal_overlay__x2ZCr');
                          overlays.forEach(el => el.remove()); 
                        """) # Иным способом Firefox перекрывает другие элементы. Пробовал ожидать и тд, не выходит
        main.click_on_lenta()

        assert self.driver.current_url == feed_page

    @allure.title("Проверка если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_info_ingredient_popup(self):
        self.driver.get(main_page)

        main = FeedPage(self.driver)
        self.driver.execute_script("""
                                  let overlays = document.querySelectorAll('.Modal_modal_overlay__x2ZCr');
                                  overlays.forEach(el => el.remove());
                                """)   # Иным способом Firefox перекрывает другие элементы. Пробовал ожидать и тд, не выходит
        main.click_on_ingredient()

        assert main.check_order_popup().is_displayed()

    @allure.title("Проверка, что всплывающее окно закрывается кликом по крестику")
    def test_close_ingredient_popup(self):
        self.driver.get(main_page)

        main = FeedPage(self.driver)
        self.driver.execute_script("""
                                  let overlays = document.querySelectorAll('.Modal_modal_overlay__x2ZCr');
                                  overlays.forEach(el => el.remove());
                                """) # Иным способом Firefox перекрывает другие элементы. Пробовал ожидать и тд, не выходит

        main.click_on_ingredient()
        main.close_ingredient_popup()
        main.wait_for_close_element(main.order_popup_user)
        assert not main.check_order_popup().is_displayed()

    @allure.title("Проверка, при добавлении ингредиента в заказ, увеличивается количество данного ингредиента")
    def test_increase_ingredient_counter(self):
        self.driver.get(main_page)

        main = FeedPage(self.driver)
        self.driver.execute_script("""
                          let overlays = document.querySelectorAll('.Modal_modal_overlay__x2ZCr');
                          overlays.forEach(el => el.remove());
                        """) # Иным способом Firefox перекрывает другие элементы. Пробовал ожидать и тд, не выходит
        main.drug_and_drop_ingredient()


        assert main.return_count_ingredient() == '2' # Драг-н-дроп не работает в Фаерфокс, опять же какие ожидания не сделай - он просто не берет ингредиент (Предложили написать явный JS скрипт для решения)

    @allure.title("Проверка, что залогиненный пользователь может оформить заказ")
    def test_auth_user_can_get_order(self):
        self.driver.get(login_page)
        self.driver.execute_script("""
                          let overlays = document.querySelectorAll('.Modal_modal_overlay__x2ZCr');
                          overlays.forEach(el => el.remove());
                        """)
        main = FeedPage(self.driver)
        main.set_email_field()
        main.set_password_field()
        main.click_login_button()
        main.wait_for_load_main_page()

        main.click_login_button()
        assert main.check_order_popup().is_displayed()
