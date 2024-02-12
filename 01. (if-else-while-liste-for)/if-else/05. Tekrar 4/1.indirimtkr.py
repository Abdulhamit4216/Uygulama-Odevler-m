fiyat1 = float(input("Birinci ürünün fiyatını giriniz: "))
fiyat2 = float(input("ikinci ürünün fiyatını giriniz: "))
toplam_fiyat = fiyat1+fiyat2 

if toplam_fiyat   <= 200:
    print("ödenecek miktar =",toplam_fiyat,"TL")
else:

    indirim_miktarı = 0.25 * toplam_fiyat
    indirimli_fiyat = toplam_fiyat - indirim_miktarı
    print("ödenecek miktar, indirimden sonra",indirimli_fiyat,"TL'dir")