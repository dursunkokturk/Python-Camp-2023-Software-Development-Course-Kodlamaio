class Human:

    # Fonksiyon Icinde Self Parametresinden Sonra Verilen Parametreye
    # Fonksiyon Disindan Deger Gonderebiliriz
    def talk(self,sentence):
        print(f"Human : {sentence}")
    
    # Fonksiyon Icinde Self Parametresinden Sonra Verilen Parametreye
    # Fonksiyon Disindan Deger Gonderebiliriz
    def walk(self,sentence):
        print(f"Human : {sentence}")

# Human Class in dan instance Olusturuyoruz
# Olusturulan instance in Atandigi Degisken Adi Uzerinden 
# Kullanarak Class Icindeki Fonksiyonlara Ulasabiliyoruz 
human = Human()
human.talk("Hello")
human.walk("Hello")