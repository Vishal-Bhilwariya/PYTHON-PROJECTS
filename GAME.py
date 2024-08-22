""" Design a game between user and computer as follows:
 There are 51 balls in a basket.
 The user has to pick less than 5 balls from the basket at a time.
 Each user will be given his/her turn alternately.
 The user who picks the last ball will win the game.
 The first turn is of the user.
 Print who won """


print("<< |- GAME START -| >>\n")
import random
total_balls = 51

while True :
    print(" ->>| Choose total balls less than 5 |<<- ")
    while True :
        a = int(input("User's turn : "))
        if a <= 4 :
            break
    total_balls -= a
    
    if total_balls <= 1:
        print("<<<< USER WON >>>>")
        break
    
    while True :
        b = random.randint(1,4)
        print("Computer's turn :",b)
        if a <= 4 :
            break
   
    total_balls -= b
    if total_balls <= 1 :
        print("<<<< COMPUTER WON >>>>")
        break
    print("\nTOTAL BALL LEFT IN BASKET =>",total_balls,"\n")