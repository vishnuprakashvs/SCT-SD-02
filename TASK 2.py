import random

def guess_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    print("Welcome to the Guess the Number game!")
    print("I have chosen a number between 1 and 100. Can you guess it?")
    
    attempts = 0
    while True:
        guess = int(input("Enter your guess (between 1 and 100): "))
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} correctly in {attempts} attempts!")
            break

if __name__ == "__main__":
    guess_number()
