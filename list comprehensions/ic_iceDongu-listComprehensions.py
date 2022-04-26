sonuc = [];

for i in range(3):
    for j in range(3):
        sonuc.append((i, j));
print(sonuc);

sonuc = [(i, j, k) for i in range(3) for j in range(3) for k in range(3)];
print(sonuc);