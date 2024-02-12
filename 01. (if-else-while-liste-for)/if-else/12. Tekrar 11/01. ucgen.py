acı1 = float(input("acı1 ın acısını gırınız: "))
acı2 = float(input("acı2 nın acısını giriniz: "))
acı3 = float(input("acı3 un acısını giriniz: "))

if acı1 == acı2 == acı3 :
    print("Bu Bir Eşkenar Üçgendir")
elif acı1 == acı2 or acı1 == acı3 or acı2 == acı3 :
    print("bu bir ikiz kenar üçgendir")
else :
    print("bu bir çeşit kenar ücgendir")

