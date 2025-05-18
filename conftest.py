import pytest
from selenium import webdriver
from webdriver_factory import WebdriverFactory  # адаптируй под свой путь

@pytest.fixture(params=["chrome", "firefox"], scope="function")  # ❗ scope="function"
def driver_init(request):
    browser = request.param
    driver = WebdriverFactory.getWebdriver(browser)
    if driver is None:
        raise RuntimeError(f"Driver could not be initialized for browser: {browser}")

    request.cls.driver = driver  # привязываем к классу
    yield
    driver.quit()