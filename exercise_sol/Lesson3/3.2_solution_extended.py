import random

# Generate a random number between 1 and 20
secret_number = random.randint(1, 20)

print("Welcome to Guess the Number Game!")
print("I'm thinking of a number between 1 and 20. Can you guess it?")
print("You have 5 chances to guess.")

# Allow 5 chances to guess the number
for attempt in range(1, 6):
    # Ask the user to input their guess
    guess = int(input(f"Attempt {attempt + 1}: Enter your guess: "))
    
    #Correct answer
    if guess == secret_number:
        print(f"Congratulations! You guessed the correct number after {attempt} attempts!")
        break
        
    if random.randint(1, 2) == 1: #select response mode; 1: high/low; 2: distance
        if guess > secret_number:
            print("Your guess was too high!")
        else:
            print("Your guess was too low!")
    else:
        difference = abs(guess - secret_number)
        print(f"Your guess was between {difference - random.randint(1, 5)}-{difference + random.randint(1,5)} numbers away from the correct number!")
    if attempt == 5:
        print(f"Sorry, you've used all 5 chances. The secret number was {secret_number}.")

