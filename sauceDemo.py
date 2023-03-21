from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class Source_Demo:

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    sleep(2)

    def userPassword(self):
        userName = self.driver.find_element(By.ID, "user-name")
        password = self.driver.find_element(By.ID, "password")
        sleep(2)
        userName.send_keys(" ")
        password.send_keys(" ")
        sleep(2)
        logIn = self.driver.find_element(By.ID, "login-button")
        logIn.click()
        sleep(3)

        errorMassage = self.driver.find_element(
            By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMassage.text == "Epic sadface: Username is required"
        print(f"TEST SONUCU: {testResult}")

    def justPassword(self):
        userName = self.driver.find_element(By.ID, "user-name")
        password = self.driver.find_element(By.ID, "password")
        sleep(2)
        userName.send_keys("standard_user")
        password.send_keys("")
        sleep(2)
        logIn = self.driver.find_element(By.ID, "login-button")
        logIn.click()
        sleep(3)

        errorMassage = self.driver.find_element(
            By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMassage.text == "Epic sadface: Password is required"
        print(f"TEST SONUCU: {testResult}")

    def locked_out_user(self):
        userName = self.driver.find_element(By.ID, "user-name")
        password = self.driver.find_element(By.ID, "password")
        sleep(2)
        userName.send_keys("locked_out_user")
        password.send_keys("secret_sauce")
        sleep(2)
        logIn = self.driver.find_element(By.ID, "login-button")
        logIn.click()
        sleep(3)

        errorMassage = self.driver.find_element(
            By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMassage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"TEST SONUCU: {testResult}")

    def icon(self):
        userName = self.driver.find_element(By.ID, "user-name")
        password = self.driver.find_element(By.ID, "password")
        sleep(2)
        userName.send_keys("1")
        password.send_keys("1")
        sleep(2)
        logIn = self.driver.find_element(By.ID, "login-button")
        logIn.click()
        sleep(3)
        errorIcon = self.driver.find_element(By.CLASS_NAME, "error-button")
        errorIcon.click()
        sleep(30)

    def inventory(self):
        userName = self.driver.find_element(By.ID, "user-name")
        password = self.driver.find_element(By.ID, "password")
        sleep(2)
        userName.send_keys("standard_user")
        password.send_keys("secret_sauce")
        sleep(2)
        logIn = self.driver.find_element(By.ID, "login-button")
        logIn.click()
        self.driver.get("https://www.saucedemo.com/inventory.html")
        sleep(2)

    def itemNumber(self):
        userName = self.driver.find_element(By.ID, "user-name")
        password = self.driver.find_element(By.ID, "password")
        sleep(2)
        userName.send_keys("standard_user")
        password.send_keys("secret_sauce")
        sleep(2)
        logIn = self.driver.find_element(By.ID, "login-button")
        logIn.click()
        sleep(3)
        urunSayisi = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        print(f"ÜRÜN SAYISI: {len(urunSayisi)}")


sourceDemo = Source_Demo()

sourceDemo.userPassword()
sourceDemo.justPassword()
sourceDemo.locked_out_user()
sourceDemo.icon()
sourceDemo.itemNumber()
sourceDemo.inventory()
