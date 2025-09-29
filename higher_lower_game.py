import random
import os

import data_higher_lower

score = 0
def display_acount_info(account):
    name = account["name"]
    description = account["description"]
    country=account["country"]
    return(f"{name}, a, {description}, from {country}")

def compare_answer(guess, highest_follower1, highest_follower2):
    if highest_follower1 < highest_follower2:
        if guess == 1:
            return False
        else:
            return True
    else:
        if guess == 1:
            return True
        else:
            return False
account_2 = random.choice(data_higher_lower.data)        
continue_flag = True        

while continue_flag:
    account_1 = account_2
    account_2 = random.choice(data_higher_lower.data)
    while account_1 == account_2:
        account_2 = random.choice(data_higher_lower.data) 
    print(f"\nCompare 1: {display_acount_info(account_1)}")
    print("\nvS")
    print(f"\nCompare 2: {display_acount_info(account_2)}")
    guess = int(input("\nWho has more followers? Type 1 or 2:  "))
    highest_follower1 = account_1["follower_count"]
    highest_follower2 = account_2["follower_count"]   
    is_correct = compare_answer(guess,highest_follower1, highest_follower2)
    os.system("cls")
    if is_correct:
        score += 1
        print(f"\nYou are right. your score is: {score}")
    else:
        print(f"\nYou are wrong... YOur final score is: {score}")
        continue_flag = False  