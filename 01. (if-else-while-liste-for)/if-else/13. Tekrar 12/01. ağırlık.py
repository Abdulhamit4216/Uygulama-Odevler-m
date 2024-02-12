boy = float(input("boyunuzu(Metre Cinsinden)girin: "))
kilo = float(input("kilonuzu (kılogram cınsınden)giriniz: "))

vki = kilo /(boy*boy)

if 18 <= vki < 25:
    durum = "Normal"
elif 25 <= vki < 30:
    durum = "Kilolu"
elif 30 <= vki:
    durum = "Obez"
else:
    durum = "Bilinmeyen"

print("Vücut Kitle İndeksi (VKİ) =", vki)
print("Durum:", durum)
