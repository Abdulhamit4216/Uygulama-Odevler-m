while True:
    şifre = input("şifreniz 8 karakterli olmalıdır:")

    if len(şifre)== 8:
        print("Şifreniz Doğrulandı")
        break
    else: 
        print("8 karakterli  bi şifre girmediniz")