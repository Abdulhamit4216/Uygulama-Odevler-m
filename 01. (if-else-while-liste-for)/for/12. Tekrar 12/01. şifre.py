while True:
    şifre = input("Lütfen 8 karakterlik bir şifre giriniz: ")

    if len(şifre) == 8:
        print("Şifreniz kaydedildi.")
        break
    else:
        print("Şifreniz 8 karakter olmalıdır.")

