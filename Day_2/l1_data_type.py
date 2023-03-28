interest = 1.59

# Atanan Deger int Tipinde
maturity1 = 36

# Atanan Deger String Tipinde
maturity2 = "36"
creditName = "Ihtiyac Kredisi"

print("Maturity1 Degiskenine Atanan Deger Ile 12 Degerinin Toplami =")
print(maturity1 + 12)
print("")

print("Maturity1 Degiskenine Atanan Degerin Veri Tipi")
print(type(maturity1))
print("")

print("Maturity2 Degiskenine Atanan Deger Ile 12 Degeri Toplama Islemi Yapilirsa Hata Verecek")
print("Maturity2 Degiskenine Atanan Degerin Veri Tipi String 12 Degeri int Tipinde")
# print(maturity2 + 12)
print("")

print("Maturity2 Degiskenine Atanan Degerin Veri Tipi Ile 12 Degeri Toplama Islemi Yapilirsa Hata Verecek")
print(int(maturity2) + 12)
print("")

print("interest Degiskenine Atanan Deger =")
print(interest)
print("")

print("interest Degiskenine Atanan Degerin Veri")
print(type(interest))
print("")

print("CreditName Degiskenine Atanan Deger =")
print(creditName)
print("")

print("CreditName Degiskenine Atanan Degerin Veri Tipi =")
print(type(creditName))
print("")





# Degiskene Atanan Degerin Veri Tipini Degistirmek Icin
# Ilk Olarak Donusum Isleminin Yapilacagi Degiskeni
# Donusturulmek Istenilen Veri Tipi Parantezine Aliyoruz
# Ikinci Olarak Yapilan Bu Islemi Bir Degiskene Atiyoruz
interest = str(interest)

# Veri Tipi Donusturme Isleminin Duzgun Yapilma Durumunu Kontrol Etmek Icin
# type Fonsiyonu Icinde Degisken Adini Yaziyoruz
print("Interest Degiskenine Atanan Degerin int Veri Tipinin Yeni Hali")
print(type(interest))
print("")

print("Maturity Degiskenine Atanan Deger =")
print(maturity2)
print("")

print("Maturity Degiskenine Atanan Degerin Veri Tipi =")
print(type(maturity2))
print("")

print("Veri Tipi String Olan Deger Ile Veri Tipi int Olan Degerlerin Toplami =")
print(int(maturity2) + 12)
print("")

# int Tipinde Veri Bulunan Degiskenin Degerini String Tipine Cevirme
# Veri Tipi Donusumu Yapilacak Degisken Adini 
# Donusturulmek Istenilen Veri Tipi Parantezinde Yaziyoruz
interest = str(interest)
print(int(interest))