# Py Test Isleminin Yapilacagi Dosya Icinde
# Py Test Confifurasyonu Icin Visual Studio Code Icinde 
# Sol Tarafta Testing Tabina Tiklamak Gerekiyor

# Testing Tabina Tikladiktan Sonra
# Karsimiza 2 Tane Buton Cikacak
# Biz Configure Python Tests Butonuna Tikliyoruz
# Sonra
# Karsimiza Cikan Kucuk Pencerede PyTest Python Framework u Seciyoruz
# Sonra 
# Karsimiza Cikan Kucuk Pencerede
# . Root Directory i Seciyoruz
# Bu Islemi Yaptiktan Sonra Python Test Islemlerinin Yapilmasini Saglayan
# Alt Yapi Olusturulacak

# Eger Hata Verir Ise Hatayi Terminal Ekranini Acitiktan Sonra
# Terminal Sekmesinin Yanindaki Output Sekmesine Tikliyoruz Sonra
# Sekmelerin Sag Tarafinda Olan Acilir Pencereden Python i Seciyoruz
# Cikan Listede Hatalar Yaziyor

# Class Yada Fonksiyonda Isim Degisikligi Yapilirsa
# Yapilan Degisikligi Testing Tabinda Refrest Test e Tiklayarak
# Yapilan Degisikligi Alt Yapidaki Dosyalarda Kaydediyoruz

# Bu Islemler Yapilirken 
# Chrome Browser Otomatik Olarak Sik Sik Calisiyor Ise
# Proje Dosyasinin Basinda Yer Alan Test_ Ibaresini Silmek Gerekiyor

# Class Isimlerinin Basinda
# Test_ Yazmiyorsa Testing Tabinda Gorunmez

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

# PyTest Anotasyonlarini Kullanabilmek Icin Kullanilan Class
import pytest

# Klasor Olusturmak Path Class ini import Ediyoruz
from pathlib import Path

# Yapilacak Islemde Tarih Bilgisi Olmasini Saglar
from datetime import date

class Test_Demo:

    # PyTest (Pyton Test) Icinde
    # Global Islemler Yapabilmek Icin
    # Class Icinde Setup Method Ve 
    # Teardown Method  Olarak 2 Tane Fonksiyon Var

    # Test Isleminin Calisma Sirasi
    # Ilk Olarak Setup Method Calisacak
    # Ikinci Olarak Yazilan Fonksiyonlar
    # Son Olarak Teardown Method Calisacak
    
    # Setup Method (Her Testten Once Cagirilir)
    # Import Edilen Class lari Calistirarak
    # Fonksiyon Icinde Belirtilen Islemlerin Yapilmasini Saglar
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

        # Tarih Bilgisini GG.AA.YYYY Formatinda Yazdirir
        self.folderPath = str(date.today())

        # Klasor Olusturma Isleminde Eger Ayni Isimde Klasor Var Ise
        # Tekrar Olusturmasini Engelliyoruz
        Path(self.folderPath).mkdir(exist_ok=True)
        
    # Teardown Method (Her Testten Sonra Cagirilir)
    # Test Islemi Bittikten Sonra Chrome Browser in Kapanmasini
    # Ve Bellekte Yer Alan Ve Artik Kullanilmayacak Dosyalarin Silinmesini Saglar
    def teardown_method(self):
        self.driver.quit()
    
    # Fonksiyon Isimlerinin Basinda
    # test_ Yazmiyorsa Testing Tabinda Gorunmez

    # Test Icin Kullanilacak Fonksiyonlara test_ Ile Baslamak Gerekiyor

    def test_demoFunction(self):

        # Test Sonucunu Condition (Sarta) Baglamak Icin
        # Assert Keyword unu Kullaniyoruz
        
        # 3A Act Arrange Assert
        text = "Hello"
        assert text == "Hello"
    
    def test_demo2(self):
        assert True
    
    # Calistirilmasi Istenilmeyen Fonksiyonlarda Kullaniyoruz
    # @pytest.mark.skip()

    # Fonksiyonda Kullanilan Parametreler Uzerinden Gonderilen Degerler
    # Kullanilarak Test Yapilmasini Saglar
    @pytest.mark.parametrize("username,password",[("1","1"),("myusername","mypassword")])

    def test_invalid_login(self,username,password):

        # Surekli Tekrar Edilen Element Gorunurlugu Islemini 
        # Fonksiyon Haline Getirdikten Sonra
        # Self Anahtar Kelimesi Uzerinden Cagiriyoruz
        self.waitForElementVisible((By.ID,"user-name"))
        loginUserNameInput = self.driver.find_element(By.ID,"user-name")

        # TimeOut Degiskenine Atanan Degerden Bagimsiz Olarak 
        # Bekleme Suresi Degeri Verebiliyoruz
        self.waitForElementVisible((By.ID,"password"),10)
        loginUserPasswordInput = self.driver.find_element(By.ID,"password")
        
        loginUserNameInput.send_keys(username)
        loginUserPasswordInput.send_keys(password)

        # loginUserNameInput.send_keys("1")
        # loginUserPasswordInput.send_keys("1")
        
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        
        # Yapilan Isleme Ait ScreenShot Bilgisini Belirtilen Dosya Yolunda 
        # Kaydeden Kisinin Kullanici Adi Ve Sifresini Dosya Adi Olarak Kullaniyoruz 
        # Islemi Yapanin Bilgisi Ile Kaydediyoruz
        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-{username}-{password}.png")

        # Test Edilen Sitenin Text Ozelliginde Yer Alan Deger Ile
        # Bizim Girdigimiz Degeri Ayni Olma Durumunu Kontrol Ediyoruz
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"

    # Surekli Tekrar Edilen Element Gorunurlugu Islemini Fonksiyon Haline Getiriyoruz

    # TimeOut Degiskenine Atanan Bekleme Suresi Degeri 
    # Tum Fonksiyonlar Icin Gecerli Oluyor
    # Istenirse Diger Fonksiyonlarda Farkli Bir Bekleme Suresi Degeri Verilebilir
    def waitForElementVisible(self,locator,timeout=5):
        WebDriverWait(self.driver,timeout).until(expected_conditions.visibility_of_element_located(locator))