import random

import os
import data_higher_lower

score = 0
def display_chioce(accounts):
    name = accounts['name']
    description = accounts['description']
    country = accounts['country']
    return f"{name} a {description} from {country}"

def follower_count(guess, follower_account1, follower_account2):
    if follower_account1<follower_account2:
        if guess == 1:
            return False
        else:
            return True
    else:
        if guess == 1:
            return True
        else:
            return False
account2 = random.choice(data_higher_lower.data)
continue_flag = True
while continue_flag:
    account1 = account2
    account2 = random.choice(data_higher_lower.data)
    while account1 == account2:
        account2 = random.choice(data_higher_lower.data)
    print(f"\nCompare 1: {display_chioce(account1)}")

    print("\nVS")
    print(f"\nCompare 2: {display_chioce(account2)}")

    guess = int(input("\nWho has more followers? type '1' or '2': "))
    follower_account1 = account1['follower_count']
    follower_account2 = account2['follower_count']
    winner = follower_count(guess, follower_account1, follower_account2)
    if winner:
        os.system('cls')
        score += 1
        print(f"you are correct score is {score}")
    else:
        print(f"you loose XXX your score is {score}")
        continue_flag = False