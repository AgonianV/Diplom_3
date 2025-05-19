from selenium import webdriver
from pages.base_page import BasePageBurger
from pages.personal_account_page import PersonalAccountPage
from urls import *
import pytest
import allure
from conftest import driver_init



@pytest.mark.usefixtures("driver_init")
class TestUserPersonalAccount:

    @allure.title("Проверка перехода по клику на «Личный кабинет»")
    def test_entrance_in_personal_account(self):
        self.driver.get(login_page)
        user = BasePageBurger(self.driver)
        user.entrance_in_personal_account()

        assert self.driver.current_url == profile_page

    @allure.title("Проверка перехода в раздел «История заказов»")
    def test_entrance_in_order_story(self):
        self.driver.get(login_page)
        user = PersonalAccountPage(self.driver)
        user.entrance_in_personal_account()
        user.click_on_order_story_button()
        assert self.driver.current_url == order_story_page

    @allure.title("Проверка выхода из аккаунта")
    def test_logout_from_personal_account(self):
        self.driver.get(login_page)
        user = PersonalAccountPage(self.driver)
        user.entrance_in_personal_account()
        user.click_on_exit_button()

        user.wait_for_load_login_page()
        assert self.driver.current_url == login_page