def get_user_information():
    user_name = input("Kullanıcı Adınızı Giriniz: \n")
    working_year = int(input("Kaç Yıl Çalıştınız: \n"))
    received_wage = int(input("Aldığınız Maaşı Giriniz: \n"))
    return user_name,working_year,received_wage

def increased_salary(user_name,working_year,received_wage):

    if working_year <= 5:
            interest = received_wage /10*100
            print("Sayın" ,user_name ,"Zamlı Maaşınız",interest,"TL'dir")

    elif working_year >= 6 and working_year <= 10 :
            interest = received_wage  /15*100
            print("Sayın" ,user_name ,"Zamlı Maaşınız",interest,"TL'dir")

    elif working_year >= 11 :
            interest = received_wage /25*100
            print("Sayın" ,user_name ,"Zamlı Maaşınız",interest,"TL'dir")
            return increased_salary()

            

user_name1,working_year1,received_wage= get_user_information()
increased_salary(user_name1,working_year1,received_wage)  