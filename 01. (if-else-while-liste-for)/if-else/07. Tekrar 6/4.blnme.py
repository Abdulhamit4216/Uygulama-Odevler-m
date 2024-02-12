sayı = int(input("Bir Sayı Giriniz: "))

if sayı % 3 == 0:

    if sayı % 5 == 0:
        print("15e tam bölünür")
else:
    print("15e tam bölünmez")