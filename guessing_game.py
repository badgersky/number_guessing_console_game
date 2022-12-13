from random import randint


def game_loop():
    """main game loop"""
    available_tries = 8
    number = randint(1, 100)
    tries = 1
    while True:
        try:
            guess = get_input()
            if tries == available_tries:
                return f'You are out of tries, The number was {number}.'
            else:
                result = check_guess(guess, number)
                if result:
                    return f'You win!'
            tries += 1
        except ValueError:
            msg = f'Enter an integer!'
            print(msg)


def get_input():
    guess = int(input('Enter your guess: '))
    return guess


def check_guess(guess, number):
    if guess < number:
        msg = f'To small, try again.'
        print(msg)
    elif guess > number:
        msg = f'To big, try again.'
        print(msg)
    else:
        return True


if __name__ == '__main__':
    print(game_loop())