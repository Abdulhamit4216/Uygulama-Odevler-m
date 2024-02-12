toplam = 0
adet = 0

while True:
      sayi = input("Bir Sayı Girin (Çıkmak İçin 1'e Basın): ")
      if sayi == '1':
            break
      elif sayi.isdigit():
            toplam += float(sayi)
            adet += 1
      else:
            print("Geçersiz giriş lütfen başka bir saayı gırın. ")
            
if adet > 0:
      ortalama = toplam/adet
      print(f"Girilen Sayının Ortalaması: {ortalama}")
else:
      print("hiç sayı girilmedi")   