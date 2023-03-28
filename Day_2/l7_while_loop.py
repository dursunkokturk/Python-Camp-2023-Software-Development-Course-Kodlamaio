# while loop
# while True:
#     print("x")
    
print("")
i = 0

print("While Dongusu Ile 0 dan Baslayarak 10 a Kadar Olan Sayilari Yazdirma")
while i < 10:
    print("x")
    i += 1

print("")

a = 0
print("Credits List Icindeki Degerleri indis Numarasina Gore List Elemani Boyutu Kadar Yazdirma")
credits = ["Ihtiyac Kredisi","Tasit Kredisi","Konut Kredisi"]
while a < len(credits):
    print(credits[a])
    a += 1

print("")

a = 0
print("Credits List Icindeki Degerleri Yazdirirken if Dongusu Ile Belirtilen Degere Gelindiginde Break Komutu Ile Donguyu Bitirme")
while a < len(credits):
    print(credits[a])
    a += 1
    if credits[a] == "Konut Kredisi":
        break

print("")

a = 0
# List Icindeki Ilk Degeri Gecip Sonraki Degerden Itibaren Yazdiriyoruz
print("Credits List Icindeki Degerleri Yazdirirken if Dongusu Ile Belirtilen Degere Gelindiginde Break Komutu Ile Donguyu Bitirme")
while a < len(credits):
    a += 1
    print(credits[a])
    if credits[a] == "Konut Kredisi":
        break