fiyat1 = float(input("Birinci ürünü giriniz: "))
fiyat2 = float(input("İkinci ürünü giriniz: "))
toplam_fiyat = fiyat1+fiyat2

if toplam_fiyat <= 200:
    print("ödenecek tutar:",toplam_fiyat) 
else:

    indirim_miktarı = 25 * toplam_fiyat
    indirimli_fiyat = toplam_fiyat + indirim_miktarı
    print("ödenecek tutar,indirimli fiyatıyla",indirimli_fiyat,"TL'dir")