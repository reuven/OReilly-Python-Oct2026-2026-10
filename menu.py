def menu(choices):
    while True:
        user_choice = input(f'Enter choice from {choices}: ').strip()
    
        if user_choice in choices:
            return user_choice
    
        print(f'Invalid choice; try one of {choices}')