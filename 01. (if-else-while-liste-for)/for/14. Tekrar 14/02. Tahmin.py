import random

rastgele = random.randint(0,20)

while True:
    sayı = int(input("0 ile 20 arasında bır sayı gırınız: \n"))

    if sayı < rastgele:
        print("Daha Yüksek Bır Sayı Girin.")
    elif sayı > rastgele:
        print("Daha Düşük Bir Sayı Girin.")
    else:
        print("Tebrikler,Bildiniz.")
        break