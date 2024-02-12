def açı_al():
    açı1 = int(input("Lütfen 1.açıyı girin:\n"))
    açı2 = int(input("Lütfen 2.açıyı girin:\n"))
    açı3 = int(input("Lütfen 3.açıyı girin:\n"))
    return(açı1, açı2, açı3)

def açı_hesapla(a1, a2, a3):
    hesap = (a1 + a2 + a3)
    return hesap

sonuç = açı_al()
toplam = açı_hesapla(sonuç[0], sonuç[1], sonuç[2])
print(toplam)

if toplam == 180:
    print("Bu bir üçgendir.")

elif toplam != 180:
    print("Bu bir üçgen değildir.")