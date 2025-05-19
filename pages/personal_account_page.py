from pages.base_page import BasePageBurger
from locators.personal_account_locators import *
from selenium.webdriver.common.by import By
import allure


class PersonalAccountPage(BasePageBurger):
    orders_story_button = [By.XPATH, orders_story]
    exit_button = [By.CLASS_NAME, exit]

    def __init__(self, driver):
        self.driver = driver

    @allure.title("Нажатие на История Заказов")
    def click_on_order_story_button(self):
        self.driver.find_element(*self.orders_story_button).click()

    @allure.title("Нажатие на кнопку Выйти из Аккаунта")
    def click_on_exit_button(self):
        self.driver.find_element(*self.exit_button).click()


