def letter():
    expression = input("Lütfen bir ifade girin: \n")
    search_letter = input("Aranacak harfi girin: \n")

    counter = 0
    for harf in expression:
        if harf == search_letter:
            counter += 1

    print(f"'{search_letter}' harfi ifadede {counter} kez geçmektedir.")

letter()

