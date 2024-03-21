import random

def guess_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Initialize a variable to keep track of the number of guesses
    num_guesses = 0
    
    print("Welcome to the Guess the Number game!")
    print("I've chosen a number between 1 and 100. Can you guess it?")
    
    while True:
        # Get user's guess
        guess = int(input("Enter your guess: "))
        
        # Increment the number of guesses
        num_guesses += 1
        
        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You've guessed the number {secret_number} correctly!")
            print(f"It took you {num_guesses} guesses.")
            break
        elif guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")

if __name__ == "__main__":
    guess_number()
