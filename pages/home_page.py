
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base_page import Base_page


class Home_page(Base_page):
    FORM_AUTHENTICATON_LINK=(By.LINK_TEXT,'Form Authentication')
    JAVA_ALERTS_LINK=(By.LINK_TEXT,'JavaScript Alerts')
    INPUTS_LINK=(By.LINK_TEXT,'Inputs')


    def navigate_to_home_page(self):
        self.driver.get('https://the-internet.herokuapp.com/')

    def enter_form_auth_url(self):
        self.wait_and_click_element_by_selector(*self.FORM_AUTHENTICATON_LINK)

    def enter_java_alerts_url(self):
        self.wait_and_click_element_by_selector(*self.JAVA_ALERTS_LINK)

    def enter_inputs_url(self):
        self.wait_and_click_element_by_selector(*self.INPUTS_LINK)




