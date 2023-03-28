# Dosyada Yapilacak Islemleri Calistirme Testi Yapmak Icin
# Ekrana Basit Bir Yazi Yazdirmak Gerekiyor
print("Dosyada Islem Yapilabilirse Asagisaki Yazi Ekranda Yazilir")
print("kodlamaio")

print("")





# Degisken Tanimlama Ve Degiskene Deger Atama Islemi
# Degiskene Atanan Deger String Tipi Deger
title = "Tasit Kredisi"

# Degiskene Atanan Degeri Yazdirma Islemi
print("Title Degiskenine Atanan Deger")
print(title)
print("Title Degiskenine Atanan Degerin Veri Tipi")
print(type(title))
print("")

print("Degiskene Atanan Degere Ulasmak Icin Istenildigi Zaman Istenildi Kadar Sayida Degisken Adini Kullanma")
print(title)
print(title)

print("")

print("Title Degiskenine Atanan Degeri Degistirme Isleminden Sonra Alinan Sonuc")
title = "Ihtiyac Kredisi"
print(title)

print("")





# Data Types
# int 
# String 
# Float
# Decimal
# Double
# bool
# boolean

# Degiskene Atanan Deger int Tipinde
maturity = 36
print("Maturity Degiskenine Atanan Deger")
print(maturity)
print("Maturity Degiskenine Atanan Degerin Veri Tipi")
print(type(maturity))

print("")

# Degiskene Atanan Deger int Tipinde Ama String Tipinde Kullaniliyor
#maturity = "36"





# Float - Decimal - Double Data
print("Mount Pay Degiskenine Atanan Deger")
monthPay = 200.50
print(monthPay)
print("Maturity Degiskenine Atanan Degerin Veri Tipi")
print(type(monthPay))

print("")





# bool , boolean -> True (Dogru) yada False (Yanlis) Sonuclar Verir
increase = True
increase = False





# Mathematical Operators (Matematiksel Operatorler)
# +
print("5 + 5 = ")
print(5 + 5)
print("")

print("Maturity Degiskenine Atanan Deger Ile 12 Rakaminin Toplami")
print(maturity + 12)
print("")


extraMaturity = 6
print("Maturity Degiskenine Atanan Deger Ile Extra Maturity Degiskenine Atanan Degerin Toplami")
print(maturity + extraMaturity)
print("")

print("36 + 6 = ")
print(36 + 6)
print("")





# -
print("5 - 5 = ")
print(5 - 5)
print("")

print("Maturity Degiskenine Atanan Deger Ile 12 Rakaminin Farki")
print(maturity - 12)
print("")

extraMaturity = 6
print("Maturity Degiskenine Atanan Deger Ile Extra Maturity Degiskenine Atanan Degerin Farki")
print(maturity - extraMaturity)
print("")
print("36 - 6 = ")
print(36 - 6)

# *
print("5 * 5 = ")
print(5 * 5)
print("")

print("Maturity Degiskenine Atanan Deger Ile 12 Rakaminin Carpimi")
print(maturity * 12)
print("")

extraMaturity = 6
print("Maturity Degiskenine Atanan Deger Ile Extra Maturity Degiskenine Atanan Degerin Farki")
print(maturity * extraMaturity)
print("")

print("36 * 6 = ")
print(36 * 6)
print("")

# /
print("5 / 5 = ")
print(5 / 5)
print("")

print("Maturity Degiskenine Atanan Deger Ile 12 Rakaminin Bolumu")
print(maturity / 12)
print("")

extraMaturity = 6
print("Maturity Degiskenine Atanan Deger Ile Extra Maturity Degiskenine Atanan Degerin Bolumu")
print(maturity / extraMaturity)
print("")

print("36 / 6 = ")
print(36 / 6)
print("")

newMaturity = maturity / 2
print("Maturity Degeri / 2 Isleminin Sonucu New Maturity Degerini Verecek")
print(newMaturity)
print("")

price = 100
print("Price / 2 Islemi Ile Indirimli Fiyat Hesaplama Isleminin Sonucu")
decreasePrice = price - 20
print(decreasePrice)
print("")




# mod % operator
print("10 % 2 = ")
print(10 % 2)
print("")

print("Maturity Degiskenine Atanan Degerin 5 Ile Bolumunden Kalan = ")
print(maturity % 5)
print("")

print("Maturity Degiskenine Atanan Degerin Extra Maturity Degiskenine Atanan Degere Bolumunden Kalan = ")
print(maturity % extraMaturity)
print("")
print("30 % 10 = ")
print(30 % 10)
print("")




# Mantiksal (Karsilastirma) Operatorler
print("1 == 1 Isleminin Sonucu = ")
print(1 == 1)
print("")

print("1 == 2 Isleminin Sonucu = ")
print(1 == 2)
print("")

print("1 > 2 Isleminin Sonucu = ")
print(1 > 2)
print("")

print("3 > 1 Isleminin Sonucu = ")
print(3 > 1)
print("")

print("1 > 1 Isleminin Sonucu = ")
print(1 > 1)
print("")

