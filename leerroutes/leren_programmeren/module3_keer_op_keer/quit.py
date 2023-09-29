
num = 0
no_quit = True

while no_quit:
    vraag = input("?").lower()
    if vraag != "quit":
        num = num + 1
    else:
        no_quit = False

print(f"De vraag werd {num} keer gesteld")
        
    
        
