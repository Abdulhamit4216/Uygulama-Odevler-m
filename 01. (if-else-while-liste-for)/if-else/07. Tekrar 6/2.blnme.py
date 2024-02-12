sayi = int(input("bir sayı giriniz: "))

if sayi % 3 == 0:

    if sayi % 5 == 0:
        print("15e tam bölünür")
else:
    print("15e tam bölünmez")