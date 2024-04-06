import numpy as np

FINAL = 'F'
INITIAL = 'S'
BLOCK = '□'
CURRENT_POS = '○'
UP = '↑'
RIGHT = '→'
DOWN = '↓'
LEFT = '←'

class Maze:
    def __init__(self, rows, columns, block_positions) -> None:
        self.rows = rows
        self.columns = columns
        self.board = self.make_board(block_positions)
        self.path_record = []
        self.last_position = (None,None)
        self.last_move = ''
        self.last_length_move = 0
        self.current_position = (0,0)


    def __str__(self):
        horizontal_border = '+---' * self.columns + '+'
        output = ""
        for row in reversed(self.board):  # Assuming maze is the correct attribute to print
            output += horizontal_border + '\n'
            output += '| ' + ' | '.join(row) + ' |\n'
        output += horizontal_border + '\n'
        return output
    
    
    def add_final_position(self, board):
        board[self.rows - 1][self.columns - 1] = FINAL
    

    def add_initial_position(self, board):
        board[0][0] = INITIAL
    

    def add_block_positions(self, board, block_positions):
        for pos in block_positions:
            board[pos[0]][pos[1]] = BLOCK


    def make_board(self, block_positions):
        board = np.full((self.rows, self.columns), ' ', dtype='object')
        self.add_initial_position(board)
        self.add_final_position(board)
        self.add_block_positions(board, block_positions)
        return board


    def children(self) -> list:
        list_of_moves = [self.up, self.down, self.left, self.right]
        children = []
        for move in list_of_moves:
            child = move()
            if child:
                child.path_record.append(child)
                children.append(child)
        return children
    
