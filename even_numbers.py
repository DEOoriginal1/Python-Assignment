def even_number(number):

    for index in range(1, number):
        if index % 2 == 0:
            print (index)
            
    return " "
   
def prime_number(number):

    for index in range(1, number):
        if number % index == 0:
            print (index)
            
    return " "
    
print(prime_number(10))
   

