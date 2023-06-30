liste = []

while True:
    sayı = input("Bir sayı girin: (çıkmak için q) ")

    if sayı == "q":
        break

    sayı = int(sayı)

    if sayı not in liste:
        liste +=  [sayı]
        print(liste)
    else:
        print("Bu sayıyı daha önce girdiniz!")