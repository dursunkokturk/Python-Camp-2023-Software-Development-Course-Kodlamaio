# Kullanicidan Alinacak Deger String Veri Tipinde Olacagi Icin
# Kullanicidan Alinan Degeri Kullanicidan Alma Asamasinda int Veri Tipine Cevirebiliriz
maturity = int(input("Lütfen Vade Miktarini Giriniz"))
print(maturity)
print("")

print(type(maturity))
print("")

# Kullanicidan Alinan int Tipindeki Deger String Veri Tipinde Oldugu Icin
# Kullanicidan Alinan Degeri int Veri Tipine Cevirmek Gerekiyor
print(int(maturity) + 12)





# String Interpolation
# Secilen Vade Sonucu Ortaya Cikan Vade

# Kullanicidan Alinan int Tipindeki Veriyi String Tipine Cevirerek Ekrana Yazdiriyoruz
print("Secilen Vade Sonucu Ortaya Cikan Vade = " + str(maturity))
print("")

# Format Fonksiyonu Icinde
# Kullanicidan Alinan Veriyi Atandigi Degisken Adi Uzerinden
# Baska Bir Degiskene Atama Yapiyoruz
# Verinin Atandigi Degisken Adini 
# Ekrana Yazdirilacak Alan Icinde Suslu Paranteze Alarak Yaziyoruz
print("Secilen Vade Sonucu Ortaya Cikan Vade = {maturityNumber}".format(maturityNumber=maturity))
print("")

name1 = "Dursun"
text = "Hello {name}".format(name=name1)
print(text)
print("")

text = "Hello {name}".format(name=name1)
print(text)
print("")



print("Secilen Vade Sonucu Ortaya Cikan Vade {maturity}")