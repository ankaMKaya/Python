ilk_metin = "gigihjrp,hwehsprhkhh0"
ikinci_metin = "şüthpğenlbmgçbeyçneiethetşhg.blşbhth"

fark=""

for s in ikinci_metin:
    if not s in ilk_metin and not s in fark:
        fark += s
        print(s)