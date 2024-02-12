def açı_al():
    açı1 = int(input("1. açıyı giriniz: \n"))
    açı2 = int(input("2. açıyı giriniz: \n"))
    açı3 = int(input("3. açıyı giriniz: \n"))
    return açı1,açı2,açı3

def üçgen_çeşidini_bul(açı1,açı2,açı3):
    if açı1 == açı2 and açı2 == açı3 and açı1 == açı3:
        print("Bu bir eşkenar üçgendir")
    elif açı1 == açı2 or açı1 == açı3:
        print("Bu Bir İkizkenar Üçgendir")
    elif açı1 != açı2 and açı1 != açı3 and açı2 != açı3 :
        print("Bu bir çeşit kenar üçgendir")

acı1,acı2,acı3 = açı_al()
üçgen_çeşidini_bul(acı1,acı2,acı3)