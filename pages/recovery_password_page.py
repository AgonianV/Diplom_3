
from locators.recovery_password_locators import *
import allure
from pages.base_page import BasePageBurger
from selenium.webdriver.common.by import By
from data import UserData
from urls import *

class RecoveryPasswordPage(BasePageBurger):
    enter_button = [By.CLASS_NAME, login_button]
    email_field = [By.CSS_SELECTOR, email]
    password_field = [By.CSS_SELECTOR, password]
    login_in_recovery_page = [By.XPATH, login_button_registration_page]
    recovery_button = [By.XPATH, recovery_password_button]
    restore_button = [By.CLASS_NAME, restore]
    recover_password_text = [By.CLASS_NAME, recover_text]
    show_password_button = [By.CLASS_NAME, show_password]
    show_password_active = [By.CLASS_NAME, show_password_check]
    password_field_restore_page = [By.CSS_SELECTOR, restore_password_field]
    modal_overlay_x2ZCr = overlay_x2ZCr
    modal_overlay_3534A = overlay__3534A

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Заполнение поля Email')
    def set_email_field(self):
        self.set_field(self.email_field, UserData.email)

    @allure.step('Заполнение поля пароля')
    def set_password_restore_page(self):
        self.set_field(self.password_field_restore_page, UserData.password)

    @allure.step('Нажатие показать Пароль')
    def click_show_password_restore_page(self):
        self.click_on_element(self.show_password_button)

    @allure.step('Ожидание загрузки страницы логина')
    def wait_for_load_login_page(self):
        self.wait_for_load_page(login_page)

    @allure.step('Ожидание загрузки страницы восстановления пароля')
    def wait_for_load_password_recovery_page(self):
        self.wait_for_load_page(forgot_password_page)

    @allure.step('Убрать оверлей _x2ZCr')
    def put_away_overlay_x2ZCr(self):
        self.put_away_overlay(self.modal_overlay_x2ZCr)

    @allure.step('Убрать оверлей _3534A')
    def put_away_overlay_3534A(self):
        self.put_away_overlay(self.modal_overlay_3534A)

    @allure.step('Нажатие на кнопку восстановить пароль')
    def click_recovery_password_button(self):
        self.click_on_element(self.recovery_button)

    @allure.step('Нажатие на кнопку восстановить')
    def click_restore_button(self):
        self.click_on_element(self.restore_button)

    @allure.step('Ожидание появления кнопки восстановить пароль')
    def wait_for_load_recovery_button(self):
        self.wait_element_for_clickable(self.recover_password_text)

    @allure.step('Получение текста их поля паспорт')
    def return_recover_text(self):
        element = self.get_element_from_text(self.recover_password_text)
        return element

    @allure.step('Ищем пароль в поле ввода')
    def find_password_field_restore_page(self):
        element = self.get_field_attribute(self.password_field_restore_page,"value")
        return element



