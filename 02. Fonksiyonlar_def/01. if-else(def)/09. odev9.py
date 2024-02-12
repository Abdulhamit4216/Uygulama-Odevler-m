def sıcaklık_değerı():
    sıcaklık = int(input("Sıcaklık Değerini Giriniz: \n"))
    return sıcaklık

def sıcaklık_değeri_bulma(sıcaklık):
    if sıcaklık <= 5 :
        print("Hava Soğuk")
    elif  sıcaklık >= 6 and sıcaklık <= 14:
        print("Hava Ilık")
    elif sıcaklık >= 15:
        print("Hava Sıcak")

sıcaklık_yazdır = sıcaklık_değerı()
sıcaklık_değer_yazdır = sıcaklık_değeri_bulma(sıcaklık_yazdır)