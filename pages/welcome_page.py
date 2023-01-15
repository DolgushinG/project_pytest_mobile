from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class WelcomePage(BasePage):

    # ANDROID
    EMAIL = (AppiumBy.XPATH, "(//android.widget.EditText)[1]")
    PASSWORD = (AppiumBy.XPATH, "(//android.widget.EditText)[2]")
    BTN_ALLOW = (AppiumBy.XPATH, "(//*[contains(@text, 'Allow')])[2]")

    def fill_field_email(self, text: str) -> None:
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.EMAIL))
        self.driver.find_element(*self.EMAIL).send_keys(text)

    def fill_field_password(self, text: str) -> None:
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.PASSWORD))
        self.driver.find_element(*self.PASSWORD).send_keys(text)

    def click_btn_allow(self) -> None:
        self._wait_and_click(self.BTN_ALLOW)
