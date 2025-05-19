import pytest
from webdriver_factory import WebdriverFactory

@pytest.fixture(params=["chrome", "firefox"], scope="function")  # ❗ scope="function для атомарности проверок"
def driver_init(request):
    browser = request.param
    driver = WebdriverFactory.getWebdriver(browser)
    if driver is None:
        raise RuntimeError(f"Driver could not be initialized for browser: {browser}")

    request.cls.driver = driver
    yield
    driver.quit()

