ing_sözlük = {"dil": "language", "bilgisayar": "computer", "masa": "table"}

sorgu = input("Lütfen anlamını öğrenmek istediğiniz kelimeyi yazınız:")

print(ing_sözlük.get(sorgu, "Bu kelime veritabanımızda yoktur!"))

# aynı mantık hava durum

# soru = input("Şehrinizin adını tamamı küçük harf olacak şekilde yazın:")

# cevap = {"istanbul": "gök gürültülü ve sağanak yağışlı",
#          "ankara": "açık ve güneşli", "izmir": "bulutlu"}

# print(cevap.get(soru, "Bu şehre ilişkin havadurumu bilgisi bulunmamaktadır."))