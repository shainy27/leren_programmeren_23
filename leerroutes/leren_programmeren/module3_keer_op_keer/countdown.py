
from multiprocessing import Event
import time

while True:
    try:
       cd = int(input("Hoelang moet de countdown zijn?"))
       break
    except:
        print("Voer een geldig aantal seconden in!")

for i in range(10,0,-1):
    Event().wait(1)
    print(f"{i} Seconds")
    # print(str(cd - i), "Seconds")
    

Event().wait(1)
print("Launching!")




