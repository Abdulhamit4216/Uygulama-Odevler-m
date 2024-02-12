while True:
  
    sayi_str = input("Lütfen 1 ile 5 arasında bir sayı giriniz: ")

    if sayi_str.isdigit():
        sayi = int(sayi_str)

        if 1 <= sayi <= 5:
            if sayi == 3:
                print("3 sayısı girildi ve döngü sona erdi.")
                break
            else:
                print(f"Girdiğiniz sayı: {sayi}")
        else:
            print("Lütfen 1 ile 5 arasında bir sayı giriniz.")
    else:
        print("Geçersiz bir giriş yaptınız. Lütfen bir sayı giriniz.")