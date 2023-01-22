from BDD.Tema_11.base_page import Base_page
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Login_page(Base_page):
    LOGIN_BUTTON = (By.XPATH, '//button[@class="radius"]')
    USER = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')

    def navigate_to_login_page(self):
        self.driver.get('https://the-internet.herokuapp.com/login')

    def introduce_user(self,user_name):
        self.wait_and_send_keys_by_selector(*self.USER,user_name)

    def introduce_password(self,password):
        self.wait_and_send_keys_by_selector(*self.PASSWORD,password)

    def click_login_button(self):
        self.wait_and_click_element_by_selector(*self.LOGIN_BUTTON)

