def menu(choices):
    while True:
        user_choice = input(f'Enter choice from {choices}: ').strip()
    
        if user_choice in choices:
            return user_choice
    
        print(f'Invalid choice; try one of {choices}')

if __name__ == '__main__':   # __name__ is a variable, '__main__' is a string -- if this is true, we're running standalone (i.e., no import)
    c = menu(['strawberry', 'peach', 'apple'])

    print(f'You chose {c}')