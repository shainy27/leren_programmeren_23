def my_function(n):
    newList = []
    # vanaf 1 tot n+1 (omdat het anders te vroeg stopt)
    for i in range(1, n+1):
        newList.append(f"Hello from function town {i}!")
    return newList     
     
loop = my_function(8)

# voor de lengte van de list voert het uit
for i in range (len(loop)):
    #print de positie in de list
    print(loop[i])


