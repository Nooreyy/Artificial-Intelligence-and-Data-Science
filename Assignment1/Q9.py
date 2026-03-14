'''Number Guessing Game

Program should:
Store a number (e.g., 7)
Ask user to guess
If guess is correct -> print "Correct"
Else -> print "Wrong"'''

number_to_guess = 7
guess = int(input("Guess the number: "))

for i in range(1, 4):
    if guess == number_to_guess:
        print("Correct")
        break
    else:
        print("Wrong")
        if i < 3:
            guess = int(input("Try again: "))