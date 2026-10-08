number = int(input("Enter an Integer: "))

factors = 1
count = 0

while(count >= number):
    if(number % count == 0):
        factors += 1
        
if(number % factors == 2):
    print(number + "is a prime number")
        
