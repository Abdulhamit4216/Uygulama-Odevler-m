def username():
    user_name = input("Kullanıcı Adınızı Giriniz: ")
    return user_name

def password():
    pass_word = input("Şifrenizi Giriniz: ")
    return pass_word

def verification(username,password):
    if username == "TIKI":
        print("Giriş Başarılı")
    if password == "0382":
        print("Giriş Başarılı")
    else:
        print("Kullanıcı Adı Veya Şifre Hatalı")

user = username()
password = password()
verification(user,password)