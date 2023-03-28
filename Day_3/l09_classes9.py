# Built in Hazir Fonksiyonlar

class Human:

    # Java da Bu Islem Constructor Olarak Biliniyor
    def __init__(self,name) -> None:
        self.name = name

    # Fonksiyon Icinde Self Parametresinden Sonra Verilen Parametreye
    # Fonksiyon Disindan Deger Gonderebiliriz
    def talk(self,sentence):

        # Class Icinde Tanimlanan Degiskeni Fonksiyon Icinde Kullanmak Icin
        # Self Anahtar Kelimesini Kullaniyoruz
        print(f"{self.name} : {sentence}")
    
    # Fonksiyon Icinde Self Parametresinden Sonra Verilen Parametreye
    # Fonksiyon Disindan Deger Gonderebiliriz
    def walk(self):

        # Fonksiyon Icinde Tanimlanan Degiskene Atanan Degeri Kullanmak Icin
        # Print Satirinda Sadece Degisken Adini Yazmak Yeterli Oluyor
        print(f"{self.name} is Walking")

# Human Class in dan instance Olusturuyoruz
# Olusturulan instance Icinde Parametre Gonderiyoruz 
human1 = Human("Dursun")

human1.talk("Hello")
human1.walk()

# Human Class in dan instance Olusturuyoruz
# Olusturulan instance Icinde Parametre Gonderiyoruz 
human2 = Human("Sefa")
human2.talk("Hi")
human2.walk()