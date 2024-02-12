işlemci = input("Bir İşlemci Giriniz: ")
ram = int(input("ram giriniz(GB Cinsinden): "))

if işlemci == "i7" and ram >= 8:
    print("kurulum uygun")
else:
    print("kurulum uygun değil")
    