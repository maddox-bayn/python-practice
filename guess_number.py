# guess a number game

import random

EASY_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTEMPTS=5

def set_difficulty(level_chosen):
    if level_chosen == 'easy':
        return EASY_LEVEL_ATTEMPTS
    elif level_chosen == 'hard':
        return HARD_LEVEL_ATTEMPTS
    else:
        return
    
def check_answer(guessed_number, answer, attempt):
    if guessed_number < answer:
        print("your guess is too low")
        return attempt-1
    elif guessed_number > answer:
        print("your guess is too high")
        return attempt-1
    else:
        print(f"your guess is right.... The answer was {answer}")

def game():       
    print("let me think of a number between 1 to 50")
    answer = random.randint(1, 50)
    level = input("choose level of difficulty....Type 'easy' or 'hard': ")
    attempt = set_difficulty(level)
    if attempt != EASY_LEVEL_ATTEMPTS and attempt != HARD_LEVEL_ATTEMPTS:
        print(" You have entered wrong difficulty level... Play again!!.")
        return
    guessed_number = 0
    while guessed_number != answer:
        print(f"You  have {attempt} remaining to guess the number.")
        guessed_number = int(input("Guess a number: "))
        attempt = check_answer(guessed_number, answer, attempt)
        if attempt == 0:
            print('You are out of guesses....You lose')
            return
        elif guessed_number != answer:
            print("guess agian"     )
    

game()