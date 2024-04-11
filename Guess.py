import random

def guess_number(max_attempts):
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    print("Welcome to Guess the Number game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    attempts = 0
    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} correctly!")
            print(f"It took you {attempts} attempts.")
            return True

    print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {secret_number}.")
    return False

if __name__ == "__main__":
    while True:
        max_attempts = int(input("Enter the number of attempts you want to have: "))
        if guess_number(max_attempts):
            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() != "yes":
                print("Thanks for playing!")
                break
        else:
            play_again = input("Do you want to try again with a different number of attempts? (yes/no): ")
            if play_again.lower() != "yes":
                print("Thanks for playing!")
                break
