sayılar = 0
notlar = []

for i in range(3):
    veri = int(input("{}. not: ".format(i+1)))
    sayılar += veri
    notlar += [veri]

print("Girdiğiniz notlar: ", *notlar)
print("Not ortalamanız: ", sayılar/10)