number_one = int(input("Enter an integer: "))
number_two = int(input("Enter an integer: "))

if number_one > 0 and number_two > 0:
    print ("Happy")
if number_one < 0 and number_two > 0:
    print ("Sad")
if number_one < 0 and number_two < 0:
    print ("Joyful")
if number_one > 0 and number_two < 0:
    print ("Delighted")
if number_one == 0 and number_two == 0:
    print ("Origin")
if number_two ==0 and number_one != 0:
    print ("Number one Axis")
if number_one ==0 and number_two != 0:
    print ("Number two Axis")





