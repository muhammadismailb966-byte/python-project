import random

user_score = 0
computer_score = 0

while True:
    print("\nRock, Paper, Scissors")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    user = input("Enter your choice: ").lower()

    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)

    print("Computer chose:", computer)

    if user not in choices:
        print("Invalid choice! Try again.")
        continue

    if user == computer:
        print("It's a tie!")

    elif user == "rock" and computer == "scissors":
        print("You win!")
        user_score += 1

    elif user == "paper" and computer == "rock":
        print("You win!")
        user_score += 1

    elif user == "scissors" and computer == "paper":
        print("You win!")
        user_score += 1

    else:
        print("Computer wins!")
        computer_score += 1

    print("Your score:", user_score)
    print("Computer score:", computer_score)

    play_again = input("Play again? (yes/no): ")

    if play_again.lower() != "yes":
        print("\nGame Over!")
        print("Final Your Score:", user_score)
        print("Final Computer Score:", computer_score)
        break

    # Computer list mein se koi aik choice randomly leta hai.

# 3. input() User apni choice enter karta hai.

# 4. Conditions if / elif / else

# Winner decide karne ke liye conditions use hoti hain.
# Rock > Scissors
# Paper > Rock
# Scissors > Paper

# 5. Score
# user_score += 1
# computer_score += 1

# Jo player round jeetta hai uska score 1 barh jata hai.

# 6. while True
#  Jab tak user game continue karta hai, naye rounds chalte rehte hain.

#  User dobara nahi khelna chahe to game end ho jata hai.
