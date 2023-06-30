import random

dizi = []

son = int(input("Kaç Seçim Arasından yapmak istiyorsunuz ? : "))
rastgele = random.randint(1, son)

for i in range(1,son+1):
    secim = input("{}.Seçeneği Giriniz : ".format(i))
    dizi.append(secim)

print("Seçildi : ",dizi[rastgele])
