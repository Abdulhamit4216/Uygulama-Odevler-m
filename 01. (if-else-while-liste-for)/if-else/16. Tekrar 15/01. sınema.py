tercih = input("sinemayımı tercıh edersınızı yoksa tıyatroyumu? : \n")
ögrenci = input("öğrencimisiniz ? (evet\hayır): \n")

ucret = 0

if tercih == "sinema" :
    ucret = 15 
elif tercih == "tiyatro" :
    ucret = 10

if ögrenci == "evet":
    ucret *= 0.5
print("ödemeniz gereken miktar",ucret,"TL")