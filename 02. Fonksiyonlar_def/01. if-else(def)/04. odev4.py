def buy_product():
    product1 = int(input("1. Ürünün Fiyatını Giriniz: \n"))
    product2 = int(input("2. Ürünün Fiyatını Giriniz: \n"))
    total = (product1 + product2)
    return total

def normal_price(total):
    if total <= 200:
        print("Ödemeniz Gereken Miktar",total,"TL")
    elif total >= 200 :
         total = total * 0.25
         print("Ödemeniz Gereken İndirimli Miktar",total,"TL")

total = buy_product()
normal_price(total)


