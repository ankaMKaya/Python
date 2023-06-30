renk1 = input("1.Renk : ")
renk2 = input("2.Renk : ")
renk3 = input("3.Renk : ")

if renk1.isalpha() and renk2.isalpha() and renk3.isalpha():
    pass  # is.alpha ---> STRİNG Mİ DİYE KONTROL EDER 

else: 
    print(" Lütfen SADECE RENK GİRİNİZ ! ")
    quit()
    
renk_Listesi = [renk1,renk2,renk3]

print("Renkleriniz : ",renk_Listesi)

print("""

Renk değişikliği yapmak istiyormusunuz ?

[e] Evet
[h] Hayır

""")

secim = input("Seçiminiz : ")

if secim == "e" or secim == "E":
    
    print("""
    Değiştirmek istediğiniz renk hangisi ?
    [1] {}
    [2] {}
    [3] {}
    """.format(renk1,renk2,renk3))
    
    secim = input("Seçiminiz : ")

    if secim == "1":
        renk1 = input("Yeni Rengi giriniz : ")  
        renk_Listesi[0] = renk1
        print("Yeni Renk Listesi : ",renk_Listesi)

    elif secim == "2":
        renk2 = input("Yeni Rengi giriniz : ")  
        renk_Listesi[1] = renk2
        print("Yeni Renk Listesi : ",renk_Listesi)
    
    elif secim == "3":
        renk3 = input("Yeni Rengi giriniz : ")  
        renk_Listesi[2] = renk3
        print("Yeni Renk Listesi : ",renk_Listesi)
    
    else:
        print("Lütfen doğru bir seçim yapınız ! ")

elif secim == "h" or secim == "H":
    print("Tekrar görüşeceğiz...")

else:
    print("Lütfen doğru bir seçim yapınız !")
