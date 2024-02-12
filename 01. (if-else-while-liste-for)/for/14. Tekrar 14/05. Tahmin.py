import random

rand = random.randint(0,20)

while True:
    sayı = int(input("0 İle 20 Arasında Bir Sayı Giriniz: "))

    if sayı < rand:
        print("Daha Yüksek Bir Sayı Girin: ")
    elif sayı > rand:
        print("Daha Düşük Bir Sayı Girin: ")
    else: 
        print("Tebrikler , Doğru Bildiniz :)")
        break