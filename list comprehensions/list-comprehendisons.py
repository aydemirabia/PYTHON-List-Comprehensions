liste = [10, 4, 7, 9, 6, 70];
sayilar = [];

for i in liste:
    i *= 2;
    sayilar.append(i);
    
# [expression for item in list] ---> [listedeki öğe için ifade]
# list comprehensions: 
sayilar = [i*2 for i in liste]
print(sayilar);

isim = "Ahmet";
isimler = ["AhmeT", "YusUf", "AysEna", "HaZal"]

sonuc = [c.upper() for c in isim]
sonuc = [str(sayi) for sayi in liste]
sonuc = [i.lower() for i in isimler]

print(sonuc);