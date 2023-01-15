import pytest

from pages.welcome_page import WelcomePage


@pytest.mark.usefixtures('driver')
class TestAuthrazation:

    def test_authrization(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.click_btn_allow()
        welcome_page.fill_field_email("Test@test.ru")
        welcome_page.fill_field_password("12314")
