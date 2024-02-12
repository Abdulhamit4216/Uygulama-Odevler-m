a1 = float(input("1. acının derecesini giriniz: "))
a2 = float(input("2. acının derecesini giriniz: "))
a3 = float(input("3. acının derecesini giriniz: "))

if a1 == a2 == a3 :
    print("bu bir eşkenar üçgendir")
elif a1 == a2 or a1 == a3 or a2 == a3 :
    print("bu bir ikiz kenar üçgendir")
else:
    print("bu bir çeşit kenar üçgendir")