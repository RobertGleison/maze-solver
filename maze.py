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
    def __init__(self, rows, columns, block_positions, last_move = ' ', initial_position = (0,0), last_position = (0,0), last_length_move = 0, counter = 0) -> None:
        self.rows = rows
        self.columns = columns
        self.board = self.make_board(block_positions)
        self.path_record = []
        self.last_move = last_move # up, down, left or right
        self.current_move = 'foo'
        self.current_position = initial_position
        self.last_position = last_position
        self.last_length_move = last_length_move
        self.counter = counter


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

    def calculate_last_move_length(self):
        if self.current_move != self.last_move:
            self.last_length_move = self.counter


    def children(self) -> list:
        list_of_moves = [self.up, self.down, self.left, self.right]
        children = []
        for move in list_of_moves:
            child = move()
            if child:
                child.path_record.append(child)
                children.append(child)
        return children
    
    def up(self):
        new_position = (self.current_position[0] + 1, self.current_position[1])
        if self.is_valid_move(new_position):
            self.current_position = new_position
            # Check for consecutive move distance
            if self.previous_move_distance != 1:
                return Maze(self.rows, self.columns, block_positions=[], 
                        last_move='U', initial_position=self.current_position, 
                        last_position=self.last_position, 
                        last_length_move=abs(self.current_position[0] - self.last_position[0]), counter=self.counter + 1)
        else:
            return None

    def down(self):
        new_position = (self.current_position[0] + 1, self.current_position[1])
        # Check if move is valid (within boundaries and not blocked)
        if self.is_valid_move(new_position):
            self.current_position = new_position
            # Check for consecutive move distance
            if self.previous_move_distance != 1:
                return Maze(self.rows, self.columns, block_positions=[], 
                        last_move='D', initial_position=self.current_position, 
                        last_position=self.last_position, 
                        last_length_move=abs(self.current_position[0] - self.last_position[0]), counter=self.counter + 1)
        else:
            return None

    def left(self):
        new_position = (self.current_position[0], self.current_position[1] - 1)
        # Check if move is valid (within boundaries and not blocked)
        if self.is_valid_move(new_position):
            self.current_position = new_position
            # Check for consecutive move distance
            if self.previous_move_distance != 1:
                return Maze(self.rows, self.columns, block_positions=[], 
                        last_move='L', initial_position=self.current_position, 
                        last_position=self.last_position, 
                        last_length_move=abs(self.current_position[1] - self.last_position[1]), counter=self.counter + 1)
        else:
            return None

    def right(self):
        new_position = (self.current_position[0], self.current_position[1] + 1)
        # Check if move is valid (within boundaries and not blocked)
        if self.is_valid_move(new_position):
            self.current_position = new_position
            # Check for consecutive move distance
            if self.previous_move_distance != 1:
                return Maze(self.rows, self.columns, block_positions=[], 
                        last_move='R', initial_position=self.current_position, 
                        last_position=self.last_position, 
                        last_length_move=abs(self.current_position[1] - self.last_position[1]), counter=self.counter + 1)
        else:
            return None

    def is_valid_move(self, new_position):
        """Checks if a move is valid within the maze boundaries and not blocked."""
        rows, cols = self.rows, self.columns
        # Check if within boundaries
        if 0 <= new_position[0] < rows and 0 <= new_position[1] < cols:
            # Check if not blocked position
            return self.board[new_position[0]][new_position[1]] != BLOCK
        else:
            return False

    # def print_sequence(node:Maze):
        # if node is None:
        #     print('There is no solution')
        #     return
        # print("Steps:", len(node.move_history) - 1)
        # # prints the sequence of states
        # for maze in node.move_history:
        #     print(maze)
        #     print()