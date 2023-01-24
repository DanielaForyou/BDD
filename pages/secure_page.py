
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base_page import Base_page


class Secure_page(Base_page):
    LOGOUT_BUTTON=(By.CLASS_NAME,'icon-signout')
    SUCCES_MESSAGE=(By.CLASS_NAME,'success')

    def navigate_to_secure_page(self):
        self.driver.get('https://the-internet.herokuapp.com/secure')

    def click_logout_button(self):
        self.wait_and_click_element_by_selector(*self.LOGOUT_BUTTON)

    def verify_succes_message(self):
        self.verify_element_is_displayed(*self.SUCCES_MESSAGE)
