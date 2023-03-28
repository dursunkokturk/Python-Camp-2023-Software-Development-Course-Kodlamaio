# listeler
credits = ["Ihtiyac Kredisi","Tasit Kredisi","Konut Kredisi"]
print("Credits List Icindeki Degerler")
print(credits)
print("")

print("Credits List Veri Tipi")
print(type(credits))
print("")

print("Credits List Icindeki 0 Nolu indiste Yer Alan Deger")
print(credits[0])
print("")

print("Credits List Icindeki 1 Nolu indiste Yer Alan Deger")
print(credits[1])
print("")

print("Credits List Icindeki 2 Nolu indiste Yer Alan Deger")
print(credits[2])
print("")

# print("Credits List Icindeki 5 Nolu indiste Yer Alan Deger")
# print(credits[5])
# print("")

print("Crdits List Icindeki Toplam Eleman Sayisi")
print(len(credits))
print("")

# List Icindeki Elemanlari Islemde Kullanirken 
# Yani List Icindeki Son Elemana Ulasmak Icin len()-1 Olarak Kullaniyoruz
print("Crdits List Icindeki Toplam Eleman Sayisi")
print(len(credits)-1)
print("")

# Array Icinde Birbirinden Farkli Elemanlar Olabilir
# array = ["Ihtiyac Kredisi",10,5.2,True]
# print(array)

# List Icindeki Verilerin En Sonuna Yeni Bir Eleman Ekliyoruz
print("List Icindeki Verilerin En Sonuna Yeni Bir Eleman Ekliyoruz")
credits.append("Ozel Kredi")
print(credits)
print("")

# Kullanici Tarafindan Fonksiyon Icinde Belirtilen indis Numarasinda Yer Alan Degeri Siler
# Kullanici Tarafindan Fonksiyon Icinde indis Numarasi Verilmedi Ise List Icindeki En Sonda Yer Alan Degeri Siler
print("Pop Fonksiyonu Icinde indis Numarasi Verilmeden List Icindeki En Sonda Yer Alan Degeri Silme")
credits.pop()
print(credits)
print("")

# Kullanici Tarafindan Fonksiyon Icinde Belirtilen indis Numarasinda Yer Alan Degeri Siler
# Kullanici Tarafindan Fonksiyon Icinde indis Numarasi Verilmedi Ise List Icindeki En Sonda Yer Alan Degeri Siler 
print("Pop Fonksiyonu Icinde indis Numarasi Verilerek List Icinde Yer Alan Degeri Silme")
credits.pop(0)
print(credits)
print("")

# Kullanici Tarafindan Fonksiyon Icinde Belirtilen Degeri Siler
# List Icinde Ayni Degerden Birden Fazla Olursa 
# Silme Isleminde List Icindeki Ilk Degeri Siler
print("Remove Fonksiyonu Ile List Icinde Belirtilen Degeri Silme")
credits.remove("Tasit Kredisi")
print(credits)
print("")

# Kullanici Tarafindan List Icine Birden Fazla Elemani Tek Seferde Ekleme
print("Extend Fonksiyonu Ile Birden Fazla Degerin Tek Seferde Eklenmis Hali")
credits.extend(["X Kredisi","Y Kredisi","Z Kredisi"])
print(credits)