def preference_get():
    preference = input("Sinema mı?\nTiyatromu?\n")
    return preference


def verify_student():
    student = input("Öğrencimisiniz? (evet/hayır)\n")
    return student


def cinema(preference,student):
    price = 15
    if preference == "sinema":
        if student == "evet":
            price *= 0.5
            print("Ödenmesi Gereken Miktar",price,"TL")
        else:
            print("Ödemeniz Gereken Miktar",price,"TL")
        
    
def theatre(preference,student):
    price = 10
    if preference == "tiyatro" :
        if student == "evet":
            price *= 0.5
            print("Ödenmesi Gereken Miktar",price,"TL")
        else:
            print("Ödemeniz Gereken Miktar",price,"TL")


def çalıştır(preference_,student_):
    if preference == "sinema":
        cinema(preference_,student_)
    else:
        theatre(preference_,student_)
    



preference = preference_get()
verifystudent = verify_student()

çalıştır(preference,verifystudent)

