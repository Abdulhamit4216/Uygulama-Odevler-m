def VKİ():
    heigh = float(input("Boyunu Gir: \n"))
    weigh = int(input("Kilonu Gir: \n"))
    return weigh/(heigh*heigh)

kk = VKİ()

if 18 < kk < 25 :
    print("KÜÇÜK KÖFTE!!🍔")
elif 25 < kk < 30 :
    print("ÇEYREK KÖFTE!!🍔")
elif 30 < kk < 34 :
    print("YARI KÖFTE!!🍔")
else : 
    print("SAAADE KÜFTE!!🍔")   


