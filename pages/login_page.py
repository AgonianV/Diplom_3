from locators.login_locators import *
import allure
from pages.base_page import BasePageBurger
from selenium.webdriver.common.by import By
from data import UserData
from urls import *

class LoginPage(BasePageBurger):
    enter_button = [By.CLASS_NAME, login_button]
    email_field = [By.CSS_SELECTOR, email]
    password_field = [By.CSS_SELECTOR, password]
    personal_account_button = [By.XPATH, personal_account]
    modal_overlay_x2ZCr = overlay_x2ZCr
    orders_story_button = [By.XPATH, orders_story]
    exit_button = [By.CLASS_NAME, exit]
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Заполнение поля Email')
    def set_email_field(self):
        self.set_field(self.email_field, UserData.email)

    @allure.step('Заполнение поля пароля')
    def set_password_field(self):
        self.set_field(self.password_field, UserData.password)


    @allure.step('Ожидание загрузки страницы логина')
    def wait_for_load_login_page(self):
        self.wait_for_load_page(login_page)


    @allure.step('Ожидание загрузки главной страницы')
    def wait_for_load_main_page(self):
        self.wait_for_load_page(main_page)

    @allure.step('Ожидание загрузки страницы профиля')
    def wait_for_load_profile_page(self):
        self.wait_for_load_page(profile_page)
    @allure.step('Убрать оверлей _x2ZCr')
    def put_away_overlay_x2ZCr(self):
        self.put_away_overlay(self.modal_overlay_x2ZCr)


    def click_login_button(self):
        self.click_on_element(self.enter_button)

    def click_on_personal_account_button(self):
        self.click_on_element(self.personal_account_button)


    def click_on_order_story_button(self):
        self.click_on_element(self.orders_story_button)


    def click_on_exit_button(self):
        self.click_on_element(self.exit_button)
    def entrance_in_personal_account(self):
        self.wait_for_load_login_page()
        self.put_away_overlay_x2ZCr()
        self.set_email_field()
        self.set_password_field()
        self.click_login_button()
        self.wait_for_load_main_page()
        self.click_on_personal_account_button()
        self.wait_for_load_profile_page()

    def login_user(self):
        self.wait_for_load_login_page()
        self.put_away_overlay_x2ZCr()
        self.set_email_field()
        self.set_password_field()
        self.click_login_button()
        self.wait_for_load_main_page()