sayi = int(input("Bir sayı giriniz: "))

def kare_bul():
    # sayi = int() // olmadı
    cikti = "{} sayının karesi {} sayısıdır..."
    print(cikti.format(sayi, sayi**2))

kare_bul()