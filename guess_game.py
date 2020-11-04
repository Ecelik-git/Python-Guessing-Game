#number guessing game
import random #importing random module
number= random.randint(0, 100)
#any number between 0 and 100
guess = None
Try=0
running = True
while running:#while loop to check the number
    guess = int(input("enter a number between 0 and 100: "))
    #users need to enter a number
    if guess < number:
        print("wrong!, it is low")
    elif guess>number:
        print("wrong!, it is high")
    elif guess==number:
        print("yes! you guessed it!")
        if Try<2:
            print("impressive! you guessed it only " % str(Try))
        elif Try>2 and Try<10:
            print("you are pretty good")
        elif Try>10:
            print("%s tries to guess the number" % str(Try))
        running=False
    Try +=1



