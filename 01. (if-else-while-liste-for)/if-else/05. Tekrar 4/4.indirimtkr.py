fiyat1 = float(input("Birinci Ürünün Fiyatını Giriniz: "))
fiyat2 = float(input("İkinci Ürünün Fiyatını Giriniz: "))
toplam_fiyat = fiyat1 + fiyat2 
 
if toplam_fiyat <= 200:
    print("ödenecek tutar",toplam_fiyat)

else:

    indrim_miktarı = 25 * toplam_fiyat
    indirimli_fiyat = toplam_fiyat - indrim_miktarı
    print("ödenecek tutar,indirmli fiyatıyla",indirimli_fiyat)