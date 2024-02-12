fiyat1 = float(input("Birinici Ürünün Fiyatını Giriniz: "))
fiyat2 = float(input("İkinci Ürünün Fiyatını Giriniz: "))
toplam_fiyat = fiyat1+fiyat2

if toplam_fiyat <= 200:
    print("ödenecek miktar",toplam_fiyat)
else: 

    indirimli_miktarı = 25 * toplam_fiyat
    indirimli_fiyat = toplam_fiyat - indirimli_miktarı
    print("ödenecek tutar,indirimden sonra",indirimli_fiyat,"TL'dir")