import os

import pytest
from appium import webdriver as AppiumDriver
from appium.options.android import UiAutomator2Options

# PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
# APP_ROOT = os.path.join(PROJECT_ROOT, 'app')
# OUTPUT_ROOT = os.path.join(PROJECT_ROOT, 'tests', 'output')
APPIUM_PORT = "4723"
APPIUM_HOST = "0.0.0.0"
APPIUM_URL = f'http://{APPIUM_HOST}:{APPIUM_PORT}/wd/hub'

PATH_APP = "/Users/dolgushin_georgii/Downloads/1231.apk"
PLATFORM_NAME = None


def get_options():
    options = UiAutomator2Options()
    options.set_capability("bootstrapPort", "8201")
    options.set_capability("app", PATH_APP)
    options.set_capability("deviceName", "Pixel_4_API_33")
    # options = XCUITestOptions()
    return options


# @pytest.fixture(scope="function", autouse=True)
@pytest.fixture()
def driver(request):
    options = get_options()
    driver = AppiumDriver.Remote(APPIUM_URL, options=options)
    request.cls.driver = driver
    yield
    request.cls.driver.quit()

# Будет выполняться перед каждым тестом
# def pytest_runtest_setup(item):
#     print(f"==============Set up for {item}=========")

# Этот хук позволяет писать свои аргументы
# def pytest_addoption(parser):
#     parser.addoption('--platform_name', default='android', action='store', help="Choose app: --platform_name android or ios ")

# Этот хук позволяет забрать свои аргументы
# def pytest_configure(config):
#     global PLATFORM_NAME
#     PLATFORM_NAME = config.getoption("--platform_name")
