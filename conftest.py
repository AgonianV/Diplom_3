import pytest
from pages.login_page import LoginPage
from urls import *
from selenium import webdriver




@pytest.fixture(params=['chrome', 'firefox'])
def driver_init(request):
    browser = None

    if request.param == 'chrome':
        browser = webdriver.Chrome()
    elif request.param == 'firefox':
        browser = webdriver.Firefox()


    yield browser
    browser.quit()


@pytest.fixture(scope='function')
def login(driver_init):
    user = LoginPage(driver_init)
    user.open_page(login_page)
    user.login_user()