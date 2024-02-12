def take_time():
    kalinan_sure = float(input("Otoparkta kaç saat kaldınız: \n "))
    return kalinan_sure


def take_price(kalinan_sure):
    if kalinan_sure <= 1:
        ucret = 5

    elif 1 < kalinan_sure <= 5:
        ucret = 5 + (kalinan_sure - 1) * 4
    else:
        ucret = 5 + (5 - 1) * 4 + (kalinan_sure - 5) * 3

    print(f"Ödemeniz gereken miktar: {ucret} TL")


take_T = take_time()
take_price(take_T)
