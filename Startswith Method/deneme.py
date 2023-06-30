print("""
Lütfen "İ" ile başlayan kelime veya cümleler giriniz.
""")

kardiz = input("Sözcüğünüz: ")

if kardiz.startswith("i") or kardiz.startswith("ı") or kardiz.startswith("I"):
        kardiz = "İ" + kardiz[1:]
        kardiz = kardiz.title()

elif kardiz.title():
    print(kardiz)

else:
      kardiz = kardiz.title()

print(kardiz)