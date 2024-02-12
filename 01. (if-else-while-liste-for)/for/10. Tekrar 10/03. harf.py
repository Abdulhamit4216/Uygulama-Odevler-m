

ifade = input("Bir ifade girin: ")
aranacak_harf = input("Aranacak harfi girin: ")


harf_sayisi = 0
for karakter in ifade:
    if karakter == aranacak_harf:
        harf_sayisi += 1
print("Girilen ifadede  aranacak harf ", harf_sayisi, " kez bulunmaktadır.")
    