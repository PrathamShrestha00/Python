import random


def play_number_guessing_game():
    print("Welcome to the Number Guessing Game!")

    total_wins = 0
    total_losses = 0

    while True:
        print("\nSelect a difficulty level:")
        print("1. Easy (Unlimited guesses)")
        print("2. Medium (6 guesses)")
        print("3. Hard (4 guesses)")

        while True:
            try:
                difficulty = int(input("Enter difficulty (1 for Easy, 2 for Medium, 3 for Hard): "))
                if difficulty in [1, 2, 3]:
                    break
                else:
                    print("Invalid choice. Please select 1, 2, or 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Set the range and max guesses based on difficulty
        number_to_guess = random.randint(1, 100)
        max_guesses = float('inf') if difficulty == 1 else 6 if difficulty == 2 else 4

        print("\nI've picked a number between 1 and 100. Can you guess it?")
        if difficulty != 1:
            print(f"You have {max_guesses} guesses. Good luck!")

        guesses_taken = 0
        game_won = False

        while guesses_taken < max_guesses:
            remaining_guesses = max_guesses - guesses_taken - 1  # Calculate remaining guesses

            try:
                guess = int(input("Enter your guess: "))
                guesses_taken += 1

                if guess < number_to_guess:
                    print("Too low!")
                elif guess > number_to_guess:
                    print("Too high!")
                else:
                    print(f"Congratulations! You guessed the number in {guesses_taken} tries.")
                    total_wins += 1
                    game_won = True
                    break

            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if guesses_taken < max_guesses:
                print(f"You have {remaining_guesses} guesses left.")
            else:
                print(f"Sorry, you've used all your guesses. The number was {number_to_guess}.")
                total_losses += 1

        # Ask if the player wants to play again
        while True:
            play_again = input("\nDo you want to play again? (yes or no): ").strip().lower()
            if play_again in ['yes', 'no']:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        # Display total wins and losses
        print(f"\nTotal Wins: {total_wins}")
        print(f"Total Losses: {total_losses}")

        if play_again == 'no':
            print("Thank you for playing! Goodbye!")
            break


# Start the game
if __name__ == "__main__":
    play_number_guessing_game()
