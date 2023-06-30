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