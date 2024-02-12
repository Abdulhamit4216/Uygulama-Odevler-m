işlemci = input("işlemci türünü giriniz:  ")
ram = int(input("ram belleği girniz(gb cinsinden): "))

if işlemci == "i7" and ram >= 8:
         print("kurulum uygun")
else:
        print("kurulum uygun değil")