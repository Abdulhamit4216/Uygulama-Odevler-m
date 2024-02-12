import random

rand = random.randint(0, 20)

while True:
    sayi = int(input("0 ile 20 arasında değer girin: "))
    
    if sayi < rand:
        print("Daha Yüksek Bir Sayı Girin.")
    elif sayi > rand:
        print("Daha Düşük Bir Sayı Girin.")
    else:
        print("Tebrikler, Bildiniz")
        break