import random

while True:
    number = random.randint(1, 50)
    attempts = 0

    print("\nI have selected a number between 1 and 50.")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("Too low! Try again.")

        elif guess > number:
            print("Too high! Try again.")

        else:
            print("Correct! You guessed the number.")
            print("Number of attempts:", attempts)
            break

    play_again = input("Do you want to play again? (yes/no): ")

    if play_again.lower() != "yes":
        print("Game Over!")
        break

    random.randint(1, 100)
# Computer 1 se 100 ke darmiyan koi bhi random number select karta hai.
# while True
# Loop game ko repeatedly chalane ke liye use hota hai.
# input()
# User se guess lene ke liye use hota hai.
# attempts += 1
# Har guess ko count karta hai.
# if guess < number
# Agar guess chota ho → Too low.
# elif guess > number
# Agar guess bara ho → Too high.
# else
# Agar guess aur computer ka number same ho → Correct.
# break
# Correct answer milne par guessing loop stop karta hai.
# play_again
# User se poochta hai ke dobara game khelna hai ya nahi.