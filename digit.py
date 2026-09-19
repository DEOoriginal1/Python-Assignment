character = input("Enter a single character: ")

if character.isdigit():
    print("It is a digit")
elif character.isalpha():
    print("It is a letter")
else:
    print("It is a special symbol")
