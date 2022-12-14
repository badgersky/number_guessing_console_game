from random import randint


def game_loop():
    """main game loop"""
    available_tries = 8
    number = randint(1, 100)
    tries = 1
    while True:
        try:
            guess = int(input('Enter your guess: '))
            if tries > available_tries:
                return f'You are out of tries, The number was {number}.'
            elif check_guess(guess, number):
                return f'You win!'
            tries += 1
        except ValueError:
            print(f'Enter an integer!')


def check_guess(guess, number):
    """function checks if number is equal to players guess"""
    if guess < number:
        print(f'To small, try again.')
    elif guess > number:
        print(f'To big, try again.')
    else:
        return True


if __name__ == '__main__':
    print(game_loop())