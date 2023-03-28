# fonksiyonlar
price = 100
discount = 20

print("Fiyat - Indirim Hesabini Yapan Fonksiyon Islem Sonucu")
def calculate():
    print(100-20)
calculate()
calculate()
calculate()

print("")

# Parametre Kullanilarak Hesaplama Yapan Fonksiyon
print("Parametre Kullanilarak Fiyat - Indirim Hesabini Yapan Fonksiyon Islem Sonucu")
def calculateWithParams(price,discount):
    print(price - discount)

calculateWithParams(100,30)

print("")

print("Say Hello Fonksiyonu Icinde F-String Kullanilarak Karsilama Mesaji Yazdirma")
def sayHello(name):
    print(f"Hello {name}")

sayHello("Dursun")

print("")

print("Fonksiyona Parametre Uzerinden Gonderilen Degerlerin Sonuclarini Donduren Fonksiyon")
def calculateAndReturn(price,discount):
    return price-discount

newPrice = calculateAndReturn(200,50)
print(newPrice)

print("")

def calculatePrice(price,discount):
    price-discount

def calculatePriceAndReturn(price,discount):
    return price-discount

# calculatePrice Fonksiyonunda Islem Yapiliyor Ancak Return Komutu Olmadigi Icin
# Yapilan Islemin Sonucu Alinamiyor 
function1 = calculatePrice(100,50)

# calculatePrice Fonksiyonunda Islem Yapiliyor Ve Return Komutu Oldugu Icin
# Yapilan Islemin Sonucu Aliniyor 
function2 = calculatePriceAndReturn(300,100)

print("Function1 Degiskenine Atanan Fonksiyon Icinde Return Komutu Olmadigindan Islem Sonucu Alinamiyor")
print(function1)

print("Function2 Degiskenine Atanan Fonksiyon Icinde Return Komutu Oldugundan Islem Sonucu Aliniyor")
print(function2)