# Shelly Wang
# Date: Nov 7
# propose: to make the guess number game

import random

def get_number():
    secret = random.randint(1,100)                      # Generate a random number from 1 to 100
    return secret                                             # create a function get_number()，becaues it can have a total function



def main():                                                  # It can make this program work properly

    total_guesses = 0
    for loop in range(1,4):
        counter = 0
        secret = get_number()

        print(loop)
                                                               #  Go make this game three times
        while True:
            guess = int(input("Guess what I was thinking"))
            counter = counter + 1

            if guess == secret:
                print("you are right", "you try ", counter, "times")
                total_guesses = total_guesses + counter
                break
            elif guess < secret:
                print("the number is so small")
            else:
                print("the number is so big")
                                                              # Use while True, then loop through if, elif, and else. If once this is achieved, break the loop

    average_score = total_guesses/3
    print("You average score is", average_score)
    # to calu the average score
    # Ending.

main()





