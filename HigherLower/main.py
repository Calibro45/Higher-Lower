import random

from art import logo, vs
from game_data import data


# create function, return a random element
def get_random_character():
    """ pass the list as a argument and return selected random character from list """
    character = random.choice(data)
    return character


def format_data(character):
    """ Pass the character as a argument and return the info of the character """
    name = character["name"]
    description = character["description"]
    country = character["country"]
    return f"{name}, a {description}, from {country}"


def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess
    and returns True if they got it right.
    Or False if they got it wrong."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(f"{logo}\n")
    score = 0
    game_should_continue = True
    account_a = get_random_character()
    account_b = get_random_character()

    while game_should_continue:
        # Make the B the new A and pick another B
        account_a = account_b
        account_b = get_random_character()
        # Check for duplicate
        while account_a == account_b:
            account_b = get_random_character()

        # print correct format
        print(f"Compare A: {format_data(account_a)}")
        print(f"{vs}\n")
        print(f"Against B: {format_data(account_b)}")

        # Ask user for a guess.
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        # Get follower count.
        a_follower = account_a["follower_count"]
        b_follower = account_b["follower_count"]
        # Check if user is correct.
        is_correct = check_answer(guess, a_follower, b_follower)

        # Clear screen between rounds.
        print("\n" * 100)
        print(f"{logo}\n")

        # print feedback and score
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_should_continue = False


game()
