import random

def guess_the_number_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    player_guess = None
    tries = 0

    print("Welcome to the Guess the Number Game!")
    print("Try to guess the secret number between 1 and 100.")

    while player_guess != secret_number:
        player_guess = int(input("What's your guess? "))
        tries += 1
        
        if player_guess < secret_number:
            print("Oops! Too low.")
        elif player_guess > secret_number:
            print("Oops! Too high.")
        else:
            print(f"Yay! You found the secret number in {tries} tries.")

if __name__ == "__main__":
    guess_the_number_game()
