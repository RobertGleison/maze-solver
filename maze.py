import copy
import numpy as np
from copy import deepcopy

FINAL = 'F'
INITIAL = 'S'
BLOCK = '□'
CURRENT_POS = '○'
UP_ARROW = '↑'
RIGHT_ARROW = '→'
DOWN_ARROW = '↓'
LEFT_ARROW = '←'

class Maze:
    def __init__(self, rows, columns, block_positions, last_move = ' ', initial_position = (0,0), last_position = (0,0), last_length_move = 0, length_move = 1) -> None:
        self.rows = rows
        self.columns = columns
        self.final_position = (rows-1,columns-1)
        self.initial_position = (0,0)
        self.board = self.make_board(block_positions)
        self.path_record = []
        self.last_move = last_move # up, down, left or right
        self.current_move = ' '
        self.current_position = initial_position
        self.last_position = last_position
        self.last_length_move = last_length_move
        self.length_move = length_move


    def __str__(self) -> str: 
        """Print board of actual maze"""
        horizontal_border = '+---' * self.columns + '+'
        output = ""
        for row in reversed(self.board):  # Assuming maze is the correct attribute to print
            output += horizontal_border + '\n'
            output += '| ' + ' | '.join(row) + ' |\n'
        output += horizontal_border + '\n'
        return output
    
    
    def add_final_position(self, board) -> None:
        """Add the final position to the maze board"""
        board[self.rows - 1][self.columns - 1] = FINAL
    

    def add_initial_position(self, board) -> None:
        """Add the initial position to the maze board"""
        board[0][0] = INITIAL
    

    def add_block_positions(self, board, block_positions) -> None:
        """Add the blocking positions to the maze board"""
        for pos in block_positions:
            board[pos[0]][pos[1]] = BLOCK


    def make_board(self, block_positions) -> np.ndarray:
        """Create the board for the maze"""
        board = np.full((self.rows, self.columns), ' ', dtype='object')
        self.add_initial_position(board)
        self.add_final_position(board)
        self.add_block_positions(board, block_positions)
        return board


    def children(self) -> list:
        """Get the possible moves of a certain state"""
        list_of_moves = [self.up, self.down, self.left, self.right]
        children = []
        for move in list_of_moves:
            child = move()
            if child:
                child.path_record += [deepcopy(child)]
                children.append(child)
        return children
    

    def update_length_moves(self):
        """Update values of move length"""
        if self.last_move == self.current_move: self.length_move+=1
        else:
            self.last_move = self.current_move
            self.last_length_move = self.length_move
            self.length_move = 1
    

    def move(func) -> np.ndarray | None:
        """Decorator for movements"""
        def decorator(self):
            node = deepcopy(self)
            result = func(node)  
            return node if result else None
        return decorator
    

    @move
    def up(self) -> bool:
        """Up movement and validations"""
        row, col = (self.current_position[0] + 1, self.current_position[1])
        if (row > self.rows-1) or (self.board[row,col] == BLOCK) or (self.board[row, col] == FINAL and np.count_nonzero(self.board == ' ') > 0) or (self.current_move != UP_ARROW and self.length_move == self.last_length_move): 
            return False

        self.current_position = (row,col)
        self.board[row][col] = UP_ARROW
        self.current_move = UP_ARROW
        self.update_length_moves()
        return True
        

    @move
    def down(self) -> bool:
        """Down movement and validations"""
        row, col = (self.current_position[0] - 1, self.current_position[1])
        if (row < 0) or (self.board[row,col] == BLOCK) or (self.board[row, col] == FINAL and np.count_nonzero(self.board == ' ') > 0) or (self.current_move != DOWN_ARROW and self.length_move == self.last_length_move): 
             return False
        self.current_position = (row,col)
        self.board[row][col] = DOWN_ARROW
        self.current_move = DOWN_ARROW
        self.update_length_moves()
        return True


    @move
    def left(self) -> bool:
        """Left movement and validations"""
        row, col = (self.current_position[0], self.current_position[1] - 1)
        if (col < 0) or (self.board[row,col] == BLOCK) or (self.board[row, col] == FINAL and np.count_nonzero(self.board == ' ') > 0) or (self.current_move != LEFT_ARROW and self.length_move == self.last_length_move): 
            return False
        self.current_position = (row,col)
        self.board[row][col] = LEFT_ARROW
        self.current_move = LEFT_ARROW
        self.update_length_moves()
        return True


    @move
    def right(self) -> bool:
        """Right movement and validations"""
        row, col = (self.current_position[0], self.current_position[1] + 1)
        if (col > self.columns-1) or (self.board[row,col] == BLOCK) or (self.board[row, col] == FINAL and np.count_nonzero(self.board == ' ') > 0) or (self.current_move != RIGHT_ARROW and self.length_move == self.last_length_move): 
            return False
        self.current_position = (row,col)
        self.board[row][col] = RIGHT_ARROW
        self.current_move = RIGHT_ARROW
        self.update_length_moves()
        return True


    def is_complete(self) -> bool:
        """Check if maze is solved"""
        return self.current_position == self.final_position and np.count_nonzero(self.board == ' ') == 0

    def print_all_moves(maze) -> None:
        """Print the the moves until maze is solved or no more move is allowed"""
        print("Steps:", len(maze.path_record) - 1)
        # prints the sequence of states
        for board in maze.path_record:
            print(board)
            print()