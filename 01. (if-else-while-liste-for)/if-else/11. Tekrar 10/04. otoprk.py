saat_suresi = float(input("oto parkta kaç saat kaldınız: "))

ucret = 0

if saat_suresi <= 1 :
    ucret = 5
elif saat_suresi <= 5 :
    ucret = 5 + (saat_suresi - 1)* 4
else: 
    ucret = 5 + 4 * 4 + (saat_suresi - 5 )* 3
print("Ödemeniz Gereken Miktar: ",ucret,"TL")
