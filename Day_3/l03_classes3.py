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

        # Ayni Class Icindeki Bir Fonksiyon Icinde 
        # Baska Bir Fonksiyona Ait Ozelligi Kullanmak Icin
        # Self Anahtar Kelimesini Kullaniyoruz
        self.walk()
    
    # Fonksiyon Icinde Self Parametresinden Sonra Verilen Parametreye
    # Fonksiyon Disindan Deger Gonderebiliriz
    def walk(self,sentence):

        # Fonksiyon Icinde Tanimlanan Degiskene Atanan Degeri Kullanmak Icin
        # Print Satirinda Sadece Degisken Adini Yazmak Yeterli Oluyor
        name = "Hakan"
        print(f"{name} : {sentence}")

# Human Class in dan instance Olusturuyoruz
# Olusturulan instance in Atandigi Degisken Adi Uzerinden 
# Kullanarak Class Icindeki Fonksiyonlara Ulasabiliyoruz 
human = Human()
human.talk("Hello")
human.walk("Hello")