print("1 >= 1 Isleminin Sonucu = ")
print(1 >= 1)
print("")

print("1 < 2 Isleminin Sonucu = ")
print(1 < 2)
print("")

print("1 < 3 Isleminin Sonucu = ")
print(1 < 3)
print("")

print("1 < 1 Isleminin Sonucu = ")
print(1 < 1)
print("")

print("1 <= 1 Isleminin Sonucu = ")
print(1 <= 1)
print("")

print("1 != 1 Isleminin Sonucu = ")
print(1 != 1)
print("")

print("1 != 2 Isleminin Sonucu = ")
print(1 != 2)
print("")





# or
# or Keyword u Kullanilirken Karsilastirma Yapilan Degerlerden 
# Herhangi birinde TRUE Sonucunu Olursa Islem Sonucu TRUE Olarak Cikar
print("1 > 2 or 5 > 2 Isleminin Sonucu = ")
print(1 > 2 or 5 > 2)
print("")

# and Keyword u Kullanilirken Karsilastirma Yapilan Degerlerin 
# Her Ikisinin De Islem Sonucu TRUE Olursa Islem Sonucu TRUE Olarak Cikar
print("1 > 2 and 5 > 2 Isleminin Sonucu = ")
print(1 > 2 and 5 > 2)
print("")

print("1 > 2 and 5 > 2 and 3 > 2 Isleminin Sonucu = ")
print(1 > 2 and 5 > 2 and 3 > 2)

# or and keywords
print("1 > 2 or 5 > 2 and 3 > 2 Isleminin Sonucu = ")
print(1 > 2 or 5 > 2 and 3 > 2)
print("")

print("2 > 1 or 1 > 2 and 3 > 2 Isleminin Sonucu = ")
print(2 > 1 or 1 > 2 and 3 > 2)
print("")





# karar yapilari
# if else

number1 = 15
number2 = 10

print("if Dongusu Kullanilarak 15 > 10 Degerlerinin Buyuklugunun Karsilastirilmasi Islemi")
# Python Dilinde Blok Kullanarak Kod Yazma Isleminde
# Blok Olusturmak Icin if Sartinin Bulundugu Kod Satirinin Sonuna : Isareti Konulduktan Sonra
# Bir Alt Satira Iniyoruz
if number1 > number2:    
    # Bir Alt Satirda Otomatik Olarak Mouse Imleci Iceriye Girmedi Ise 
    # Klavyedeki Tab Tusuna 1 Kez Basarak Mouse Imlecinin Iceriye Girmesini Saglamak Gerekiyor
    # Mouse Imleci Iceriye Girdikten Sonra Yazilan Kodlar Blok Icinde Gecerli Oluyor
    print("Number1 Number2 dan Daha Buyuk")

# Yazilan Kodlarin Blok Icinde Gecerli Olmasini Engellemek Icin 
# Yazilan Satirin En Bastan Baslamasi Gerekiyor
print("If Blogunun Disinda Kalan Satirdaki Kodlar Her Zaman Calisir")
print("")



number1 = 10
number2 = 15

print("if Dongusu Kullanilarak 10 < 15 Degerlerinin Karsilastirilmasi Islemi")
if number1 < number2:
    print("Number1 Number2 den Daha Kucuk")

print("")





number1 = 10
number2 = 15

print("if Else Dongusu Kullanilarak 10 < 15 Degerlerinin Karsilastirilmasi Islemi")
if number1 < number2:
    print("Dongude if Kisminda 10 < 15 Degerlerinin Karsilastirilmasi Isleminin Sonucu")
    print("Number1 Number2 dan Daha Kucuk")
else:
    print("Dongude else Kisminda 10 > 15 Degerlerinin Karsilastirilmasi Isleminin Sonucu")
    print("Number1 Number2 dan Daha Buyuk")
print("")




number1 = 10
number2 = 15

# if elif else Dongusunde Herhangi Bir Blok Icindeki Sart Saglandi Ise 
# Geriye Kalan Bloklardaki Sartlara Bakilmaz
print("if Elif Else Dongusu Icinde 10 < 15  - 10 == 15 - 10 > 15 Degerlerinin Karsilastirilmasi Islemi")
if number1 < number2:
    print("Number1 Number2 dan Daha Kucuk")
elif number1 == number2:
    print("Iki Sayi Esittir")
else:
    print("Number1 Number2 dan Daha Buyuk")

print("")





number1 = 10
number2 = 15

# if Bloklari Alt Alta Yazilarak Bile Birden Fazla Kullanilsa Bile 
# Her Blok Birbirinden Bagimsiz Yapida Olduklari Icin Kontrol Edilir
# Ve Bloklar Icindeki Islemler Yapilir
print("if if Else Dongusu Icinde 10 < 15  - 10 == 15 - 10 > 15 Degerlerinin Karsilastirilmasi Islemi")
if number1 < number2:
    print("Number1 Number2 dan Daha Kucuk")
if number1 == number2:
    print("Iki Sayi Esittir")
else:
    print("Number1 Number2 dan Daha Buyuk")