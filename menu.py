from parameters import num_for_column

class Menu:

    '''
    This class handles all the actions and information of the initial and game menu.
    '''

    def __init__(self, type) -> None:
        self.type = type


    def print_initial_menu(self) -> None:
        '''
        This method prints the initial menu.
        '''
        print("\nWELCOME TO NEXUS!\n")
        print("Select an option:")
        print("[1] New Game")
        print("[2] Load Game")
        print("[3] Ranking of Scores")
        print("[0] Quit\n")


    def print_game_menu(self) -> None:
        '''
        This method prints the game menu.
        '''
        print("\nSelect an option:")
        print("[1] Discover a Sector")
        print("[2] Save Game")
        print("[3] Save and Return to Initial Menu")
        print("[0] Return to Initial Menu (WITHOUT SAVE)\n")


    def validate_option(self, option: str) -> bool:
        '''
        This method checks if the character(s) entered by the user are valid as a response.
        Receives the user's response as a string and returns True if the character(s) are valid, and False if not.
        '''
        if option.isdigit() == True and int(option) in range(0, 4):
            valid = True
        else:
            valid = False
            print("\nPlease select a valid option (1, 2, 3 or 0).\n")
        return valid


    def ask_for_command(self) -> dict:
        '''
        This method ask the user to execute a command, until the command is valid.
        Returns a dictionary with a command to execute.
        '''
        valid = False
        while valid != True:
            response = input("")
            valid = self.validate_option(response)
        dict_response = self.handle_command(int(response))
        return dict_response


    def enter_username(self) -> str:
        '''
        This method ask the user to enter their username, until the username is valid.
        Returns the username as an string.
        '''
        valid_username = False
        while valid_username != True:
            username = input("\nEnter your Username:  \n")
            valid_username = self.validate_username(username)
        return username


    def validate_username(self, username: str) -> bool:
        '''
        This method checks if the username is valid or not.
        Receives the username, checks if it's alphanumeric and if it has an appropriate 
        length. Then it returns True if it's valid and False if it's not.
        '''
        valid = False
        if username.isalnum:
            if 0 < len(username) <= 10:
                valid = True
            else:
                print("\nPlease enter a non-empty username of 10 characters or less.\n")
        else:
                print("\nPlease enter an alphanumeric username.\n")
        return valid


    def handle_command(self, command: int) -> dict:
        '''
        This method handles the numeric command that the user enters
        and returns a dictionary with the response to execute.
        '''
        if self.type == "Initial":
            if command == 1 or command == 2:
                username = self.enter_username()
                if command == 1:
                    response = {'Game Type': "New"}
                else:
                    response = {'Game Type': "Created"}
                response['Username'] = username
                response['Command'] = "Open Game"
                self.type = "Game"
            else:
                if command == 3:
                    response = {'Command': "Open Score Ranking"}
                else:
                    response = {'Command': "Quit"}
        else:
            if command == 1:
                response = {'Command': "Discover a Sector"}
            elif command == 2:
                response = {'Command': "Save Game"}
            elif command == 3:
                response = {'Command': "Save And Go Back"}
                self.type = "Initial"
            else:
                response = {'Command': "Go Back"}
                self.type = "Initial"
        return response


    def ask_dimension(self, rows_or_columns: str) -> int:
        '''
        This method asks the user to enter a valid number of rows or columns of the board
        that he will use to play the game. It receives the string "rows" or "columns"
        '''
        valid_number = False
        while valid_number != True:
            number = input(f"\nChoose the number of {rows_or_columns} of the new board:  \n")
            valid_number = self.validate_dimensions(number)
            if valid_number == False:
                print("\nPlease choose a valid integer between 3 and 15.\n")
            else:
                return int(number)


    def validate_dimensions(self, number_dimension: str) -> bool:
        '''
        This method validates the dimensions supplied by the user. 
        Checks if the input, as a string, is an integer between 3 and 15. 
        If so, return True, if not, return False
        '''
        if number_dimension.isdigit() and 3 <= int(number_dimension) <= 15:
            return True
        else:
            return False


    def ask_row(self, visible_table: list) -> int:
        '''
        This method asks the user to enter a valid number of the row of the sector that he wants to discover.
        It receives the visible table and return the valid integer of the row"
        '''
        valid = False
        while valid != True:
            row = input("\nSelect the row of the sector you want to discover:  \n")
            valid = self.validate_row(row, visible_table)
            if valid == False:
                print("\nPlease select one of the valid numbers.")
        return int(row)

    
    def validate_row(self, row: str, visible_table: list) -> bool:
        '''
        This method checks whether the row number entered by the user is valid for the game board or not.
        If it's valid, it returns True, and if not, it returns False.
        '''
        if row.isdigit() and int(row) in range(0, len(visible_table)):
            return True
        else:
            return False

    
    def ask_column(self, visible_table: list) -> int:
        '''
        This method asks the user to enter a valid letter of the column of the sector that he wants to discover.
        It receives the visible table and return the valid integer of the column"
        '''
        valid = False
        while valid != True:
            column = input("\nSelect the column of the sector you want to discover:  \n")
            valid = self.validate_column(column, visible_table)
            if valid == False:
                print("\nPlease select one of the valid numbers.")
        return num_for_column[(column.upper())]


    def validate_column(self, column: str, visible_table: list) -> bool:
        '''
        This method checks whether the column letter entered by the user is valid for the game board or not.
        If it's valid, it returns True, and if not, it returns False.
        '''
        num_columns = len(visible_table[0])
        if len(column) == 1 and column.isalpha():
            column = num_for_column[(column.upper())]
            if column < num_columns:
                return True
            else:
                return False
        else:
            return False
    

    
    
