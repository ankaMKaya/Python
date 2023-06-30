# isim1 = 'Muhammed'
isim = 'Kaya'

def fonk():
    global isim
    isim += ' Fırat'
    return isim

print("metin: {} " .format(fonk()))