def parola ():
    while True:
     şifre = input("Şifreyi Giriniz: \n")
     if şifre == "python" or "Python":
        print("Giriş Başarılı")
        break
     else:
        print("Tekrar Deneyiniz")
        
parola()