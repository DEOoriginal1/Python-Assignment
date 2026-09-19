player_1 = input("Choose: ")
player_2 = input("Choose: ")

style_1 = "Rock"
style_2 = "Scissors"
style_3 = "Paper"


if player_1 == style_1 and player_2 == style_2:
    print ("Player 1 wins")
if player_1 == style_3 and player_2 == style_1:
    print ("Player 1 wins")
if player_1 == style_2 and player_2 == style_3:
    print ("Player 1 wins")
if player_2 == style_1 and player_1 == style_2:
    print ("Player 2 wins")
if player_2 == style_3 and player_1 == style_1:
    print ("Player 2 wins")
if player_2 == style_2 and player_1 == style_3:
    print ("Player 2 wins")
else:   
     print ("Tie")




