from menu import Menu
from table import Table
from math import ceil
from parameters import PROB_BEAST, POND_SCORE
from load import check_users_game, load_game, load_scores, print_score_table
from save import save_game_over, save_game

class Game:

    '''
    This class handles all the logic and flow of the game.
    '''

    def __init__(self) -> None:
        self.score = 0
        self.status = "Playing"
    

    def count_discovered_cells(self, visible_table: list) -> int:
        '''
        This method receives the visible board and counts the number
        of discovered cells.
        '''
        discovered_cells = 0
        for row in visible_table:
            for cells in row:
                if cells != " ":
                    discovered_cells += 1
                else:
                    continue
        return discovered_cells
    

    def play(self) -> None:
        '''
        This method handles ALL the logic of the game.
        '''
        while self.status == "Playing":
            menu = Menu("Initial")
            menu.print_initial_menu()
            command = menu.ask_for_command()
            if command['Command'] == "Open Game":
                self.username = command["Username"]
                while menu.type == "Game":
                    if command['Game Type'] == "New":
                        num_rows = menu.ask_dimension("rows")
                        num_columns = menu.ask_dimension("columns")
                        num_beasts = ceil(num_rows * num_columns * PROB_BEAST)
                        table = Table(num_rows, num_columns, num_beasts)
                        visible_table = table.visible_table
                        invisible_table = table.invisible_table
                    else:
                        self.username = command["Username"]
                        valid_user = check_users_game(command['Username'])
                        if valid_user:
                            loaded_game = load_game(command['Username'])
                            visible_table = loaded_game[1]
                            invisible_table = loaded_game[2]
                            num_rows = len(visible_table)
                            num_columns = len(visible_table[0])
                            num_beasts = ceil(num_rows * num_columns * PROB_BEAST)
                        else:
                            menu.type = "Initial"
                            break
                    num_cells = num_rows * num_columns
                    cells_to_discover = num_cells - num_beasts
                    discovered_cells = self.count_discovered_cells(visible_table)
                    while cells_to_discover > discovered_cells and menu.type == "Game":
                        self.print_table(visible_table)
                        menu.print_game_menu()
                        command = menu.ask_for_command()
                        if command['Command'] == "Discover a Sector":
                            response = self.discover_sector(menu, visible_table, invisible_table)
                            if response['Is Alive']:
                                if response['Status'] == "Sector discovered":
                                    discovered_cells += 1
                                    self.score = num_beasts * discovered_cells * POND_SCORE
                            else:
                                save_game_over(self.username, self.score)
                                menu.type = "Initial"
                        elif command['Command'] == "Save Game" or command['Command'] == "Save And Go Back":
                            save_game(self.username, [visible_table, invisible_table])
                    if cells_to_discover == discovered_cells:
                        self.print_winner(invisible_table)
                        save_game_over(self.username, self.score)  
            elif command['Command'] == "Open Score Ranking":
                scores_ranking = load_scores()
                print_score_table(scores_ranking)
            else:
                self.status = "Quit"


    def print_winner(self, invisible_table: list) -> None:
        '''
        This method is responsible for printing the corresponding 
        information when the user wins.
        '''
        self.print_table(invisible_table)
        print("\nCongratulations! You discovered all sectors without beasts!")
        print("YOU WON!!!\n")
        print(f"Username: {self.username} -- Score: {self.score}")
                    



    def discover_sector(self, menu: Menu, visible_table: list, invisible_table: list) -> dict:
        '''
        This method is in charge of managing the logic of discovering a sector and executing 
        what corresponds to each case. Returns a dictionary indicating whether the user is 
        still in the game and the status of his command.
        '''
        selected_row = menu.ask_row(visible_table)
        selected_column = menu.ask_column(visible_table)
        discovered_cell = self.check_discovered_sector(visible_table, invisible_table, selected_row, selected_column)
        if discovered_cell == False:
            is_beast = self.check_beast(selected_row, selected_column, invisible_table)
            if is_beast:
                return {'Is Alive': False}
            else:
                visible_table[selected_row][selected_column] = invisible_table[selected_row][selected_column]
                return {'Is Alive': True, 'Status': "Sector discovered"}
        else:
            return {'Is Alive': True, 'Status': "Already discovered"}


    def check_beast(self, selected_row: int, selected_column: int, table: list) -> bool:
        '''
        This method checks if there's a beast in the selected cell.
        Returns True if there is, and False if there isn't.
        '''
        if table[selected_row][selected_column] == "N":
            self.print_lost_game(table)
            return True
        else:
            return False

    
    def print_lost_game(self, invisible_table: list) -> None:
        '''
        This method is responsible for printing the corresponding 
        information when the user loses.
        '''
        self.print_table(invisible_table)
        print("\nYou found a Nexus beast and it attacked you!")
        print("You lose.\n")
        print(f"Username: {self.username} -- Score: {self.score}")
            

        
    def print_table(self, table: list) -> None:
        '''
        This method prints the game board on the user's console.
        '''
        n = len(table)
        m = len(table[0])
        table = [['■' if x == ' ' else x for x in y] for y in table]
        table = [[str(x) if isinstance(x, int) else x for x in y] for y in table]
        columns = ' ' * 5
        for index in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:m]:
            columns += f' {index}'
        print(columns)
        print(' ' * 4 + '┌' + '─' * (2 * m + 1) + '┐')
        for index in range(n):
            row = ''
            if index < 10:
                row += f'  {index} │'
            else:
                row += f' {index} │'

            row += ' ' + ' '.join(table[index]) + ' │'
            print(row)
        print(' ' * 4 + '└' + '─' * (2 * m + 1) + '┘')


    def check_discovered_sector(self, visible_table: list, invisible_table: list, selected_row: int, selected_column: str) -> bool:
        '''
        This method checks whether the selected cell has already been discovered or not.
        If it was already discovered, it returns True, and if not, it returns False.
        '''
        if visible_table[selected_row][selected_column] == invisible_table[selected_row][selected_column]:
            print("\nThis sector has already been discovered! Try another.\n")
            return True
        else:
            return False


