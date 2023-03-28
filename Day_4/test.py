from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class testClass:
    def emptyLoginAlert(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(3)
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(3)
        loginButton = driver.find_element(By.ID, "login-button")
        loginButton.click()
        sleep(3)
        errorMessage = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username is required" 
        print(f"sonuç: {testResult}")
        sleep(5)

    def emptyPasswordAlert(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(3)
        usernameInput = driver.find_element(By.ID, "user-name")
        usernameInput.send_keys(1)
        passwordInput = driver.find_element(By.ID, "password")
        sleep(3)
        loginButton = driver.find_element(By.ID, "login-button")
        loginButton.click()
        sleep(3)
        errorMessage = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(f"sonuç: {testResult}")
        sleep(5)

    def spesificLogin(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(3)
        usernameInput = driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("locked_out_user")
        passwordInput = driver.find_element(By.ID, "password")
        passwordInput.send_keys("secret_sauce")
        loginButton = driver.find_element(By.ID, "login-button")
        loginButton.click()
        sleep(3)
        errorMessage = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"sonuç: {testResult}")
        sleep(150)

    def errorIcon(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")    
        driver.maximize_window()
        sleep(3)
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        loginButton = driver.find_element(By.ID, "login-button")
        loginButton.click()
        sleep(3)
        errorIcon = driver.find_element(By.CLASS_NAME, "error-button")
        errorIcon.click()
        sleep(100)

    def loginInventory(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(3)
        usernameInput = driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("standard_user")   
        passwordInput = driver.find_element(By.ID, "password")
        passwordInput.send_keys("secret_sauce") 
        loginButton = driver.find_element(By.ID, "login-button")
        loginButton.click()
        sleep(3)
        driver.get("https://www.saucedemo.com/inventory.html")
        sleep(100)
        
    def inventoryList(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(3)
        usernameInput = driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("standard_user")   
        passwordInput = driver.find_element(By.ID, "password")
        passwordInput.send_keys("secret_sauce") 
        loginButton = driver.find_element(By.ID, "login-button")
        loginButton.click()
        sleep(3)
        driver.get("https://www.saucedemo.com/inventory.html")
        productList = driver.find_elements(By.CLASS_NAME, "inventory_item") 
        print(f"Toplam Ürün : {len(productList)}")
        sleep(100)

test = testClass()

# test.emptyLoginAlert() 
# test.emptyPasswordAlert()
# test.spesificLogin()
test.errorIcon()
# test.loginInventory()
# test.inventoryList()