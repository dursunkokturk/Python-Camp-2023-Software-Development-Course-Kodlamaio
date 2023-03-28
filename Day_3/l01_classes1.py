class Human:

    # Class Icindeki Fonksiyona Class Disindan Ulasabilmek Icin
    # Fonksiyona Self Anahtar Kelimesini Parametre Olarak Vermek Gerekiyor
    # Self -> This
    # Anahtar Kelimesinin Java ve C# daki Karsiligi This Anahtar Kelimesidir
    def talk(self):
        print("Human is Talking")
    
    # Class Icindeki Fonksiyona Class Disindan Ulasabilmek Icin
    # Fonksiyona Self Anahtar Kelimesini Parametre Olarak Vermek Gerekiyor
    # Self -> This
    # Anahtar Kelimesinin Java ve C# daki Karsiligi This Anahtar Kelimesidir
    def walk(self):
        print("Human is Walking")

# Human Class in dan instance Olusturuyoruz
# Olusturulan instance in Atandigi Degisken Adi Uzerinden 
# Kullanarak Class Icindeki Fonksiyonlara Ulasabiliyoruz 
human = Human()
human.talk()
human.walk()