import random

words = ["python", "computer", "program", "gaming", "school"]
word = random.choice(words)

guessed_word = ["_"] * len(word)
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6
print("=== Welcome to Hangman ===")

while incorrect_guesses < max_incorrect and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Guessed Letters:", " ".join(guessed_letters))
    print("Remaining Incorrect Guesses:", max_incorrect - incorrect_guesses)

    guess = input("Enter a letter: ").lower()
 
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("Wrong!")
        incorrect_guesses += 1

if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The correct word was:", word)

