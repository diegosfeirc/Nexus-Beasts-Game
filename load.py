import os

def check_users_game(username: str) -> bool:
    '''
    This function checks if there is a saved game 
    associated with the username entered.
    '''
    path = f"games/{username}.txt"
    valid = False
    if os.path.isfile(path) == True:
        valid = True
    else:
        print(f"\nThere is no saved game associated with {username}\n")
        valid = False
    
    return valid


def load_game(username: str) -> list:
    '''
    This function receives a username 
    and loads the information of his incomplete game.
    '''
    data_game = [username]
    path = f"games/{username}.txt"
    print(f"\nLoading {username}'s game...\n")
    with open(path, "rt", encoding = "utf-8") as game:
        loaded_game_data = (game.readlines())[0]
    data_list = loaded_game_data.split("-")
    for num in range(1, 3):
        table = ((data_list[num]).split(";"))
        table.pop(-1)
        updated_table = []
        for row in table:
            table_row = row.split(",")
            table_row.pop(-1)
            updated_table.append(table_row)
        updated_table = str_to_integer(updated_table)
        data_game.append(updated_table)
    print("\nGame Loaded Successfully.\n")

    return data_game


def load_scores() -> list:
    '''
    This function open the file scores.txt and returns a list
    with all the usernames saved y their respective score.
    '''
    list_user_score = []
    with open("scores.txt", "rt", encoding = "utf-8") as game:
        user_score = game.readlines()
    for element in user_score:
        game_list = element.split(" - ")
        user = game_list[0]
        score = (game_list[1]).strip("\n")
        list_user_score.append([user, score])
    list_user_score = create_ranking(list_user_score)
    return list_user_score


def create_ranking(list_user_score: list) -> list:
    '''
    This function receives the list given in load_scores() and orders the scores
    from highest to lowest. Returns a list with the 10 best scores from highest 
    to lowest with their respective users.
    '''
    sorted_scores = sorted(list_user_score, key=lambda x: int(x[1]), reverse=True) 
    # We pass a lambda function as the 'key' parameter
    # to specify that the sorting should be done based 
    # on the numeric value of the score
    top_10_scores = sorted_scores[:10]
    return top_10_scores


def print_score_table(scores: list) -> None:
    '''
    This function receives the list with the ordered
    users and scores and prints the ranking of these
    '''
    print("\n       RANKING")
    print("---------------------")
    print("Username     | Score")
    print("---------------------")
    for index, score in enumerate(scores, start=1):
        username, points = score
        print(f"{index:2d}. {username:<12} | {points}")
    print("---------------------")


def str_to_integer(list_of_lists: list) -> list:
    '''
    This function receives a list of lists and transforms
    all digits in string format to integers. Returns the 
    list of modified lists
    '''
    new_list = []
    for sublist in list_of_lists:
        new_sublist = []
        for element in sublist:
            if element.isdigit():
                new_sublist.append(int(element))
            else:
                new_sublist.append(element)
        new_list.append(new_sublist)
    return new_list