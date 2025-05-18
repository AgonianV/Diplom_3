from pages.base_page import BasePageBurger
from urls import *
from locators.personal_account_locators import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import *
import allure


class PersonalAccountPage(BasePageBurger):
    orders_story_button = [By.XPATH, orders_story]
    exit_button = [By.CLASS_NAME, exit]

    def __init__(self, driver):
        self.driver = driver

    def click_on_order_story_button(self):
        self.driver.find_element(*self.orders_story_button).click()

    def click_on_exit_button(self):
        self.driver.find_element(*self.exit_button).click()


