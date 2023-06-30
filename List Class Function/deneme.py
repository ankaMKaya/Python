sayac = 1

import os

os.system("clear")

metin =  dir(list)

for i in metin:
    if i[0] == "_":
        sayac+=1

print(sayac)

print(dir(list))
