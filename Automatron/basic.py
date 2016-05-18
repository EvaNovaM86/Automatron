import unittest
# from selenium import common
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from configobj import ConfigObj


# This is a class with basic functions to establish basic actions for navigating the page
class BasicActions(object):
    def __init__(self, config_info):
        self.action = None
        self.config_info = config_info
        self.proxy_url = self.config_info['proxy_url']
        self.username_auth = self.config_info['username_auth']
        self.password_auth = self.config_info['password_auth']
        self.radio_button = None
        self.driver = None
        self.next = None
        self.url_to_get = None

    # https://selenium-python.readthedocs.org/api.html
    # This function allows the other to preform operations on the page
    def set_up(self):
        self.driver = webdriver.Firefox()
        self.action = webdriver.ActionChains(self.driver)

    def test_authenticate(self):
        BasicActions.set_up(self)

        self.driver.get(self.proxy_url)

        username_auth = self.driver.find_element_by_id('username')
        password_auth = self.driver.find_element_by_id('password')

        username_auth.send_keys(self.username_auth)
        password_auth.send_keys(self.password_auth)
        password_auth.send_keys(Keys.RETURN)

    def get_page(self):
        self.url_to_check = self.driver.getCurrentUrl()

    def wait_until(self, element):
        driver = webdriver.Firefox()
        driver.get(self.url_to_check)
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, element)))
        finally:
            driver.quit()

    def move_and_click_perform(self, element):
        self.next = self.driver.find_element_by_name(element)
        self.action.move_to_element(self.next)
        self.action.click(self.next)
        BasicActions.wait_until(self, self.next)
        self.action.perform()

    # Switch to JS alert
    def alert(self):
        self.driver.switch_to.alert.accept()

    # A method to set up a basic forward proxy from the quick service creation
    def test_quick_service_creation_f(self):
        assert isinstance(self.action, webdriver.ActionChains)
        page = self.proxy_url + '/ApplianceWizards.php?view=Quick%20Service%20Creation'
        self.driver.get(page)

        self.move_and_click_perform('serviceWizardOk')
        self.move_and_click_perform('wizSvNameOk')
        self.move_and_click_perform('wizSvAddressOk')
        self.move_and_click_perform('wizSvExtrasOk')

    def tearDown(self):
        self.driver.close()


def main():
    config = '../Automatron/Basic/config'
    config_info = ConfigObj(config)
    basic_actions = BasicActions(config_info)
    basic_actions.test_authenticate()
    basic_actions.test_quick_service_creation_f()
    # basic_actions.tearDown()
    print(config)


main()

if __name__ == '__main__':
    unittest.main()
