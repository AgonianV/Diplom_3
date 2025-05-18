from pages.base_page import BasePageBurger
from urls import *
from locators.feed_locators import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import *
import allure


class FeedPage(BasePageBurger):
    first_ingredient = [By.XPATH, ingredient]
    exit_popup_button = [By.XPATH, exit_popup]
    popup_check = [By.CLASS_NAME, popup]
    ingredient_main_page = [By.CLASS_NAME, ingredient_main]
    burger_bucket = [By.CLASS_NAME, busket]
    ingredient_counter = [By.CLASS_NAME, counter]
    order_popup_user = [By.CLASS_NAME, order_popup]

    def __init__(self, driver):
        self.driver = driver

    def check_order_popup(self):
        popup = self.driver.find_element(*self.order_popup_user)
        return popup
    def drug_and_drop_ingredient(self):
        ingredient = self.driver.find_element(*self.ingredient_main_page)
        busket = self.driver.find_element(*self.burger_bucket)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(ingredient, busket).perform()

    def return_count_ingredient(self):
        ingredient = self.driver.find_element(*self.ingredient_counter)
        return ingredient.text
    def check_popup(self):
        popup = self.driver.find_element(*self.popup_check)
        return popup

    def click_on_first_ingredient(self):
        self.driver.find_element(*self.first_ingredient).click()

    def click_on_close_button(self):
        self.driver.find_element(*self.exit_popup_button).click()