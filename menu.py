def menu(choices):
    user_choice = input('Enter choice: ').strip()

    if user_choice in choices:
        return user_choice

    print(f'Invalid choice; try one of {choices}')