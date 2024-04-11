import random

def guess_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to Guess the Number game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} correctly!")
            print(f"It took you {attempts} attempts.")
            break

    play_again = input("Do you want to play again? (yes/no): ")
    return play_again.lower() == "yes"

if __name__ == "__main__":
    while True:
        if not guess_number():
            print("Thanks for playing!")
            break

