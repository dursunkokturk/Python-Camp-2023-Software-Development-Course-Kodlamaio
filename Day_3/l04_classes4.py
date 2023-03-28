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
        print("Human is Walking")

# Human Class in dan instance Olusturuyoruz
# Olusturulan instance in Atandigi Degisken Adi Uzerinden 
# Kullanarak Class Icindeki Fonksiyonlara Ulasabiliyoruz 
human = Human()

# Fonksiyon Icinde Degiskene Atanan Deger Yada Degerler Olsa Bile
# Fonksiyon Icindeki Degiskene Sonradan Atanan Baska Bir Deger Yazdirilabilir
human.name = "Sefa"

human.talk("Hello")
human.walk()