# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from constants import globalConstants

class TestIcon():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(ChromeDriverManager().install())
    self.driver.get(globalConstants.url)
    self.driver.maximize_window()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()

  @pytest.mark.parametrize("username,password",[("1","1")])
  def test_icon(self,username,password):

    usernameInput = self.driver.find_element(By.ID, globalConstants.userNameID)
    self.waitForElementVisible((By.CSS_SELECTOR, "*[data-test=\"username\"]"))
    passwordInput = self.driver.find_element(By.ID, globalConstants.passwordID)
    self.waitForElementVisible((By.CSS_SELECTOR, "*[data-test=\"password\"]"))

    action = ActionChains(self.driver)
    action.send_keys_to_element(usernameInput,username)
    action.send_keys_to_element(passwordInput,password)

    logIn = self.driver.find_element(By.ID, globalConstants.logIn)
    logIn.click()

    icon = self.driver.find_element(By.CSS_SELECTOR, globalConstants.icon)
    icon.click()
  
  
  def waitForElementVisible(self,locator,timeout = 5):
    WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

  