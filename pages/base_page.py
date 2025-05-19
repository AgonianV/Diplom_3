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
    order_hystory_button = [By.XPATH, order_history]

    @allure.step('Открываем браузер Chrome')
    def __init__(self,driver):
        self.driver = driver

    @allure.step('нажимаем История Заказов')
    def click_on_order_hystory(self):
        self.driver.find_element(*self.order_hystory_button).click()

    @allure.step('Ожидаем загрузки страницы Лента заказов')
    def wait_for_load_feed_page(self):  # Ожидаем пока главная страница не прогрузится
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be((feed_page)))

    @allure.step('нажимаем Лента Заказов')
    def click_on_lenta(self):
        self.driver.find_element(*self.lenta_button).click()

    @allure.step('нажимаем Конструктор')
    def click_on_costructor(self):
        self.driver.find_element(*self.costructor_button).click()

    @allure.step('нажимаем Личный кабинет')
    def click_on_personal_account_button(self):
        self.driver.find_element(*self.personal_account_button).click()

    @allure.step('Ищем пароль по поле ввода')
    def find_password_field_restore_page(self):
        element = self.driver.find_element(*self.password_field_restore_page)
        value = element.get_attribute("value")
        return value

    @allure.step('нажимаем на показать пароль')
    def click_show_password_restore_page(self):
        self.driver.find_element(*self.show_password_button).click()

    @allure.step('Вводим пароль')
    def set_password_restore_page(self):
        self.driver.find_element(*self.password_field_restore_page).send_keys("555999")

    @allure.step('Получаем пароль из поля ввода')
    def return_recover_text(self):
        element = self.driver.find_element(*self.recover_password_text)
        return element.text

    @allure.step('Нажатие по кнопке Восстановить пароль')
    def click_restore_button(self):  # Нажатие по кнопке "Восстановить пароль"
        self.driver.find_element(*self.restore_button).click()

    @allure.step('Ожидаем загрузки элементов на странице')
    def wait_for_load_element(self, element):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element))

    @allure.step('Ожидаем закрытия элементов на странице')
    def wait_for_close_element(self,element):
        WebDriverWait(self.driver, 5).until(expected_conditions.invisibility_of_element_located(element))

    @allure.step('Нажатие по кнопку Восстановить пароль')
    def click_recovery_password_button(self): # Нажатие по кнопке "Восстановить пароль"
        self.driver.find_element(*self.recovery_button).click()

    @allure.step('Ожидаем зугрузки страницы История заказов')
    def wait_for_load_order_history_page(self):   # Ожидаем пока главная страница не прогрузится
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be((order_story_page)))

    @allure.step('Ожидаем зугрузки главной страницы')
    def wait_for_load_main_page(self):   # Ожидаем пока главная страница не прогрузится
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be((main_page)))

    @allure.step('Ожидаем зугрузки страницы Личный кабинет')
    def wait_for_load_profile_page(self):   # Ожидаем пока главная страница не прогрузится
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be((profile_page)))

    @allure.step('Ожидаем зугрузки страницы Восстановления пароля')
    def wait_for_load_password_recovery_page(self):   # Ожидаем пока главная страница не прогрузится
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be((forgot_password_page)))

    @allure.step('нажатие по кнопку Войти в аккаунт')
    def click_login_button(self):    # Нажатие по кнопке "Войти в аккаунт"
        self.driver.find_element(*self.enter_button).click()

    @allure.step('Ожидаем пока  страница авторизации не прогрузится')
    def wait_for_load_login_page(self):    # Ожидаем пока  страница авторизации не прогрузится
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be((login_page)))

    @allure.step('Заполнение поля Email')
    def set_email_field(self):   # Заполнение поля Email на странице входа
            self.driver.find_element(*self.email_field).send_keys("Denis_kvartych_15_333@yandex.ru")

    @allure.step('Заполнение поля пароль')
    def set_password_field(self):  # Заполнение поля Email на странице входа
        self.driver.find_element(*self.password_field).send_keys("555999")

    @allure.step('Ожидаем пока  страница восстановления пароля не прогрузится')
    def wait_for_load_password_recovery_page(self):    # Ожидаем пока  страница воссатановления пароля не прогрузится
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be((forgot_password_page)))

    @allure.step('Нажатие по кнопке Войти на странице восстановления пароля')
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


