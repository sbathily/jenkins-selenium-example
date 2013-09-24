#!/usr/bin/python
import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class JujuSeleniumTest(unittest.TestCase):

    def setUp(self):
	      self.driver = webdriver.Remote(command_executor='http://192.168.1.216:4444/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX)

    def test_selenium_juju(self):
        driver = self.driver
        driver.get("https://juju.ubuntu.com/")
        self.assertEqual("Ubuntu Juju", driver.title)
        elem = driver.find_element_by_link_text("Install Juju")
	      elem.click()
	      wait = WebDriverWait(self.driver, 10)
	      wait.until(lambda driver: "Install" in driver.title)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
