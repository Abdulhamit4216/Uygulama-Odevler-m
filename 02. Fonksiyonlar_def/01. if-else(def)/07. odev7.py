
def enter_processor():
    processor = input("İşlemci Türünü Giriniz: ")
    return processor

def enter_ram():
    ram = int(input("Raminizi Giriniz: "))
    return ram

def control(enter_processor,enter_ram):
    if enter_processor >= "i7" and enter_ram >= 8:
        print("kurulum uygun")
    else:
        print("kurulum uygun değil")

pros = enter_processor()
ram = enter_ram()
control(pros,ram)