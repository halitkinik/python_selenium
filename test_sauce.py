from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date


class Test_Sauce:
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)

    def teardown_method(self):
        self.driver.quit()

    # ikisi de boş geçildiği zaman
    @pytest.mark.parametrize("userName,password", [("", "")])
    def test_spaceEnter(self, userName, password):
        self.waitForElementVisible((By.ID, "user-name"))
        userNameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, "password"))
        passwordInput = self.driver.find_element(By.ID, "password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(userNameInput, userName)
        action.send_keys_to_element(passwordInput, password)
        action.perform()

        logIn = self.driver.find_element(By.ID, "login-button")
        logIn.click()

        self.driver.save_screenshot(
            f"{self.folderPath}/test-spaceEnter-{userName}-{password}.png")

        errorMassage = self.driver.find_element(
            By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        assert errorMassage.text == "Epic sadface: Username is required"

    # sadece sifre bos geçildiği zaman
    @pytest.mark.parametrize("username,password", [("standard_user", "")])
    def test_spacePassword(self, username, password):
        self.waitForElementVisible((By.ID, "user-name"))
        userNameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, "password"))
        passwordInput = self.driver.find_element(By.ID, "password")
        userNameInput.send_keys(username)
        passwordInput.send_keys(password)

        logIn = self.driver.find_element(By.ID, "login-button")
        logIn.click()

        self.driver.save_screenshot(
            f"{self.folderPath}/test-spacePassword{username}-{password}.png")
        errorMassage = self.driver.find_element(
            By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        assert errorMassage.text == "Epic sadface: Password is required"

    # başarılı giris
    @pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
    def test_success_login(self, username, password):
        self.waitForElementVisible((By.ID, "user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, "password"))
        passwordInput = self.driver.find_element(By.ID, "password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput, username)
        action.send_keys_to_element(passwordInput, password)
        action.perform()

        self.driver.save_screenshot(
            f"{self.folderPath}/test-success-login{username}-{password}.png")

        logIn = self.driver.find_element(By.ID, "login-button")
        logIn.click()

    # icona basma
    @pytest.mark.parametrize("username,password", [("1", "1")])
    def test_icon(self, username, password):
        self.waitForElementVisible((By.ID, "user-name"))
        userNameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, "password"))
        passwordInput = self.driver.find_element(By.ID, "password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(userNameInput, username)
        action.send_keys_to_element(passwordInput, password)
        action.perform()

        logIn = self.driver.find_element(By.ID, "login-button")
        logIn.click()

        self.driver.save_screenshot(f"{self.folderPath}/test-icon.png")

        errorIcon = self.driver.find_element(By.CLASS_NAME, "error-button")
        errorIcon.click()

    # inventory
    @pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
    def test_inventory(self, username, password):
        self.waitForElementVisible((By.ID, "user-name"))
        userNameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, "user-name"))
        passwordInput = self.driver.find_element(By.ID, "password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(userNameInput, username)
        action.send_keys_to_element(passwordInput, password)
        action.perform()

        logIn = self.driver.find_element(By.ID, "login-button")
        logIn.click()

        self.driver.get("https://www.saucedemo.com/inventory.html")
        self.driver.save_screenshot(f"{self.folderPath}/test-inventory.png")

    # ürün sayısı
    @pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
    def test_item_number(self, username, password):
        self.waitForElementVisible((By.ID, "user-name"))
        userNameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, "password"))
        passwordInput = self.driver.find_element(By.ID, "password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(userNameInput, username)
        action.send_keys_to_element(passwordInput, password)
        action.perform()
        logIn = self.driver.find_element(By.ID, "login-button")
        logIn.click()
        itemNumber = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        self.driver.save_screenshot(f"{self.folderPath}/test-item-number.png")
        assert len(itemNumber) == 6

    # çıkış yapma senaryosu
    @pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
    def test_logout(self, username, password):
        self.waitForElementVisible((By.ID, "user-name"))
        userNameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, "password"))
        passwordInput = self.driver.find_element(By.ID, "password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(userNameInput, username)
        action.send_keys_to_element(passwordInput, password)
        action.perform()
        logIn = self.driver.find_element(By.ID, "login-button")
        logIn.click()
        menu = self.driver.find_element(
            By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div/button")
        menu.click()

        logout = self.driver.find_element(
            By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/nav/a[3]")
        self.driver.save_screenshot(f"{self.folderPath}/test-logout.png")
        logout.click

    #ürünleri filtreleme senaryosu
    @pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
    def test_filtert(self, username, password):
        self.waitForElementVisible((By.ID, "user-name"))
        userNameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, "password"))
        passwordInput = self.driver.find_element(By.ID, "password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(userNameInput, username)
        action.send_keys_to_element(passwordInput, password)
        action.perform()
        logIn = self.driver.find_element(By.ID, "login-button")
        logIn.click()
        filtrele = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/span/select")
        filtrele.click()
        filtrele2 = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/span/select/option[2]")
        self.driver.save_screenshot(f"{self.folderPath}/test-filter.png")
        filtrele2.click()

    # sepete ürün ekleme ve sepete gitme senaryosu

    @pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
    def test_add_to_cart(self, username, password):
        self.waitForElementVisible((By.ID, "user-name"))
        userNameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, "password"))
        passwordInput = self.driver.find_element(By.ID, "password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(userNameInput, username)
        action.send_keys_to_element(passwordInput, password)
        action.perform()
        logIn = self.driver.find_element(By.ID, "login-button")
        logIn.click()

        addToCart = self.driver.find_element(
            By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button")
        addToCart.click()
        goToCart = self.driver.find_element(
            By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/a")
        goToCart.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-add-to-cart.png")

    def waitForElementVisible(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            ec.visibility_of_element_located(locator))
