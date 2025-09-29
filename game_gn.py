import random


EASY_LEVEL_ATTEMPT = 10
HARD_LEVEL_ATTEMPT = 5
def set_difficulty(level_choosen):
    if level_choosen == 'easy':
        return EASY_LEVEL_ATTEMPT
    elif level_choosen == 'hard':
        return HARD_LEVEL_ATTEMPT
    else:
        return

def check_answer(guessed_answer,answer,attempt):
    if guessed_answer < answer:
        print("your guess is too low")
        return attempt - 1
    elif guessed_answer > answer:
        print("yor guess is too high")
        return attempt - 1
    else:
        print(f"your guess is right the answer was {answer}")
        

def game():
    print("Let me think of a number between 1 too 50. And then you geuss it. ")

    answer = random.randint(1, 15)
    print(answer)
    level = input("choose your level of difficulty either 'easy' or 'hard': ")
    attempt = set_difficulty(level)
    if attempt == EASY_LEVEL_ATTEMPT and attempt == HARD_LEVEL_ATTEMPT:
        print(f"You have {attempt} chances to guesss the right answer. ")
    if attempt != EASY_LEVEL_ATTEMPT and attempt != HARD_LEVEL_ATTEMPT:
        print("You have entered a wrong dificulty level...play again")
        return
    guessed_answer = 0
    while guessed_answer != answer:
        guessed_answer = int(input("Make a guess: "))
        if guessed_answer != answer:
            print(f"wrong! You have {attempt - 1} chances to guesss the right answer. ")
        attempt = check_answer(guessed_answer,answer,attempt)
        if attempt == 0:
            print("You lose, you have guessed out your attempt")
            return
        elif guessed_answer != answer:
            print("play again")
        elif attempt != EASY_LEVEL_ATTEMPT and attempt != HARD_LEVEL_ATTEMPT:
            game()
            

game()