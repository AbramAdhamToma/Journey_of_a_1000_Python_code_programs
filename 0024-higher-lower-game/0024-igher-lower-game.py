from art import logo, vs
from game_data import data
import random


""" Format the account data into printable format """
def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return (f"{account_name}, a {account_descr}, from {account_country}")


def check_answer(guess, a_follower, b_follower ):
    """Takes the account data and return the printable format."""
    if a_follower > b_follower:
        return guess == "a"
    else:
        return guess == "b"


# Display art 
# print(logo)
score = 0

# Make the game repeatable.
game_should_continue = True
account_b = random.choice(data)# this beacause we need to replace account A with B if B is the right and continue GAME

while game_should_continue:
    # # Generate a random account from the game data.
    account_a = account_b
    account_b = random.choice(data)
    
    while account_a == account_b: # for chicking if the 2 random choice  is equal or no
        account_b = random.choice(data)

    print(f"compare A:{format_data(account_a)}. ")
    # print(vs)
    print(f"compare A:{format_data(account_b)}. ")


    # Ask user for a guess.
    guess = input("who has more followers? Type 'A' or 'B': " ).lower()


    # check if user is correct.
    ## Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)


    # Give user feadback on their guess.
    # score Keeping
    if is_correct:
        score += 1
        print(f"You're right! Current Score: {score}. ")
    else:
        game_should_continue = False
        print(f"Sorry, That's Wrong. Final: {score}. ")
        












## Use if statement to cheack if user is correct.
    

















