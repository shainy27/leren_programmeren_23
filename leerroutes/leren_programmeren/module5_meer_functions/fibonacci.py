
def fibonacci_reeks(aantal):
    fib_list = [0,1]
    # Begint bij 2, omdat de list niet minder dan 2 heeft:
    for index in range(2, aantal):
        # Volgende getal in de reeks wordt de laatste + de een na laatste getal in de reeks
        volgend_getal = fib_list[index-2] + fib_list[index-1]
        # Zet het volgende getal in de list
        fib_list.append(volgend_getal)      
    return fib_list


aantal = 10

resultaat = fibonacci_reeks(aantal)
print(resultaat)

x = resultaat[-2]
y = resultaat[-1]
ratio = (y + x) / y
print(ratio)




    
