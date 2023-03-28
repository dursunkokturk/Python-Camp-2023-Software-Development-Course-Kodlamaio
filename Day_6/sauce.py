from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from constants import globalConstants

# Web Driver Wait Class ini Kullanarak
# Site Acilma Suresini Ve Veri Gonderme Gibi Islemler Yapilirken
# Bekleme Surelerini Duzenlemeye Yardimci Oluyor
from selenium.webdriver.support.wait import WebDriverWait

# Belirtilen Sureyi Beklerken Hangi Sarta Gore Beklenecegini Belirtiyoruz
# Yani HTML Elementine Gonderilen Deger Ekranda Gorunene Kadar Bekletebiliyoruz
# Yada Belitilen HTML Elementi Ekranda Gorunene Kadar Bekletebiliyoruz
from selenium.webdriver.support import expected_conditions

# Site Acilma Suresi Valid Login Invalid Login Gibi Islemleri Sirasiyla Yapmak Icin
# ActionChains Class ini Kullanarak Yapilacak Islemleri Zincir Haline Getiriyoruz
from selenium.webdriver.common.action_chains import ActionChains

class Test_SauceDemo:
    def test_invalid_login(self):

        # WebDriverWait Fonksiyonu Icinde
        # Aranan HTML Elementini Bulana Kadar
        # Maximum 5 Saniye olacak Sekilde Bekleme Islemini Duzenliyoruz

        # Ilk Parametre Bekleme Isleminin Uygulanacagi Driver Degiskenine Atanan Islem
        # Ikinci Parametre Maximum Bekleme Suresi

        # Until Fonksiyonu Icinde Bekleme Sartinin Class i Uzerinden
        # visibility_of_element_located Fonksiyonunu Cagiriyoruz
        # visibility_of_element_located Fonksiyonu Icinde Tuple Veri Tipi Seklinde
        # Elementin Nasil Bulunacagini Ve Elementin Adini Belirtiyoruz
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        loginUserNameInput = self.driver.find_element(By.ID,"user-name")

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        loginUserPasswordInput = self.driver.find_element(By.ID,"password")
        
        loginUserNameInput.send_keys("1")
        loginUserPasswordInput.send_keys("1")
        
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        
        
        # Kullanici User Name ve Password Bilgilerini Girdikten Sonra 
        # Girilen Bilgilerde Hata Varsa
        # Hatali Giris Yapildiginda Gorunecek Yaziyi Seciyoruz
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        print(errorMessage)

        # Hatali Giris Uyarisini Ekrana Yazdirma Asamasinda
        # Kendimizce Gore Bir Mesaj Yazdirirsak Test Sonucu False Olur
        # Siteyi Olusturan Yazilimcinin Hata Uyarisini Kullanirsak
        # Test Sonucu True Olur

        # Test Sonucu False Olursa 2 Ihtimal Vardir
        # 1. Test Kodlarinda Hata Vardir
        # 2. Siteyi Olusturan Yazilimci Hatali Urun Yapmis Olabilir
        testResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"Test Result : {testResult}")
        
    def test_valid_login(self):
        
        self.driver.get(globalConstants.URL)

        # Aranan HTML Elementini Bulana Kadar
        # Maximum 5 Saniye olacak Sekilde Bekle
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        loginUserNameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        loginUserPasswordInput = self.driver.find_element(By.ID,"password")
        
        

        # Zindir Olusturma Islemini Self Parametresi Uzerinden
        # Driver Degiskenine Atanan Islem Kullanilacak
        actions = ActionChains(self.driver)

        # send_keys_to_element Fonksiyonu Icinde
        # Ilk Kisim Deger Gonderilecek Element
        # Ikici Kisim Gonderilecek Deger 
        actions.send_keys_to_element(loginUserNameInput,"standard-user")
        actions.send_keys_to_element(loginUserPasswordInput,"secret-sauce")

        # Olusturulan Zincir Yapisinin Calismasi Icin
        # Perform Fonksiyonunu Kullaniyoruz
        actions.perform()
        
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()

        # Exexute Script Fonksiyonu Icinde
        # Test Icin Acilan Sitede JavaScript Kodu Kullanilarak 
        # Kullanicinin Gorebilecegi Sekilde 
        # Yapilacak Islemi Belirtiyoruz
        self.driver.execute_script("window.scrollTo(0,500)")

testClass = Test_SauceDemo()
testClass.test_invalid_login()
testClass.test_valid_login()