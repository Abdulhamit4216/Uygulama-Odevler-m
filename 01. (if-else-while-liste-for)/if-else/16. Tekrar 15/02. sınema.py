preference = input("Bir Tercih Yapınız (sinema/tiyatro): \n")
öğrenci = input("öğrencimisiniz? (evet/hayır) : \n")

ucret = 0

if preference == "tiyatro" :
    ucret = 10
elif preference == "sinema" :
    ucret = 15
if öğrenci == "evet" :
    ucret *= 0.5

print("ödemeniz gereken miktar: ",ucret,"TL") 