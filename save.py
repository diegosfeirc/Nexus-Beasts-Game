def save_game(username: str, data_boards: list) -> None:
    '''
    This function receives a user and the boards of the game 
    to be saved and arranges them in such a way that they can 
    be put together again (by the split() function).
    '''
    path = f"games/{username}.txt"
    print(f"\nSaving {username}'s game...\n")
    with open(path, "w", encoding = "utf-8") as game:
        game.writelines(f"{username}")
        for table in data_boards:
            game.writelines("-")
            for row in table:
                for column in row:
                    game.writelines(f"{column}")
                    game.writelines(",")
                game.writelines(";")
    print("\nGame Saved Succesfully.\n")


def save_game_over(username: str, score: int) -> None:
    '''
    This function receives a user and their score at
    the end of a game and saves this information in 
    the scores.txt file. This information will be used for ranking.
    '''
    path = "scores.txt"
    with open(path, "a", encoding = "utf-8") as game:
        game.writelines(f"{username} - {score}\n")