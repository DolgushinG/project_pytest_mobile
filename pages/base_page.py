# class BasePage:
#     def __int__(self, driver):
#         self.driver = driver
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver

    TIME = 10

    def _wait_and_click(self, element):
        # try and catch
        # try:
        element = WebDriverWait(self.driver, timeout=self.TIME).until(EC.element_to_be_clickable(element))
        element.click()
        # WebDriverWait(self.driver,
        #               ignored_exceptions=(NoSuchElementException, StaleElementReferenceException),
        #               timeout=self.TIME).until(EC.element_to_be_clickable(element)).click()
        # except NoSuchElementException:
        # msg = f'Element not found, element: "{element}"'
        # raise NoSuchElementException(msg)
        # except TimeoutException:
        # msg = f'Element not found, element: "{element}"'
        # raise TimeoutException(msg)