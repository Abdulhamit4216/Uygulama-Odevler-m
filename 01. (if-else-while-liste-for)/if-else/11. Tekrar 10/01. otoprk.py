saat_süre = float(input("otoparkta kaç saat kaldınız? : "))

ucret = 0

if saat_süre <= 1 :
    ucret = 5
elif saat_süre <= 5 :
    ucret = 5 + (saat_süre - 1)* 4
else: 
    ucret = 5 + 4 * 4 + (saat_süre - 5 )* 3

print("ödemeniz gereken miktar" ,ucret,"TL")