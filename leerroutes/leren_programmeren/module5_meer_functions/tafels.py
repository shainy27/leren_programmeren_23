def my_function(num):
    for i in range(1,11):
        tafel = num * i
        print(f"{i} x {num} = {tafel}")
        
        
num = int(input("Van welk getal wilt u de tafel weten?:  "))
my_function(num)