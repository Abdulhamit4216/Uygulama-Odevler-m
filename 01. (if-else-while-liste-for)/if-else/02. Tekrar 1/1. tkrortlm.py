sinav1 = float(input("ilk sınav notunuzu giriniz: "))
sinav2 = float(input("ikinci sınav notunuzu giriniz: "))
performans_notu = float(input("performans notunuzu giriniz: "))

ortalama = (sinav1+sinav2+performans_notu) /3

if ortalama >= 50:
    input("başarılı")

else:
    input("başarısız")