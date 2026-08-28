import random

def guess(num, attempts):
    while attempts > 0:
        guessed_num = int(input("Make a guess: "))
        if guessed_num > 100 or guessed_num < 1:
            print("Guess a number between 1 to 100.")
            attempts -= 1
        elif guessed_num == num:
            print(f"You got it! The answer was {num}")
            return
        elif guessed_num > num:
            print("Too High\nGuess Again.")
            attempts -= 1
        elif guessed_num < num:
            print("Too Low\nGuess Again.")
            attempts -= 1
        else:
            print("Guess Again.")

        print(f"You have {attempts} attempts remaining to guess the number.")

    print(f"You've run out of guesses, the number was {num}.\nRefresh the page to run again.")



print(r'''  ________                              ___________.__              _______               ___.                 
 /  _____/ __ __   ____   ______ ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/                  \/     \/          \/            \/    \/     \/       
      ''')

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == "easy":
    attempts = 10
    print(f"You have {attempts} attempts remaining to guess the number.")
elif difficulty == "hard":
    attempts = 5
    print(f"You have {attempts} attempts remaining to guess the number.")
else:
    print("Invalid Input.")

chosen_num = random.randint(1,100)

guess(chosen_num, attempts)
