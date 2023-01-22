from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class Browser():
	driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
	driver.implicitly_wait(10)
	driver.set_page_load_timeout(10)
	driver.maximize_window()
	driver.delete_all_cookies()

	def close(self):
		self.driver.delete_all_cookies()
		self.driver.close()