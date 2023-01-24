
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base_page import Base_page


class Login_page(Base_page):
    LOGIN_BUTTON = (By.XPATH, '//button[@class="radius"]')
    USER = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    MESSAGE = (By.ID, 'flash')

    def navigate_to_login_page(self):
        self.driver.get('https://the-internet.herokuapp.com/login')

    def introduce_user(self,username):
        self.wait_and_send_keys_by_selector(*self.USER,username)

    def introduce_password(self,password):
        self.wait_and_send_keys_by_selector(*self.PASSWORD,password)

    def click_login_button(self):
        self.wait_and_click_element_by_selector(*self.LOGIN_BUTTON)

    def verify_if_login_button_is_displayed(self):
        self.verify_element_is_displayed(*self.LOGIN_BUTTON)

    def verify_text_message(self,expected):
        actual_text= self.driver.find_element(*self.MESSAGE).text.replace("\n","").replace("×","")
        assert expected==actual_text, "Error message is invalid"

