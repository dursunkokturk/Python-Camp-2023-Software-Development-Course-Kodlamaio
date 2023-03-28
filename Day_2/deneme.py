# Öğrenci Kayıt Sistemi

ogrenciler = ["Ali Akçay", "Osman Karakuş", "Ragıp Şenses"]
print(ogrenciler)

def ogrenciEkle():
    yeniOgrenci = input("Lütfen öğrenci isim ve soyisim giriniz: ")
    return yeniOgrenci #return kullanarak elde ettiğimiz değeri fonskiyon dışında kullanabiliriz
yeniOgrenci = ogrenciEkle()
ogrenciler.append(yeniOgrenci) #append ekleme komutudur
print(ogrenciler)

def ogrenciSil():
    silinecekOgrenci = input("Lütfen listeden çıkarmak istediğiniz öğrencinin adını ve soyadını yazınız: ")
    return silinecekOgrenci
silinecekOgrenci = ogrenciSil()
ogrenciler.remove(silinecekOgrenci) #remove silme/çıkarma komutudur
print(ogrenciler)   

def multiOgrenciEkle():
    kacOgrenci = input("Lütfen kaç öğrenci ekleyeceğinizi giriniz: ") #inputtan gelen veriler string veri tipidir for döngüsünde sayaç olarak kullanabilmemiz için önce integer değere çevirmeliyiz aşağıdaki koşulda olduğu gibi.
    for i in range(int(kacOgrenci)):
        multiEkle = input("Lütfen eklemek istediğiniz öğrenci isim soyisimini giriniz: ")
        ogrenciler.append(multiEkle)
        print(ogrenciler)
multiOgrenciEkle()

for ogrenci in ogrenciler:
    print(ogrenci)

def whatIsNumber():
    ogrenciAdi = input("Lütfen numarasını öğrenmek istediğiniz öğrencinin isim ve soyismini giriniz: ")
    for i in range(len(ogrenciler)):
        if ogrenciler[i] == ogrenciAdi: #Burada kullanıcıdan öğrencinin adını aldık for döngüsüyle ogrenciler listemizin döndürülmesini sağladık. if koşulu olarak for döngüsünden gelen öğrenci isminin kullanıcıdan ogrenciAdı değişkeni ile aldığımız isimi karşılaştırdık. eğer == durumu var ise ogrenciler listesinin o andaki elemanı i. elemandır ve ödev isterine göre index numarası aynı zamanda öğrencinin nuamrası sayıalcak. Biz buradan i değerini return ederek öğrencimizin numarasına ulaşmış oluyoruz.
            return i
ogrenciNo = whatIsNumber()
print(f"Girdiğiniz öğrencinin numarası: {ogrenciNo}")

def multiOgrenciSil():
    kacOgrenci = input("Lütfen kaç öğrenci silmek istediğinizi giriniz: ")  #inputtan gelen veriler string veri tipidir while döngüsünde sayaç olarak kullanabilmemiz için önce integer değere çevirmeliyiz aşağıdaki koşulda olduğu gibi.
    i=0
    while i<int(kacOgrenci):
        multiSil = input("Lütfen listeden çıkarmak istediğiniz öğrencinin ad ve soyadını yazınız: ")
        ogrenciler.remove(multiSil)
        print(ogrenciler)
        i+=1
multiOgrenciSil()