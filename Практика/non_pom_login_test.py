import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.common.by import By
import page
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.relative_locator import locate_with


class DemoQA(unittest.TestCase):
    # Sample test case using POM
    def setUp(self):
        firefox_options = Options()
        
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com")

    def test_demoqa_login(self):
        self.driver.find_element(
            By.XPATH, "//*[@class='card mt-4 top-card'][6]").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID, 'login').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID, 'userName').send_keys("testuser")
        self.driver.find_element(By.ID, 'password').send_keys(
            "fxSkcKv^6gRxY@sj_bJDXWuqfGN=RnE+")
        self.driver.find_element(By.ID, 'login').click()
        self.driver.implicitly_wait(5)
        assert "testuser" not in self.driver.page_source, "Not logged!"
        self.driver.find_element(By.ID, 'submit').click()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
