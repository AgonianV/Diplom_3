
from pages.login_page import LoginPage
from urls import *
import pytest
import allure
from conftest import driver_init



class TestUserPersonalAccount:

    @allure.title("Проверка перехода по клику на «Личный кабинет»")
    def test_entrance_in_personal_account(self, driver_init):
        user = LoginPage(driver_init)
        user.open_page(login_page)
        user.entrance_in_personal_account()

        assert user.get_current_url() == profile_page

    @allure.title("Проверка перехода в раздел «История заказов»")
    def test_entrance_in_order_story(self, driver_init):
        user = LoginPage(driver_init)
        user.open_page(login_page)
        user.entrance_in_personal_account()
        user.click_on_order_story_button()

        assert user.get_current_url() == order_story_page

    @allure.title("Проверка выхода из аккаунта")
    def test_logout_from_personal_account(self, driver_init):
        user = LoginPage(driver_init)
        user.open_page(login_page)
        user.entrance_in_personal_account()
        user.click_on_exit_button()
        user.wait_for_load_login_page()

        assert user.get_current_url() == login_page
