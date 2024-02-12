while True:
    password = input("8 karakteri olan bir şifre girin:  ")
    
    if len(password) == 8:
        print("Şifreniz kaydedildi")
        break
    else :
        print("Şifreniz 8 karakterli olmalıdır")