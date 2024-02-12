def plaka_kodu():
    plaka = input("Bir Plaka Kodu Giriniz: \n")
    return plaka
def tespit(plaka):
    if plaka == "06":
        print("Girdiğiniz Plakanın Şehri Ankara")
    elif plaka == "07":
        print("Girdiğiniz Plakanın Şehri Antalya")
    elif plaka == "08":
        print("Girdiğiniz Plakanın Şehri Artvin")
    else: 
        print("Türkiye")
    
plaka = plaka_kodu()
tespit_2 = tespit(plaka)