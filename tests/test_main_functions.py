from selenium import webdriver
from pages.feed_page import FeedPage
from urls import *
import pytest
import allure
from conftest import driver_init , login

@pytest.mark.usefixtures("driver_init")
class TestMainFunctions:

    @allure.title("Проверка перехода по клику на «Конструктор»")
    def test_main_page_after_constructor_button(self):
        main = FeedPage(self.driver)
        main.open_page(login_page)
        main.put_away_overlay_x2ZCr()
        main.click_on_costructor()

        assert main.get_current_url() == main_page

    @allure.title("Проверка перехода по клику на «Лента Заказов»")
    def test_feed_page_after_lenta_button(self):
        main = FeedPage(self.driver)
        main.open_page(login_page)
        main.put_away_overlay_x2ZCr()
        main.click_on_lenta()

        assert main.get_current_url() == feed_page

    @allure.title("Проверка если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_info_ingredient_popup(self):

        main = FeedPage(self.driver)
        main.open_page(main_page)
        main.put_away_overlay_x2ZCr()
        main.click_on_ingredient()

        assert main.check_order_popup().is_displayed()

    @allure.title("Проверка, что всплывающее окно закрывается кликом по крестику")
    def test_close_ingredient_popup(self):
        main = FeedPage(self.driver)
        main.open_page(main_page)
        main.put_away_overlay_x2ZCr()

        main.click_on_ingredient()
        main.close_ingredient_popup()
        main.wait_for_close_popup()

        assert not main.check_order_popup().is_displayed()

    @allure.title("Проверка, при добавлении ингредиента в заказ, увеличивается количество данного ингредиента")
    def test_increase_ingredient_counter(self):
        main = FeedPage(self.driver)
        main.open_page(main_page)
        main.put_away_overlay_x2ZCr()
        main.drug_and_drop_ingredient()


        assert main.return_count_ingredient() == '2' # Драг-н-дроп не работает в Фаерфокс, опять же какие ожидания не сделай - он просто не берет ингредиент (Предложили написать явный JS скрипт для решения)

    @allure.title("Проверка, что залогиненный пользователь может оформить заказ")
    def test_auth_user_can_get_order(self, driver_init, login):
        main = FeedPage(driver_init)
        main.open_page(login_page)

        main.wait_order_button()
        main.click_order_button()
        main.wait_load_order_popup()
        assert main.check_order_popup().is_displayed()