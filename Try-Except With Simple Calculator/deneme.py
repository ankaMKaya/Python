while True:

    try:
        sayi1 = int(input("1.Değişkeninizi giriniz: "))
        sayi2 = int(input("2.Değişkeninizi giriniz: "))
    except:
        print("çıkış yapılıyor!!")
        quit()

    print(""" Lütfen bir seçim yapnız:
    [1] Toplama
    [2] Çıkarma
    [3] Çarpma
    [4] Bölme

    [q] çıkış yap
    """)

    secim = input("Seçiminiz: ")

    if secim == "1":
        sonuc = sayi1 + sayi2
        print("Toplam sonucunuz: ", sonuc)

    elif secim == "2":
        sonuc = sayi1 - sayi2
        print("Çıkarma sonucunuz: ", sonuc)

    elif secim == "3":
        sonuc = sayi1 * sayi2
        print("Çarpma sonucunuz: ", sonuc)
    
    elif secim == "4":
        try:
            sonuc = sayi1 / sayi2
            print("Bölme sonucunuz: ", sonuc)
        except ZeroDivisionError:
           print("Sıfıra Bölünemez aq")
    else:
           print("Lütfen Doğru bir seçim yapınız!! ")
    continue