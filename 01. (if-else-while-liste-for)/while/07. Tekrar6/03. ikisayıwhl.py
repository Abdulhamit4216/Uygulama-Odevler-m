start = int(input("Başlangiç sayisini girin: "))
finish = int(input("Bitiş sayisini girin: "))
total = 0
number =  start

while number <=  finish:
    total += number
    number += 1

print("ilk sayı ve son sayı toplamı :",total)