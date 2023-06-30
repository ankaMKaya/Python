print("""
merhabalar sistemimizie hoşgeldiniz sisteme giriş yapmanız için parolanızı girmelisiniz
""")
sayi2 = int(input("Parolanızı girin: "))

if sayi2 == 25802580:
    print("parolanız doğru")

if sayi2 != 25802580: 
    print("parolanız yanlış tekrar giriniz")

kullanıcı_adı = input("Kullanıcı adınız: ")
parola        = input("Parolanız       : ")

toplam_uzunluk = len(kullanıcı_adı) + len(parola)

mesaj = "Kullanıcı adı ve parolanız toplam {} karakterden oluşuyor!"

print(mesaj.format(toplam_uzunluk))

if toplam_uzunluk > 40:
    print("Kullanıcı adınız ile parolanızın ",
          "toplam uzunluğu 40 karakteri geçmemeli!")
else:
    print("Sisteme hoşgeldiniz!")
     