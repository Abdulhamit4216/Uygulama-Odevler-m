def take_weight():
    luggage = int(input("Bagajınızın Ağırlığını Giriniz: \n"))
    return luggage

def price(luggage):
    if luggage <= 20 :
        print("Herhangi Bir Ücret Ödemenize Gerek Yok\n"
            "İyi Yolculuklar Dileriz...")
    else:
        luggage += 1*10
        print("Ödemeniz Gereken Miktar",luggage,"TL\n\n"
               "İyi Yolculuklar Dileriz...")

luggage = take_weight()
price(luggage)
