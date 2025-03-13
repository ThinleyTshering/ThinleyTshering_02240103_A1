import random


def guess_number_game():
    lower_limit = 1
    upper_limit = 100
    number_to_guess = random.randint(lower_limit, upper_limit)

    print(f"\nWelcome to guess the number game")
    print(f"I'm thinking of a number between {lower_limit} and {upper_limit}")

    while True:
        try:
            user_guess = int(input("Enter your guess: "))

            if user_guess < lower_limit or user_guess > upper_limit:
                print(
                    f"Please guess a number between {lower_limit} and {upper_limit}")
                continue

            if user_guess < number_to_guess:
                print("Too low Try again")
            elif user_guess > number_to_guess:
                print("Too high Try again")
            else:
                print("Congratulations you've guessed the number")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number")


def rock_paper_scissors_game():
    options = ["rock", "paper", "scissors"]

    print("\nWelcome to rock, paper, scissor")

    while True:
        user_choice = input(
            "Enter your choice(rock, paper, scissors) or 'quit' to exit: ").lower()

        if user_choice == 'quit':
            break

        if user_choice not in options:
            print("Invalid choice. Please choose rock, paper, or scissor")
            continue

        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win")
        else:
            print("You lose")


def main():
    while True:
        print("\nChoose a game: ")
        print("1. Guess the number")
        print("2. Rock, Paper, Scissor")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            guess_number_game()
        elif choice == '2':
            rock_paper_scissors_game()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please select 1,2, or 3")


main()
