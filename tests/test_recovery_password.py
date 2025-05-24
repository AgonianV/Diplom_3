from selenium import webdriver
from pages.recovery_password_page import RecoveryPasswordPage
from urls import *
import pytest
import allure
from conftest import driver_init



class TestPassRecovery:

    @allure.title("Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_enter_in_pass_recovery_page(self, driver_init):
        recover = RecoveryPasswordPage(driver_init)
        recover.open_page(login_page)
        recover.wait_for_load_login_page()
        recover.put_away_overlay_x2ZCr()
        recover.click_recovery_password_button()
        recover.wait_for_load_password_recovery_page()

        assert recover.get_current_url() == forgot_password_page

    @allure.title("Проверка ввода почты и клик по кнопке «Восстановить»")
    def test_set_email_with_restore(self, driver_init):
        recover = RecoveryPasswordPage(driver_init)
        recover.open_page(forgot_password_page)
        recover.wait_for_load_password_recovery_page()
        recover.set_email_field()

        recover.put_away_overlay_x2ZCr()
        recover.put_away_overlay_3534A()

        recover.click_restore_button()
        recover.wait_for_load_recovery_button()

        assert recover.return_recover_text() == "Пароль"

    @allure.title("Проверка, что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    def test_show_password_in_recovery_page(self, driver_init):
        recover = RecoveryPasswordPage(driver_init)
        recover.open_page(forgot_password_page)
        recover.wait_for_load_password_recovery_page()
        recover.set_email_field()

        recover.put_away_overlay_x2ZCr()
        recover.put_away_overlay_3534A()

        recover.click_restore_button()
        recover.wait_for_load_recovery_button()

        recover.set_password_restore_page()
        recover.click_show_password_restore_page()


        assert recover.find_password_field_restore_page() == "555999"