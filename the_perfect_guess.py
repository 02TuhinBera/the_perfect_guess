import random    # importing random module to genertae random int value
rand_number = random.randint(1, 100)   # randomly generated value will be between 1 - 100 
                                       # generating random value and stored it into the variable
# print(rand_number)   -->  hiding from u

user_guess = None
guesses = 0          # initializing the guess number to 0

while(user_guess != rand_number):    # condition for while loop
    user_guess = int(input("Enter your number: "))    # taking the input of the number that u have guessed
    guesses += 1
    if(user_guess == rand_number):
        print("You guessed it right ! Nice work !")
    else:
        if(user_guess > rand_number):
            print("You guesses it wrong ! Think small !")
        else:
            print("You guessed it wrong ! Think high !")  
        
print(f"You guessed the number in {guesses} attempts.")    # print it how many attempts does u take

with open("highscore.txt", "r") as f:          # read the highscore.txt file to check the score
    highscore = int(f.read())
    
if(guesses < highscore):
    print("You have just broken the high score!")
    with open("highscore.txt", "w") as f:      # rewrite ur score into the highscore.txt file, if u guess it less attempts than others
        f.write(str(guesses))