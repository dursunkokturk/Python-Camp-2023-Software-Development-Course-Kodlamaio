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


# maturity = input("Lütfen Vade Miktarini Giriniz")
# print(maturity)
# print(type(maturity))
# print(maturity + 12)



 

# String Interpolation
# Secilen Vade Sonucu Ortaya Cikan Vade
print("Secilen Vade Sonucu Ortaya Cikan Vade" + str(maturity1))
print("Secilen Vade Sonucu Ortaya Cikan Vade {maturityNumber}".format(maturityNumber=maturity1))
print(f"Secilen Vade Sonucu Ortaya Cikan Vade {maturity1}")

name1 = "Dursun"
text = "Hello {name}".format(name=name1)
print(text)
print("")

# name1 = input("Isminizi Giriniz")
text = "Hello {name}".format(name=name1)
print(text)
print("")




# f-string
text = f"Welcome {name1}"





# listeler
credits = ["Ihtiyac Kredisi","Tasit Kredisi","Konut Kredisi"]
print(credits)
print("")

print(type(credits))
print("")

print(credits[0])
print("")

print(credits[1])
print("")

print(credits[2])
# print(credits[5])

print(len(credits))
print("")

# array = ["Ihtiyac Kredisi",10,5.2,True]
# print(array)

credits.append("Ozel Kredi")
print(credits)
print("")

credits.pop()
print(credits)
print("")

credits.remove("Tasit Kredisi")
print(credits)
print("")

credits.extend(["X Kredisi","Y Kredisi","Z Kredisi"])
print(credits)
print("")

for i in range(10):
    print(i)

print("")

for a in range(5,10):
    print(a)

print("")

for b in range(0,51,10):
    print(b)

print("")

# for c in range(0.1,0.5):
#     print(c)

credits = ["Ihtiyac Kredisi","Tasit Kredisi","Konut Kredisi"]

for credi in credits:
    print(credi)

print("")

for d in range(len(credits)):
    print(credits[d])

print("")





# while loop
# while True:
#     print("x")
    
print("")

while i < 10:
    print("x")
    i += 1

print("")

while i < 10:
    print("x")
    i += 1

print("")

while i < len(credits):
    print(credits[i])
    i += 1

print("")

while i < len(credits):
    if credits[i] == "Konut Kredisi":
        break
    print(credits[i])
    i += 1


# döngüler
# fonksiyonlar
price = 100
indirim = 20

def calculate():
    print(100-20)
calculate()
calculate()
calculate()

print("")

def calculateWithParams(price,indirim):
    print(price - indirim)

calculateWithParams(100,30)

print("")

def sayHello(name):
    print(f"Hello {name}")

sayHello("Dursun")

print("")

def calculateAndReturn(price,discount):
    return price-discount

newPrice = calculateAndReturn(200,50)
print(newPrice)

print("")

# function1 = calculatePrice(100,50)
# function2 = calculatePriceAndReturn(300,100)
# print(function1)
# print(function2)