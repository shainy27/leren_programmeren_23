#Tishainy Naar
#Pizza calculator


from socket import getprotobyname
from ssl import ALERT_DESCRIPTION_CERTIFICATE_UNOBTAINABLE


while True:
    afmeting = input("Kies de grootte van de pizza: small, medium, groot") # hier word er gevraagd welke afmeting de user wil
    if afmeting in ["small", "medium", "groot"]:
        break

aantal = int(input("Hoeveel pizzas wilt u?:")) #hier word er gevraagd hoeveel pizzas de user wil

if afmeting == "small":      
    prijs = 9.99
elif afmeting == "medium":
    prijs = 13.99
elif afmeting == "groot":
    prijs = 17.99
else:
    prijs = 0

    print("u heeft niet de juiste grootte gekozen. Proberr het opnieuw")    

totaalprijs = prijs * aantal #hier word de prijs bij elkaar opgeteld

print("----------------------------------------------------") #dit is het bonnetje
print("|  " ,aantal, afmeting, "pizzas:" ,totaalprijs ,"euro")
print("----------------------------------------------------")



    



     
