print("Hipotenüs değerleri için kenar değerlerini giriniz...")

dikkenar1 = int(input("1.Dik Kenar Değeri= "))
dikkenar2 = int(input("2.Dik Kenar Değeri= "))

hipotenus = (dikkenar1 ** 2) + (dikkenar2 ** 2)

hipdeg = int(hipotenus ** 0.5)

print("Hipotenüs Değeriniz= ", hipdeg)


sayi = input("bir değer giriniz: ")

for sayi in range(len(sayi)):
    print(sayi)