from selenium import webdriver
from pages.feed_page import FeedPage
from urls import *
import pytest
import allure
from conftest import driver_init , login


class TestFeedFunctions:


    @allure.title("Проверка открытия всплывающего окна заказа с деталями в фиде")
    def test_info_order_popup(self, driver_init):
        main = FeedPage(driver_init)
        main.open_page(main_page)
        main.put_away_overlay_x2ZCr()
        main.click_on_lenta()
        main.wait_for_load_feed_page()
        main.wait_for_load_first_ingredient()
        main.click_on_first_ingredient()

        assert main.check_popup().is_displayed()

    @allure.title("Проверка заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_order_in_story_and_list_same(self, driver_init, login): # Драг-н-дроп не отрабатывает в Firefox

        main = FeedPage(driver_init)

        main.drug_and_drop_ingredient()
        main.click_order_button() # сделать заказ

        main.wait_for_load_exit_ingredient_popup()
        main.wait_order_number()

        order_number_main = main.return_order_number_main_page()
        order_number = f"#0{order_number_main}"

        main.close_ingredient_popup()
        main.wait_for_close_order_popup_user()

        main.click_on_personal_account_button()
        main.wait_for_load_profile_page()
        main.click_on_order_hystory()
        main.wait_for_load_order_history_page()
        main.wait_for_load_order(order_number)

        main.open_page(feed_page)
        main.wait_for_load_feed_page()
        main.wait_for_load_order(order_number)

        assert order_number == main.find_order_list_page(order_number)

    @allure.title("Проверка, что при создании нового заказа счётчик Выполнено за всё время увеличивается")
    def test_increase_completed_for_all_time(self, driver_init, login):

        main = FeedPage(driver_init)

        main.open_page(feed_page)
        main.wait_for_load_feed_page()
        main.wait_for_load_complete_for_all_time()
        first_order_num = main.return_number_completed_orders_for_all_time()

        main.open_page(main_page)
        main.wait_for_load_main_page()
        main.drug_and_drop_ingredient()
        main.click_order_button()  # сделать заказ

        main.wait_for_load_exit_ingredient_popup()
        main.wait_order_number()
        main.close_ingredient_popup()
        main.wait_for_close_order_popup_user()

        main.open_page(feed_page)
        main.wait_for_load_feed_page()
        main.wait_for_load_complete_for_all_time()
        second_order_num = main.return_number_completed_orders_for_all_time()
        assert int(first_order_num) < int(second_order_num)

    @allure.title("Проверка, что при создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_increase_completed_for_today(self, driver_init, login):

        main = FeedPage(driver_init)

        main.open_page(feed_page)
        main.wait_for_load_feed_page()
        main.wait_for_load_complete_for_today()
        first_order_num = main.return_number_completed_orders_for_today()

        main.open_page(main_page)
        main.wait_for_load_main_page()
        main.drug_and_drop_ingredient()
        main.click_order_button()  # сделать заказ

        main.wait_for_load_exit_ingredient_popup()
        main.wait_order_number()
        main.close_ingredient_popup()
        main.wait_for_close_order_popup_user()

        main.open_page(feed_page)
        main.wait_for_load_feed_page()
        main.wait_for_load_complete_for_today()
        second_order_num = main.return_number_completed_orders_for_today()
        assert int(first_order_num) < int(second_order_num) # тут проблема в том, что на момент проверки после 00:00 счетчик на сайте начал уменьшаться а не увеличиваться

    @allure.title("Проверка, что при создании нового заказа его номер появляется в разделе В работе")
    def test_order_in_work(self, driver_init, login):

        main = FeedPage(driver_init)

        main.drug_and_drop_ingredient()
        main.click_order_button() # сделать заказ

        main.wait_for_load_exit_ingredient_popup()
        main.wait_order_number()

        order_number_main = main.return_order_number_main_page()
        order_number = f"0{order_number_main}"

        main.close_ingredient_popup()
        main.wait_for_close_order_popup_user()

        main.open_page(feed_page)
        main.wait_for_load_feed_page()
        main.wait_for_load_order(order_number)
        main.wait_order_number_in_work()
        order_in_work = main.return_number_completed_orders_in_work()


        assert order_number == order_in_work