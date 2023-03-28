# Python Icinde Selenium Kullanabilmek Icin Yapilmasi Gereken Kurulumlar
# Bu Kurulumlar VSCode Terminal Ekraninda Yada CMD Ekraninda Yapilabilir
# 1 - pip (Sadece Bu Yazilacak)
# 2 - pip install selenium

# Selenium : Kullanicinin Browser da Yaptigi Islemleri Otomatik Hale Getiren Yapidir

# Selenium Paketinin Adi Ile Dosya Adi Ayni Olursa Kod Calistirma Asamasinda
# Otomatik Olarak Dosya Adi Uzerinden Islem Yapmaya Calisacaktir
# Bu Durumu Engellemek Icin
# Selenium Paketinin Adi Ile Dosya Adinin Farkli Olmasi Gerekiyor
# Selenium Paketinin WebDriver Class ini import Ediyoruz
from selenium import webdriver

# 2 Numarada Yer Alan Islemi Yaptiktan Sonra 1 Pencere Hizlica Acilip Kapaniyorsa
# ChromeDriver Paketinin Download Edilmesine Gerek Yok

# Chrome Browser Versiyonuna Gore Linkte Yer Alan Paketi Download Etmek Gerekiyor
# Chrome Browser Versiyonu En Az 111 Ise Gerek Yok
# https://chromedriver.chromium.org/downloads

# Download Edilen Chrome Driver Paketinin 
# Calisilan Uygulama Dahil Edilmesi Asamasinda 
# 1. Yol
# Download Edilen Dosya Icindeki Exe Uzantili Dosyayi
# Calisilan Proje Icine Kopyaliyoruz
# 2. Yol
# Download Edilen Dosya Icindeki Exe Uzantili Dosyayi
# C Surucusu Icine Birakiyoruz
# Birakilan Dosyayinin Yolunu Ve Adini String Veri Tipi Olarak
# driver = webdriver.Chrome()
# Satirindaki () Icine Yaziyoruz
# 3. Yol
# WebDriver Manager Paketi
# pip install webdriver-manager Komut Satirini Kullanarak 
# Web Driver Paketini Yukluyoruz
# Bu Islem Yapildiginda Otomatik Olarak Web Driver Paketinin Yuklenmesini Ve 
# Konfigurasyon Islemlerinin Yapilmasini Saglar

# WebDriverManager Modulu Uzerinden Chrome Modulu Parantezinde
# ChromeDriverManager Class ini import Ediyoruz 
from webdriver_manager.chrome import ChromeDriverManager

# Chrome Browser in Acilirken Hemen Kapanmasini Engellemenin Baska Bir Yolu
# Time Modulunden Sleep Class ini import Etmek
from time import sleep

# Selenium Modulu Icindeki 
# WebDriver Modulu Icinde 
# Common Modulu Icindeki 
# By Modulu Icinde Yer Alan
# By Class ini import Ediyoruz
# By Class i Test Edilecek Web Sitesinde Test Icin 
# Secilmesi Gereken HTML Tag larinin Secilmesi Icin Kullaniliyor
from selenium.webdriver.common.by import By

# WebDriverManager Modulu Uzerinden Chrome Modulu Parantezinde
# ChromeDriverManager Paketinin Icindeki install Fonksiyonu Ile 
# Uygulamanin Calistirildi Bilgisayarda Chrome Driver Paketinin 
# Otomatik Olarak Kurulmasini Dosya Yolunun Ayarlanmasini Ve Calistirilmasini Saglar
# Bu Islemi Degiskene Atama Yaparak Kullanimini Kolay Hale Getiriyoruz
driver = webdriver.Chrome(ChromeDriverManager().install())

# Test Yapilacak Browser i Tam Ekran Olarak Acmak Icin
# Degiskene Atanan Web Driver Paketi 
# Chrome Driver Manager Paketi ve 
# indtall Fonksiyonunun Atandigi Degisken Adi Uzerinden
# Maximize Window Fonksiyonunu Kullaniyoruz
driver.maximize_window()

