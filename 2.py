import random

def guess_the_number():
    print("Welcome to the Number Guessing Game!")
    print("Choose a difficulty level: Easy, Medium, Hard")

    difficulty = input("Enter difficulty: ").strip().lower()
    if difficulty == "easy":
        max_number = 10
        max_attempts = 5
    elif difficulty == "medium":
        max_number = 50
        max_attempts = 7
    elif difficulty == "hard":
        max_number = 100
        max_attempts = 10
    else:
        print("Invalid choice. Defaulting to Medium difficulty.")
        max_number = 50
        max_attempts = 7

    number_to_guess = random.randint(1, max_number)
    attempts = 0

    print(f"I'm thinking of a number between 1 and {max_number}. You have {max_attempts} attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"🎉 You guessed it in {attempts} attempts. Well done!")
                return
        except ValueError:
            print("⚠️ Invalid input. Please enter a number.")

    print(f"❌ Sorry, you're out of attempts. The number was {number_to_guess}.")

# Run the game
guess_the_number()
