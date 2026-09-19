integer_a = int(input ("Enter an integer: "))
integer_b = int(input ("Enter an integer: "))
integer_c = int(input ("Enter an integer: "))

largest = integer_a
if integer_b > largest:
    largest = integer_b
if integer_c > largest:
    largest = integer_c 

print (largest , "is the Largest Number")
