f1 = float(input("Birinci Ürünün Fiyatını Giriniz: "))
f2 = float(input("ikinici ürünü fiyatını giriniz:  "))
tf = f1+f2

if tf <= 200:
    print("ödencek tutar",tf)

else:
    indirim_miktarı = 25 * tf
    indirimli_fiyat = tf - indirim_miktarı
    print("ödenecek tutar,indirimli fiyatıyla",indirimli_fiyat)