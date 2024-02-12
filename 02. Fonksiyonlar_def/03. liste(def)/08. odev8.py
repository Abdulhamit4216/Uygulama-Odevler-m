def lesson():
    ders = ["B","İ","L","İ","Ş","İ","M"]
    ders.sort
    print(ders)
    ders.reverse()
    print(ders)
    ders.reverse()
    print(ders)
    say = ders.count("İ")
    print(say)
    ders.pop(4)
    ders.pop(3)
    print(ders)
    ders.copy()
    print(ders)
    print(ders.index("L"))
    ders.clear()
    print(ders)
                        
    
lesson()