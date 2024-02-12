kg = float(input("valiz ağırlığını giriniz: "))
ek_ücret = (kg - 20)*10

if kg > 20:
    print("ek ücret dahildir:",ek_ücret)
else:
    print("ek ücret dahil değildir")