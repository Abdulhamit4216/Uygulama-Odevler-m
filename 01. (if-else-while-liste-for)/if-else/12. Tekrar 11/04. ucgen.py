aci1 = float(input("1. acinin derecesini giriniz: "))
aci2 = float(input("2. acinin derecesini giriniz: "))
aci3 = float(input("3. acinin derecesini girniz: "))
total = float(input("ücgen kac derece : "))
if total == 180:
    print("bu bir üçgendir şimdi hangi tür olduğunu bulunuz")
    if  aci1 == aci2 == aci3 :
        print("bu bir eşkenar üçgendir")
elif aci1 == aci2 or aci1 == aci3 or aci2 == aci3 :
    print("bu bir ikiz kenar üçgendir")
else:
    print("bu bir çeşit kenar üçgendir")