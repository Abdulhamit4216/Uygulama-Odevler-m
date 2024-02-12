while True :
    şifere = input("Lütfen 8 Karakteri olan bir şifre giriniz: ")

    if len(şifere) == 8:
        print("Şifreniz Kaydedildi")
        break
    else:
        print("8 karakterli  bir şifre girmediniz")