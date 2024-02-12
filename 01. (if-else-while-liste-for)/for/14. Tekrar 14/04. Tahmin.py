import random

rand = random.randint(0,20)

while True:
    sayı = int(input("0 ile 20 Arasında bir sayı giriniz: "))

    if sayı < rand:
        print("Daha Yüksek Bir Sayı Giriniz: ")
    elif sayı > rand: 
        print("Daha Düşük Bir Sayı Giriniz: ")
    else:
        print("Tebrikler doğru bildiniz")
        break