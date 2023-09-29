
from multiprocessing import Event

num = 30

while num >=0:
    print(f"{num}seconden")
    Event().wait(1)
    num -= 1

print("Launching!")