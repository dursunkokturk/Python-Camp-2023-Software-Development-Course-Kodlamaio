class Human:

    # Fonksiyon Icinde Self Parametresinden Sonra Verilen Parametreye
    # Fonksiyon Disindan Deger Gonderebiliriz
    def talk(self,sentence,name):

        # Class Icinde Tanimlanan Degiskeni Fonksiyon Icinde Kullanmak Icin
        # Self Anahtar Kelimesini Kullaniyoruz
        print(f"{name} : {sentence}")
    
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

# Fonksiyon Icinde Degiskene Atanan Deger Yada Degerler Olsa Bile
# Fonksiyon Icindeki Degiskene Sonradan Atanan Baska Bir Deger Yazdirilabilir
human1.name = "Sefa"

human1.talk("Hello","Büşra")
human1.walk()

# Class tan Istenildigi Kadar Obje Olusturulabilir
# Olusturulan Obje Uzerinden 
# Class Icindeki Fonksiyonlara Ve Ozelliklere Deger Gonderilebilir
human2 = Human()
human2.name = "Mehmet"
human2.talk("Hi","Gizem")
human2.walk()