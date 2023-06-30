while True:

    try:
        kadi = int(input("Adınızı giriniz: "))
        sadi = int(input("Soyadınızı giriniz: "))

    except:
        pass
    else:
        print("Rakam girme")

    kilo = int(input("Kilonuzu giriniz: "))
    boy = float(input("Boyunuzu giriniz: "))

    formul = kilo / (boy*boy)

    print(kadi, sadi, "Vücut Kitle Endeksiniz: ", formul)

    if 0 <= formul <= 18:
        print("Zayıfsınız! Lütfen sıkca yemek yiyiniz")

    elif 18 < formul <= 24:
        print("İdeal kilodasınız") 
    
    elif 24 < formul <= 28:
        print("Çok kilosunuz, oruç tutmalısınız")

    else:
        print("Olması gereken kilonun çok üstündesiniz, ölebilirsiniz")
    continue