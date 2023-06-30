import random

dizi = []

son = int(input("Kaç Seçim Arasından yapmak istiyorsunuz ? : "))
rastgele = random.randint(1, son)

for i in range(1,son+1):
    secim = input("{}.Seçeneği Giriniz : ".format(i))
    dizi.append(secim)



try:
    sayi1 = int(input("Birinci Sayıyı Giriniz :"))

except ValueError:
    print()
    print("Ondalık Sayı Girdiniz !")
    sayi1 = float(input("Birinci Sayıyı Şimdi Tekrar Giriniz : "))


try:
    sayi2 = int(input("İkinci Sayıyı Giriniz : "))

except ValueError:
    print()
    print("Ondalık Sayı Girdiniz !")
    sayi2 = float(input("İkinci Sayıyı Şimdi Tekrar Giriniz : "))


try:
    sayi3 = int(input("Üçüncü Sayıyı Giriniz : "))

except ValueError:
    print()
    print("Ondalık Sayı Girdiniz !")
    sayi3 = float(input("Üçüncü Sayıyı Şimdi Tekrar Giriniz : "))

print("Toplam : ",sayi1+sayi2+sayi3)