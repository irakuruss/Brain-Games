from brain_games.cli import welcome_user


def main():
    print('Welcome to the Brain Games!')
    user_name = welcome_user()
    return user_name
