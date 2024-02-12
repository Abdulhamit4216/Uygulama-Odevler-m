name = input("Lütfen Kullanıcı Adınızı Giriniz: ")
year = float(input("Lütfen Kaç Yıl Çalıştığınızı Giriniz: "))
wage = int(input("Lütfen Aldığınız Maaşı Giriniz: "))


    
if 0 < year < 5 :
        zam = 0.10
elif 6 < year < 10 :
        zam = 0.15
elif year >= 11 :
        zam = 0.25

zam_oranı = zam * wage
zam_miktarı = zam_oranı + wage
print("sayın ",name,"maaşınız zamdan sonra",zam_miktarı)