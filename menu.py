# if another program says "import menu"
# then it starts to read and execute this file... line 4, it defines "menu"... line 13, the "if" is False, so its body doesn't run

# if we run this program from the command line
# then it starts to read and execute the file... when it reaches line 16, the "if" is True, so we invoke `menu` and get a reuslt, which we print

def menu(choices):
    while True:
        user_choice = input(f'Enter choice from {choices}: ').strip()
    
        if user_choice in choices:
            return user_choice
    
        print(f'Invalid choice; try one of {choices}')

if __name__ == '__main__':   # __name__ is a variable, '__main__' is a string -- if this is true, we're running standalone (i.e., no import)
    c = menu(['strawberry', 'peach', 'apple'])

    print(f'You chose {c}')