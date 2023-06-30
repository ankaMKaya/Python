def fonk(n):
    # sayi = input("sayınızı giriniz: ")
    if n < 0:
        return 'eksi değerli sayı olamaz!!'
    else:
        return n
    
f = fonk(5)

print("Merhaba girdiğiniz sayı değeri: {} " .format(fonk(f)))