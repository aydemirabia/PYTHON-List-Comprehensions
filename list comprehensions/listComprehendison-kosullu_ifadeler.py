# for item in liste:
#     if (koşul):
#         expression

# [expression for item in liste if koşul]

#---------------------------------------------------------------------------------------

sayilar =[1,5,6,9,10,16,34];
sonuc = [];

for sayi in sayilar:
    if(sayi % 2 == 0):
        sonuc.append(sayi);
print(sonuc);


#---------------------------------------------------------------------------------------
# list comprehensions:
sonuc2 = [sayi for sayi in sayilar if sayi % 2 == 0] 
print(sonuc2);

fiyatlar = [1000, 2000, 3000, 0, 4000, 0];
vergiler = [];

for fiyat in fiyatlar:
    if(fiyat>0):
        vergiler.append(fiyat*1.18)
print("Vergiler: ",vergiler);

#---------------------------------------------------------------------------------------
# list comprehensions:

vergiler = [fiyat*1.18 for fiyat in fiyatlar if fiyat > 0];
vergiler = [fiyat*1.18 if fiyat>0 else "Vergi Hesaplanmadi" for fiyat in fiyatlar];
print(vergiler);