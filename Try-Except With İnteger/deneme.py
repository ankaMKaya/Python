while True:
        
    print("Lütfen 3 ayrı tam sayı değeri giriniz...")
    try:
        sayi1 = int(input("1.tam sayı= "))
        sayi2 = int(input("2.tam sayı= "))
        sayi3 = int(input("3.tam sayı= "))

    except:
            print("ondalık sayı girmeyiniz")

    tamsayi = sayi1 * sayi2 * sayi3
                            
    print("Girdiğiniz değerlerin çarpım sonucu= ", tamsayi)
    continue