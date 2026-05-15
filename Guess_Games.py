secret_word = "Abeera"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word:

    if guess_count < guess_limit and not out_of_guesses:
        guess = input("Guess a word:")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses. YOU LOSE!")
else:
    print("you win!")