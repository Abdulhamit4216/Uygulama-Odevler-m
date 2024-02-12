def not_al():
    not1 = int(input("1. Notunuzu Giriniz:\n"))
    not2 = int(input("2. Notunuzu Giriniz:\n"))
    not3 = int(input("3. Notunuzu Giriniz:\n"))
    return not1, not2, not3

def ortalama_hesapla(not1, not2, not3):
    ortalama = (not1+not2+not3)/3
    if ortalama >= 50:
        print("Başarılı")
    else:
        print("Başarısız")
        

not1, not2, not3 = not_al()
ortalama = ortalama_hesapla(not1,not2,not3)
print(ortalama)