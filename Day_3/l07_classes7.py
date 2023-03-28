class Human:

    # Class Icinde Tanimlanan Degiskene Atanan Degeri
    # Fonksiyon Icinde Kullanabilmek Icin
    # Self Anahtar Kelimesini Parametre Olarak Kullanmak Gerekiyor
    name = "Dursun"

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
# Olusturulan instance in Atandigi Degisken Adi Uzerinden 
# Kullanarak Class Icindeki Fonksiyonlara Ulasabiliyoruz 
human1 = Human()

human1.talk("Hello")
human1.walk()

# Class tan Istenildigi Kadar Obje Olusturulabilir
# Olusturulan Obje Uzerinden 
# Class Icindeki Fonksiyonlara Ve Ozelliklere Deger Gonderilebilir
human2 = Human()
# human2.name = "Mehmet"
human2.talk("Hi")
human2.walk()