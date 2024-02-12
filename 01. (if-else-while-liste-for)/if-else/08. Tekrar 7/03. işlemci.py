işlemci = input("Bir İşlemci Giriniz: "),
ram = int(input("Ram Giriniz(GB Cinsinden): "))
 
if işlemci == "i7" and ram >= 8:
    print("Kurulum Uygun")
else:
    print("Kurulum Uygun Değil")
    