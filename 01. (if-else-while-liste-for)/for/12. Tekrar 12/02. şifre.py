while True:
    şifre = input("Lütfen 8 Karakterli Bir Şifre Giriniz:")

    if len(şifre) == 8:
        print("Şifreniz Kaydedildi: ")
        break
    else:
       print("Lütfen 8 Karakterli Bir Şifre Girin\n")