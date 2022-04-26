isimler = ["Ahmet", "Ayse", "LeYla", "HASan", "HazaL"]
string = "Merhaba Istanbul 34903";
yillar = [1957, 1989, 1999, 2002];
dereceler = [20, 5, 15, -2, -6, 0];

# 1) 1-100 arasındaki sayılardan 12 sayısına tam bölünebilen sayı listesi oluşturun.
# 2) isimler listesindeki her ismi küçük harfe çevirip tersten yazdırın.
# 3) Verilen "string" içindeki rakamları içeren bir liste oluşturunuz.
# 4) "yillar" dizisindeki her doğum yılı için yaş bilgisini içeren liste oluşturunuz.
# 5) "dereceler" listesinde bulunan hava sıcaklık bilgisine göre eksi değer için buzlanma
# tehlikesi yazınız.

# 1:

sonuc = [i for i in range(101) if i % 12 == 0];
print(sonuc);

#2:

isimler = [isim.lower()[::-1] for isim in isimler]
print(isimler);

#3:

string = [sttr for sttr in string if sttr.isdigit()];
print(string);

#4:
import datetime
yillar = [(datetime.datetime.now().year-dogumYili) for dogumYili in yillar];
print(yillar);

#5:

dereceler = [derece if derece >= 0 else "Buzlanma Tehlikesi" for derece in dereceler]
print(dereceler);