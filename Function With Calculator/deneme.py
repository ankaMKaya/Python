print("Girilen 2 sayının Toplama, Çıkarma ve Çarpma işlemlerini ekrana getirecektir.")

sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))


def çarpma():
    # sayi = int() // olmadı
    carp = sayi1 * sayi2
    cikti = "{} - {} sayılarının çarpımı {} sayısıdır..."
    print(cikti.format(sayi1, sayi2, carp))

çarpma()

def toplama():
    toplam = sayi1 + sayi2 
    cikti = "{} - {} sayılarının toplamı {} sayısıdır..."
    print(cikti.format(sayi1, sayi2, toplam))

toplama()

def çıkarma():
    ckrma = sayi1 - sayi2
    cikti = "{} - {} sayılarının çıkarması {} sayısıdır..."
    print(cikti.format(sayi1, sayi2, ckrma))
    
çıkarma()