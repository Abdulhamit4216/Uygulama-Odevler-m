tercih = input("bir tercih yapınız(sinema/tiyatro): \n")
öğrenci = input("öğrencimisiniz(evet/hayır): \n")

ucret = 0

if tercih == "sinema":
    ucret = 15
elif tercih == "tiyatro":
    ucret = 10
if öğrenci == "evet":
    ucret *= 0.5
    print("ödemeniz gereken miktar:",ucret,"TL")