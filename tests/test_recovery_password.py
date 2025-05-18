from selenium import webdriver
from pages.base_page import BasePageBurger
from urls import *
import pytest
import allure
from conftest import driver_init


@pytest.mark.usefixtures("driver_init")
class TestPassRecovery:

    def test_enter_in_pass_recovery_page(self):
        self.driver.get(login_page)

        recover = BasePageBurger(self.driver)
        recover.wait_for_load_login_page()
        self.driver.execute_script("""
          let overlays = document.querySelectorAll('.Modal_modal_overlay__x2ZCr');
          overlays.forEach(el => el.remove());
        """)
        recover.click_recovery_password_button()
        recover.wait_for_load_password_recovery_page()

        assert self.driver.current_url == forgot_password_page

    def test_set_email_with_restore(self):
        self.driver.get(forgot_password_page)
        recover = BasePageBurger(self.driver)
        recover.wait_for_load_password_recovery_page()
        recover.set_email_field()
        self.driver.execute_script("""
                  let overlays = document.querySelectorAll('.Modal_modal_overlay__x2ZCr');
                  overlays.forEach(el => el.remove());
                """)
        self.driver.execute_script("""
                          let overlays = document.querySelectorAll('.Modal_modal__loading__3534A');
                          overlays.forEach(el => el.remove());
                        """)
        recover.click_restore_button()
        recover.wait_for_load_element(recover.recover_password_text)

        assert recover.return_recover_text() == "Пароль"


    def test_show_password_in_recovery_page(self):
        self.driver.get(forgot_password_page)
        recover = BasePageBurger(self.driver)
        recover.wait_for_load_password_recovery_page()
        recover.set_email_field()
        self.driver.execute_script("""
                  let overlays = document.querySelectorAll('.Modal_modal_overlay__x2ZCr');
                  overlays.forEach(el => el.remove());
                """)
        self.driver.execute_script("""
                          let overlays = document.querySelectorAll('.Modal_modal__loading__3534A');
                          overlays.forEach(el => el.remove());
                        """)
        recover.click_restore_button()
        recover.wait_for_load_element(recover.recover_password_text)

        recover.set_password_restore_page()
        recover.click_show_password_restore_page()


        assert recover.find_password_field_restore_page() == "555999"