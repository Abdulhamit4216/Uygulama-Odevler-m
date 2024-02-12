def get_number():
    number1 = int(input("Sayıyı Giriniz: \n"))
    return number1

def control(number1):
    if number1 %3 == 0 and number1 %5 == 0:
        print("15'e tam bölünür")
    else: 
        print("15'e tam bölünmez")

getnumber = get_number()
control(getnumber)


