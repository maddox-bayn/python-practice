import random

import os

import data_higher_lower

score = 0
def display_acountinfo(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name} a {description} from {country}"

def check_answer(account1_followers, account2_followers):
    if account1_followers<account2_followers:
        if geuss == 1:
            return False
        else:
            return True
    else:
        if geuss == 1:
            return True
        else:
            return False
def game():        
    account_2 = random.choice(data_higher_lower.data)
    continue_flag = True
    while continue_flag:       
        account_1 = account_2
        account_2 = random.choice(data_higher_lower.data)
        while account_1 == account_2:
            account_2 = random.choice(data_higher_lower.data)    
        print(f"\nCompare 1: {display_acountinfo(account_1)}")
        print("\nVs")
        print(f"\nCompare 2: {display_acountinfo(account_2)}")
        geuss = int(input("Who has more follower? Type 1 or 2: "))
        acount1_followers = account_1['follower_count']
        acount2_followers = account_2['follower_count']
        is_correct = check_answer(acount1_followers,acount2_followers)
        os.system('cls')
        if is_correct == True:
            score += 1
            print(F"You are right. Your score is {score}")
        elif is_correct == False:
            score -= 1
            print(f"You are wrong. your score is {score}")
        else:
            if score == 0:
                print(f"You are wrong. Your final score is {score} ")
                continue_flag = False 
                return
game() 