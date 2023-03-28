from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class Test_SauceDemo:
    def test_invalid_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window
        driver.get("https://www.saucedemo.com/")

        sleep(5)
        
        loginUserNameInput = driver.find_element(By.ID,"user-name")
        loginUserPasswordInput = driver.find_element(By.ID,"password")
        
        sleep(2)
        
        loginUserNameInput.send_keys("1")
        loginUserPasswordInput.send_keys("1")
        
        sleep(10)
        
        loginBtn = driver.find_element(By.ID, "login-button")
        loginBtn.click()
        
        sleep(30)

        # Kullanici User Name ve Password Bilgilerini Girdikten Sonra 
        # Girilen Bilgilerde Hata Varsa
        # Hatali Giris Yapildiginda Gorunecek Yaziyi Seciyoruz
        errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        print(errorMessage)

        # Hatali Giris Uyarisini Ekrana Yazdirma Asamasinda
        # Kendimizce Gore Bir Mesaj Yazdirirsak Test Sonucu False Olur
        # Siteyi Olusturan Yazilimcinin Hata Uyarisini Kullanirsak
        # Test Sonucu True Olur

        # Test Sonucu False Olursa 2 Ihtimal Vardir
        # 1. Test Kodlarinda Hata Vardir
        # 2. Siteyi Olusturan Yazilimci Hatali Urun Yapmis Olabilir
        testResult = errorMessage.text == "Incorrect Login"
        print(f"Test Result : {testResult}")
        
        sleep(30)
    
testClass = Test_SauceDemo()
testClass.test_invalid_login()