# Degiskene Atanan Web Driver Paketi 
# Chrome Driver Manager Paketi ve 
# indtall Fonksiyonunun Atandigi Degisken Adi Uzerinden
# Get Fonksiyonuna 
# Test Yapilacak Sitenin URL Bilgisini Tam Olarak Girmek Gerekiyor
driver.get("https://www.google.com")

# Sleep Fonksiyonu Ile 
# Chrome Browser da Acilmak Istenilen Sitenin Acilmasi Icin Sure Taniyoruz
# Acilirken Sonraki Komutun Calismasi Icin 
# Kac Saniye Beklenecegini Belirtiyoruz 
sleep(2)

# Test Islemlerini Yapabilmek Icin Test Isleminin Yapilacagi 
# Web Sitesinde HTML Kodlarini Kullaniyoruz
# Bu Isleme HTML LOCATORS

# Driver Degiskeni Uzerinden Find Element Fonksiyonuna By Modulu Uzerinden
# Web Sitesinde Test Icin Kullanilacak Alana Ait Uniq (Essiz) Olmasi Gerekiyor
# Kullanilacak Alan Adinin Diger Alan Adlarindan Farkli Olmasi Gerekiyor
# ID Bilgisi Name Bilgisi Gibi Alanlar Uniq Alan Olarak Kabul Edilebilir
# Alan Adini ve O Alana Verilen Isim Bilgisini Giriyoruz

# Find Element Fonksiyonu Icinde 
# Ilk Parametre Olarak HMTL Tag Secimi Icin By Class ini Yazdiktan Sonra
# Secilmek Istenilen HTML Tag ini Yaziyoruz
# Ikinci Parametre Olarak Secim Icin Kullanilacak Tag a Uygun Olan Degerin Ozelligini Yaziyoruz
input = driver.find_element(By.NAME,"q")

print(f"input Element : {input}")

# Send Fonksiyonu Icinde
# Browser da Test Icin Acilan Sitede Arama Yaptirilacak Text i Giriyoruz
input.send_keys("kodlamaio")


# Sonra Kullanici Tarafindan Tıklanacak Ara Butonuna Tıklamayi Otomatik Yaptiriyoruz
# Find Element Fonksiyonu Icinde 
# Ilk Parametre Olarak HMTL Tag Secimi Icin By Class ini Yazdiktan Sonra
# Secilmek Istenilen HTML Tag ini Yaziyoruz
# Ikinci Parametre Olarak Secim Icin Kullanilacak Tag a Uygun Olan Degerin Ozelligini Yaziyoruz
searchButton = driver.find_element(By.NAME, "btnK")

print(f"Searh Button : {searchButton}")

# Butona Otomatik Tiklama Isleminden Sonra 2 Saniye Bekliyoruz
sleep(2)

# Send Keys Fonksiyonu Icine Girilen Text i Arama Islemi Yapiyoruz
searchButton.click()
sleep(2)

# Acilan Sitede Arama Isleminin Yapidigi Satirdaki Full Xpath i Seciyoruz
# firstResult = driver.find_element(By.XPATH,"/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a")
firstResult = driver.find_element(By.XPATH,"//*[@id='rso']/div[1]/div/div/div/div/div/div/div[1]/a")
print(f"First Result : {firstResult}")

# Yapilan Arama Isleminden Sonra Siteye Giris Yapiyoruz
firstResult.click()

# Class Adina Gore Bulanan Sonuclari Degiskene Atama Yapiyoruz
# Find Element Fonksiyonu Arama Yapilan Sitede Sadece Buldugu Ilk Sonucu Verir
# Find Elements Fonksiyonu Arama Yapilan Sitede Ayni Turden Kac tane Varsa Hepsini Liste Halinde Verir
listOfCourses = driver.find_elements(By.CLASS_NAME,"course-listing")

# Bulunan Sonucu Yazdiriyoruz
print(f"Kodlamaio Sitesinde Suanda {len(listOfCourses)} Adet Kurs Var")

# Chrome Browser Acilma Asamasinda Iken Hemen Kapanmasini Engelliyoruz
while True:
    continue


# XPATH
# Kullanilacak HTML Tag ina Ulasmak Icin En Kisa Yol
# //*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/a

# FULL XPATH
# HTML TAG ina Ulasmak Icin Kullanilacak Uzun Yol
# /html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/a