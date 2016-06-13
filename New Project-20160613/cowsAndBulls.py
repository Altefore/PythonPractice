# Cows and Bulls!
# 1) user guesses a random number given by the computer in as few guesses as possible!
# 2) for every correct digit in the wrong place, the user gets a cow
# 3) for every correct digit in the right place, the user gets a bull
# 4) user must input a 4 digit integer to play the game

import random

tries = 0

def cows_and_bulls():
    random_number = random.randint(1000,9999)
    #print(str(random_number))
    user_number = 0
    while user_number != random_number:
        user_number = input("Please enter a four digit number: ")
        if isinstance(user_number, int): 
            global tries 
            tries += 1
            print("Tries: %d" %tries)
            print(number_check(user_number, random_number))
        else:
            print("You did not enter an integer...")
        
    
def number_check(user_number, random_number):
    cows = 0
    bulls = 0
    if user_number > 9999 or user_number <= 999:
        return "The number you entered was not 4 digits long..."
    if user_number == random_number:
        return "cows: 0, bulls: 4\nYou win!!"
    user = [int(i) for i in str(user_number)]
    random = [int(i) for i in str(random_number)]
    for i in xrange(len(user)):
        if user[i] == random[i]:
            bulls += 1
    
    for i in xrange(len(user)):
        for j in xrange(len(user)):
            if user[i] == random[j] and i != j:
                cows += 1
                break
        
    return "Cows: " + str(cows) + ", Bulls: " + str(bulls) 
    
if __name__ == "__main__":
    cows_and_bulls()
