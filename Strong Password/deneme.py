while True:
    parola = input("Yeni bir parola belirleyiniz: ")

    if not parola:
        print("parola boş geçilemez, lütfen parola giriniz!!")

    elif len(parola) > 8 or len(parola) < 3 :
        print("parolanızın karakter uzunluğu 3 den büyük 8 den küçük olmamalıdır")
    else:
        print("Yeni Parolanız: ", parola)
        break 