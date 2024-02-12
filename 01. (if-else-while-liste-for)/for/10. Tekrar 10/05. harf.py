
ifade = input("Bir ifade girin: ")
aranan_harf = input("Aranacak harfi girin: ")


harf_sayisi = 0
for saYI in ifade:
    if saYI == aranan_harf:
        harf_sayisi += 1
print("Girilen ifadede  aranacak harf ", harf_sayisi, " kez bulunmaktadır.")
    