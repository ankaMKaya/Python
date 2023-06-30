sesliharf = "aeıioöuü"
sessizhar = "bcçdfgğhjklmnprsştvyz"

sesliler = ""
sessizler = ""

kelime = int(input("Bir Kelime giriniz: "))

       
# try:
#     kelime = input("Bir Kelime giriniz: ")
    
# except:
#     print()
#     print("Sayı Girdiniz !")
#     kelime = input("Kelimeyi Şimdi Tekrar Giriniz : ")


for i in kelime:
    if i in sesliharf:
        sesliler += i
    else:
        sessizler += i
 

print("Sesli Harfler: ", sesliler)
print("Sessiz Harfler: ", sessizler)