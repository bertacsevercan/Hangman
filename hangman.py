
import random
import string

word_list = ["python", "java", "kotlin", "javascript"]

print("H A N G M A N\n")
lives = 8
comp_choice = list(random.choice(word_list))
hidden = "-" * len(comp_choice)
hidden_list = list(hidden)
empty = ""
guesses = []
menu = input('Type "play" to play the game, "exit" to quit:')

while lives > 0:
    if menu == "play":
        print("\n"+empty.join(hidden_list))
        guess = input("Input a letter:")
        if len(guess) > 1 or len(guess) == 0:
            print("You should print a single letter")
        elif guess not in string.ascii_lowercase:
            print("It is not an ASCII lowercase letter")
        elif guess in comp_choice:
            for i in range(len(comp_choice)):
                if guess == comp_choice[i]:
                    hidden_list[i] = guess
                i += 1
            if hidden_list == comp_choice:
                print(f"You guessed the word {empty.join(hidden_list)}!\nYou survived!")
                break
            if guess in guesses:
                print("You already typed this letter")
            guesses.append(guess)
        else:
            if guess not in guesses:
                print("No such letter in the word")
                lives -= 1
            elif guess in guesses:
                print("You already typed this letter")
            guesses.append(guess)
        if lives == 0:
            print("You are hanged!")

    elif menu == "exit":
        break
    else:
        menu = input('Type "play" to play the game, "exit" to quit:')
