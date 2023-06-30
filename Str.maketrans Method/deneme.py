kaynak = "şçöğüıŞÇÖĞÜİ"
hedef = "scoguiSCOGUI"

ceviri_tablosu = str.maketrans(kaynak, hedef)

metin = "bilidiğiniz üzre python yazılım dilidir."

print(metin.translate(ceviri_tablosu))