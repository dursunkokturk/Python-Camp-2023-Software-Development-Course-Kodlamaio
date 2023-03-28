# self => this

class Human:

    def __init__(self,name) -> None:
        self.name = name
        print("Bir Human instance Uretildi")

    def __str__(self) -> str:
        return f"STR Fonksiyonundan Donen Deger : {self.name}"
    
    # Fonksiyonun Cagirilmasi Ve Kullanilmasi Icin
    # Fonksiyon Icinde Self Parametresi Kullanmak Gerekiyor
    def talk(self,sentence):
        print(f"{self.name} : {sentence}")
    def walk(self,sentence):
        print(f"{self.name} : {sentence}")

# inheritance Islemi Yapiyoruz
human = Human("Enes")
# human.name = "Hakan"
human.talk("Hello")
human.walk("Hello")
print(human)