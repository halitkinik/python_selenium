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

url = "https://www.saucedemo.com/"
userNameID ="user-name"
passwordID = "password"
logIn = "login-button"
icon = ".fa-times"
kullaniciAdi = "standard_user"
sifre = "secret_sauce"