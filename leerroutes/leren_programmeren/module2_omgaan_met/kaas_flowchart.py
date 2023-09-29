vraag_1 = input("is de kaas geel")

if vraag_1 == "ja":
    vraag_2 = input("Zitten er gaten in?")
    if vraag_2 == "ja":
        vraag_3 = input("Is de kaas belachelijk duur?")
        if vraag_3 == "ja":
            print("Emmenthaler")
        if vraag_3 == "nee":
            print("Leerdammer")   
             
    if vraag_2 == "nee":
        vraag_4 = input("Is de kaas hard als steen?")
        if vraag_4 == "ja":
            print("Parmigiano Regiano")
        if vraag_4 == "nee":
            print("Goudse Kaas")

if vraag_1 == "nee":
    vraag_2 = input("Heeft de kaas blauwe schimmel")
    if vraag_2 == "nee":
        vraag_3 = input("Heeft de kaas een korst?")
        if vraag_3 == "nee":
            print("Mozarella")
        if vraag_3 == "ja":
            print("Camembert")   
    
    if vraag_2 == "ja":
        vraag_4 = input("Heeft de kaas een korst?")
        if vraag_4 == "ja":
            print("Blue de rochbaron")
        if vraag_4 == "nee":
            print("Foume d'Ambert")    





