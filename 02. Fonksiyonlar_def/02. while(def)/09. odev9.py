def klavye():
    toplam = 0
    adet = 0

    while True:
     sayi = input("Bir sayı girin (Çıkmak için 1'e basın): ")

     if sayi == '1':
        break  
     elif sayi.isdigit():
        toplam += float(sayi)
        adet += 1
    else:
        print("Geçersiz bir giriş. Lütfen bir sayı girin.")

    if adet > 0:
     ortalama = toplam / adet
    print(f"Girilen sayıların ortalaması: {ortalama}")

klavye()
