import random

rand_om = random.randint(0,20)
while True:
    sayı = int(input("0 ile 20 Arasında sayı gırınz: "))

    if sayı < rand_om:
        print("Daha Yüksek bir sayı giriniz.")
    elif sayı > rand_om:
        print("daha düşük bir sayu giriniz.")
    else:
        print("tebrikler, doğru bildiniz")
        break