import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PageAuth(unittest.TestCase):

    def browserSetUp(self):
        self.driver = webdriver.Firefox()

    def auth_page(self):
        driver = self.driver
        driver.get("https://eve-r/manage/Login.php")
        # self.assertIn("Python", driver.title)
        elem = driver.find_element_by_id('username')
        elem.send_keys("admin")
        elem = driver.find_element_by_id('password')
        elem.send_keys("admin")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()