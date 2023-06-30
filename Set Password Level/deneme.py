print("""
LÜTFEN BU KARAKTERLERİ İÇEREN BİR ŞİFRE GİRİNİZ...

1234567890
qwertyuıopğüsdfghjklşizxcvbnmöç
|\}][{¾½$#£>!_?=)(/&%+^')}]
""")

sifre = input("Bir şifre giriniz: ")

sayi = "1234567890"

karakter = "qwertyuıopğüsdfghjklşizxcvbnmöç"

ozelkrktr = "|\}][{¾½$#£>!_?=)(/&%+^')}]"

kontrol = sayi + karakter + ozelkrktr

if sayi in sifre:
    print("Parolanız zayıf seviyede")

elif karakter in sifre:
    print("Parolanız orta seviyede")

elif ozelkrktr in sifre:
    print("Parolanız güçlü seviyede")

elif kontrol in sifre:
    print("Parolanız Çok Güçlü  seviyede")

else:
    print("Eksik ya da hatalı girdiniz...")