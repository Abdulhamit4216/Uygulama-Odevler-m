n1 = int(input("1. Sayıyı  Giriniz: "))
n2 = int(input("2. Sayıyı Giriniz: "))
toplam =  0

for a in range(n1, n2 + 1): 
    toplam += a

print("Toplamı :",toplam)