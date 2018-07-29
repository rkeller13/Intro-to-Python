
#Lucky Sevens program requirements
#input - amount of money put into pot
#loops until the pot is gone
#output - print the number of total rolls (loops)
#output - print the maximum amount of money in the pot

#six ways to get 7, win $4
#thirty ways to get else, lose $1

#import random library module
import random

#player's money into pot, using int since you lose a $1 with each
#losing roll, so it would be pointless(and not allowed) to use less than $1
monIn = int(input("How much money do you want to lose?: $"))

#roll counter
rollCt = 0

#max pot
potMax = monIn

#loop through random rolls and add/subtract money
while monIn > 0:
    die1Roll = random.randrange(1, 7)
    die2Roll = random.randrange(1, 7)
    diceRoll = die1Roll + die2Roll
    print("\nYou rolled a " + str(diceRoll))
    rollCt += 1
    if diceRoll == 7:
        print("You win $4!!!")
        monIn += 4
        if potMax < monIn:
            potMax = monIn
        print("The total amount in the pot is $" + str(monIn))
    else:
        print("You lose $1...")
        monIn -= 1
        print("The total amount in the pot is $" + str(monIn))

#print total number of rolls
print("\nYou lost all your money in only " + str(rollCt) + " rolls!")

#print max money in pot
print("\nThe max amount in the pot was $"+ str(potMax) +
", you should have stopped while you were ahead.")
