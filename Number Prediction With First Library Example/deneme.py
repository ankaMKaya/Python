import random

rastgele = random.randint(0,100)


while True:


    tahmin = int(input("Tahmininiz: "))
    if rastgele == tahmin:
        print("Tahmininz doğru")
        
        break
    
    elif tahmin > rastgele:
        print("Daha Küçük sayı gir")
        continue

    elif tahmin < rastgele:
        print("Daha büyük sayı gir")
        continue
    
    else:
        print("Lütfen Sayı giriniz.")
        break