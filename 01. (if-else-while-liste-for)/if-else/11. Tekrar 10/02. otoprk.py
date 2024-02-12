saat_süresi = float(input("oto parkta kaç saat kaldınız: "))

ucret = 0 

if saat_süresi <= 1 :
    ucret = 5 

elif saat_süresi <= 5 :
    ucret = 5 + (saat_süresi - 1)* 4
else: 
    ucret = 5 + 4 * 4 + (saat_süresi - 5 )* 3
print("Ödemeniz Gereken Miktar: ",ucret,"TL")