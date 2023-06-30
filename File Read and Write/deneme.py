with open("fihrist.txt", "r+") as f:
    veri = f.readlines()
    veri.insert(2, "Sedat Köz\t: 0322 234 45 45\n")
    f.seek(0)
    for öğe in veri:
        f.write(öğe)