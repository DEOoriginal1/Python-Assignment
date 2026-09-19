favourite_colour = "blue"
for index in range (3):
    guess = input("Guess your favourite colour: ")
    
    if guess == favourite_colour:
        print("correct")
        break
    elif guess == "green":
        print("close!")
        
    else:
        print("wrong")
            
            
            
