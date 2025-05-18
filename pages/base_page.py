from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import *
import allure
from urls import *



class BasePageBurger:
    enter_button = [By.CLASS_NAME, login_button]
    email_field = [By.CSS_SELECTOR, email]
    password_field = [By.CSS_SELECTOR, password]
    login_in_recovery_page = [By.XPATH, login_button_registration_page]
    recovery_button = [By.XPATH, recovery_password_button]
    firefox_modal_wait = [By.CLASS_NAME, firefox_modal]
    restore_button =  [By.CLASS_NAME, restore]
    recover_password_text = [By.CLASS_NAME, recover_text]
    show_password_button = [By.CLASS_NAME, show_password]
    show_password_active = [By.CLASS_NAME, show_password_check]
    password_field_restore_page = [By.CSS_SELECTOR, restore_password_field]
    personal_account_button = [By.XPATH, personal_account]
    costructor_button = [By.XPATH, costructor]
    lenta_button = [By.XPATH, lenta]
    def __init__(self,driver):
        self.driver = driver

    def wait_for_load_feed_page(self):  # Ожидаем пока главная страница не прогрузится
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be((feed_page)))
    def click_on_lenta(self):
        self.driver.find_element(*self.lenta_button).click()
    def click_on_costructor(self):
        self.driver.find_element(*self.costructor_button).click()
    def click_on_personal_account_button(self):
        self.driver.find_element(*self.personal_account_button).click()
    def find_password_field_restore_page(self):
        element = self.driver.find_element(*self.password_field_restore_page)
        value = element.get_attribute("value")
        return value

    def click_show_password_restore_page(self):
        self.driver.find_element(*self.show_password_button).click()
    def set_password_restore_page(self):
        self.driver.find_element(*self.password_field_restore_page).send_keys("555999")
    def return_recover_text(self):
        element = self.driver.find_element(*self.recover_password_text)
        return element.text

    def click_restore_button(self):  # Нажатие по кнопке "Восстановить пароль"
        self.driver.find_element(*self.restore_button).click()
    def wait_for_load_element(self, element):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element))

    def wait_for_close_element(self,element):
        WebDriverWait(self.driver, 5).until(expected_conditions.invisibility_of_element_located(element))
    def click_recovery_password_button(self): # Нажатие по кнопке "Восстановить пароль"
        self.driver.find_element(*self.recovery_button).click()

    def wait_for_load_main_page(self):   # Ожидаем пока главная страница не прогрузится
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be((main_page)))

    def wait_for_load_profile_page(self):   # Ожидаем пока главная страница не прогрузится
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be((profile_page)))

    def wait_for_load_password_recovery_page(self):   # Ожидаем пока главная страница не прогрузится
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be((forgot_password_page)))

    def click_login_button(self):    # Нажатие по кнопке "Войти в аккаунт"
        self.driver.find_element(*self.enter_button).click()

    def wait_for_load_login_page(self):    # Ожидаем пока  страница авторизации не прогрузится
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be((login_page)))

    def set_email_field(self):   # Заполнение поля Email на странице входа
            self.driver.find_element(*self.email_field).send_keys("Denis_kvartych_15_333@yandex.ru")

    def set_password_field(self):  # Заполнение поля Email на странице входа
        self.driver.find_element(*self.password_field).send_keys("555999")

    def wait_for_load_password_recovery_page(self):    # Ожидаем пока  страница воссатановления пароля не прогрузится
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be((forgot_password_page)))

    def click_login_password_recovery_page(self):    # Нажатие по кнопке "Войти" на странице восстановления пароля
        self.driver.find_element(*self.login_in_recovery_page).click()


    def entrance_in_personal_account(self):
        self.wait_for_load_login_page()
        self.driver.execute_script("""
                  let overlays = document.querySelectorAll('.Modal_modal_overlay__x2ZCr');
                  overlays.forEach(el => el.remove());
                """)
        self.set_email_field()
        self.set_password_field()
        self.click_login_button()
        self.wait_for_load_main_page()
        self.click_on_personal_account_button()
        self.wait_for_load_profile_page()


