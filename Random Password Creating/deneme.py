import random

while True:

    alfabe = "abcdefghjklmnroö0prz123456789/*-+"

    password = ""

    for i in range(len(alfabe)):

        password = password + random.choice(alfabe)

    print("Şifreniz:{}".format(password))