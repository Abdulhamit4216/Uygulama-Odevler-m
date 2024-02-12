def enter_number():
    n1 = int(input("1. sayıyı giriniz: "))
    n2 = int(input("2. sayıyı giriniz: "))
    n3 = int(input("3. sayıyı giriniz: "))
    return n1,n2,n3
def big_number(n1,n2,n3):
    if n1 > n2 and n3:
        print("En Büyük Sayı 1. Sayıdır")
    elif n2 > n1 and n3:
        print("En Büyük Sayı 2. Sayıdır")
    elif n3 > n1 and n2:
        print("En Büyük Sayı 3. Sayıdır")

n1,n2,n3 = enter_number()
bignumber = big_number(n1,n2,n3)