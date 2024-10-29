#Ryan Davies
#1255293
#Homework 2 Program Set 1
#This program generates a random lottery number, then asks the user for a guess.
#The program compares the guess to the random number, and returns a value depending on how many numbers are the same or in the same place.
#The program will loop forever unless the user inputs a flag with value -999.

#imports random for use in loop and initializes guess for use in the loop
import random
guess = 0

#loop will run until user has raised flag
while (guess != -999):
    #takes input from user and generates random 2 digit number
    lotto = int(random.randint(10, 99))
    guess = int(input("Enter your lottery pick (2 digits) or -999 to quit: "))

    #only does calculations and sends output if user flag is not raised
    if (guess != -999):
        
        #splits lotto and guess via integer math and remainder math
        lotto1 = lotto//10
        lotto2 = lotto%10
        
        guess1 = guess//10
        guess2 = guess%10

        #compares the values of the split lotto and guess variables
        compare = 0
        if (lotto1 == guess1 or lotto1 == guess2):
            compare += 1
        if (lotto2 == guess1 or lotto2 == guess2):
            compare += 1
        if (lotto == guess):
            compare += 1

        #checks the compare values and prints the result
        if (compare == 3):
            print("Exact match: you win $10,000!")
        elif (compare == 2):
            print("Match all digits: you win $3,000")
        elif (compare == 1):
            print("Math one digit: you win $1,000")
        else:
            print ("Sorry no match")
        print('')

##TEST RUN 1##
##Enter your lottery pick (2 digits) or -999 to quit: 44
##Sorry no match
##
##Enter your lottery pick (2 digits) or -999 to quit: 23
##Sorry no match
##
##Enter your lottery pick (2 digits) or -999 to quit: 68
##Sorry no match
##
##Enter your lottery pick (2 digits) or -999 to quit: 12
##Math one digit: you win $1,000
##
##Enter your lottery pick (2 digits) or -999 to quit: 45
##Sorry no match
##
##Enter your lottery pick (2 digits) or -999 to quit: -999


##TEST RUN 2##
##Enter your lottery pick (2 digits) or -999 to quit: 24
##Sorry no match
##
##Enter your lottery pick (2 digits) or -999 to quit: 11
##Math one digit: you win $1,000
##
##Enter your lottery pick (2 digits) or -999 to quit: 26
##Sorry no match
##
##Enter your lottery pick (2 digits) or -999 to quit: 77
##Sorry no match
##
##Enter your lottery pick (2 digits) or -999 to quit: 59
##Sorry no match
##
##Enter your lottery pick (2 digits) or -999 to quit: -999

##TEST RUN 3##
##Enter your lottery pick (2 digits) or -999 to quit: 89
##Sorry no match
##
##Enter your lottery pick (2 digits) or -999 to quit: 34
##Sorry no match
##
##Enter your lottery pick (2 digits) or -999 to quit: 27
##Sorry no match
##
##Enter your lottery pick (2 digits) or -999 to quit: 31
##Sorry no match
##
##Enter your lottery pick (2 digits) or -999 to quit: 26
##Sorry no match
##
##Enter your lottery pick (2 digits) or -999 to quit: 84
##Sorry no match
##
##Enter your lottery pick (2 digits) or -999 to quit: -999

##TEST RUN 4##
##Enter your lottery pick (2 digits) or -999 to quit: 57
##Sorry no match
##
##Enter your lottery pick (2 digits) or -999 to quit: 89
##Match all digits: you win $3,000
##
##Enter your lottery pick (2 digits) or -999 to quit: 73
##Sorry no match
##
##Enter your lottery pick (2 digits) or -999 to quit: 46
##Sorry no match
##
##Enter your lottery pick (2 digits) or -999 to quit: -999

##TEST RUN 5##
##Enter your lottery pick (2 digits) or -999 to quit: 94
##Match all digits: you win $3,000
##
##Enter your lottery pick (2 digits) or -999 to quit: 32
##Sorry no match
##
##Enter your lottery pick (2 digits) or -999 to quit: 47
##Match all digits: you win $3,000
##
##Enter your lottery pick (2 digits) or -999 to quit: 84
##Sorry no match
##
##Enter your lottery pick (2 digits) or -999 to quit: 35
##Sorry no match
##
##Enter your lottery pick (2 digits) or -999 to quit: 91
##Math one digit: you win $1,000
##
##Enter your lottery pick (2 digits) or -999 to quit: -999
