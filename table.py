from random import randint

class Table:

    '''
    This class handles all the information on the game table. Receives 
    a number of rows, columns, and beasts, given by user input.
    '''


    def __init__(self, rows: int, columns: int, beasts: int) -> None:
        self.rows = rows
        self.columns = columns
        self.beasts = beasts
        self.visible_table = self.create_visible_table()
        self.invisible_table = self.create_invisible_table()
    

    def create_rows(self) -> list:
        '''
        This method creates the rows of the game table.
        '''
        table = []
        for row in range(self.rows):
            table.append([])
        return table


    def create_visible_table(self) -> list:
        '''
        This method creates the table that the user 
        sees in the console and interacts with.
        '''
        table = self.create_rows()
        for row in table:
            for column in range(self.columns):
                row.append(" ")
        return table


    def create_invisible_table(self) -> list:
        '''
        This method creates the table that's "under" the 
        visible table and contains all the unrevealed information
        of the table.
        '''
        table = self.create_rows()
        for row in table:
            for column in range(self.columns):
                row.append(0)
        table = self.set_beasts(table)
        table = self.assign_values(table)
        return table


    def neighbor_beasts(self, cell_row: int, cell_column: int, table: list) -> int:
        '''
        This method counts the number of beasts around a cell. 
        It receives the board and the row and column of the cell as parameters.
        '''
        neighbor_beasts = 0
        # We iterate through each of the neighboring cells and add the number of neighboring beasts
        for row in range(max(0, cell_row - 1), min(self.rows - 1, cell_row + 1) + 1): # We check the cell above and the cell below, without leaving the board.
            for column in range(max(0, cell_column - 1), min(self.columns - 1, cell_column + 1) + 1): # We check the cell on the right and the cell on the left, without leaving the board.
                if row == cell_row and column == cell_column:
                    continue
                if table[row][column] == "N":
                    neighbor_beasts += 1
        return neighbor_beasts


    def set_beasts(self, table: list) -> list:
        '''
        This method set the beasts in the given game table.
        '''
        placed_beasts = 0
        while placed_beasts < self.beasts:
            beast_row = randint(0, (self.rows - 1))
            beast_column = randint(0, (self.rows - 1))
            if table[beast_row][beast_column] == "N": # It means we already put a beast in that cell
                continue
            else:
                table[beast_row][beast_column] = "N"
                placed_beasts += 1
        return table


    def assign_values(self, table: list) -> list:
        '''
        This method assigns the number of neighboring beasts to cells that don't have a beast.
        '''
        for row in range(self.rows):
            for column in range(self.columns):
                if table[row][column] == "N":
                    continue
                table[row][column] = self.neighbor_beasts(row, column, table)
        return table