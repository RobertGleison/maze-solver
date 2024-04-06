import numpy as np

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
        self.board = self.make_board(block_positions)
        self.path_record = []
        self.last_move = last_move # up, down, left or right
        self.current_move = ' '
        self.current_position = initial_position
        self.last_position = last_position
        self.last_length_move = last_length_move
        self.length_move = length_move


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

    def compare_last_move_length(self):
        if self.current_move != self.last_move:
            self.last_length_move = self.length_move
            self.length_move = 0


    def children(self) -> list:
        list_of_moves = [self.up, self.down, self.left, self.right]
        children = []
        for move in list_of_moves:
            child = move()
            if child:
                child.path_record.append(child)
                children.append(child)
        return children
    
    def update_length_moves(self):
        if self.last_move == self.current_move: self.length_move+=1
        # else:
        #     self.last_move = self.current_move
        #     self.last_length_move = self.length_move
        #     self.length_move = 1
        
    def up(self):
        row, col = (self.current_position[0] + 1, self.current_position[1])
        if (row > self.rows-1) or (self.board[row,col] == BLOCK) or (self.board[row, col] == FINAL and np.count_nonzero(self.maze == ' ') > 0) or (self.length_move == self.last_length_move): 
            return None

        self.current_position = (row,col)
        self.board[row][col] = UP_ARROW
        self.current_move = 'up'
        self.update_length_moves
        

    def down(self):
        row, col = (self.current_position[0] - 1, self.current_position[1])
        if (row < 0) or (self.board[row,col] == BLOCK) or (self.board[row, col] == FINAL and np.count_nonzero(self.maze == ' ') > 0) or (self.length_move == self.last_length_move): 
             return None
        self.current_position = (row,col)
        self.board[row][col] = DOWN_ARROW
        self.current_move = 'down'
        self.update_length_moves


    def left(self):
        row, col = (self.current_position[0], self.current_position[1] - 1)
        if (col < 0) or (self.board[row,col] == BLOCK) or (self.board[row, col] == FINAL and np.count_nonzero(self.maze == ' ') > 0) or (self.length_move == self.last_length_move): 
            return None
        self.current_position = (row,col)
        self.board[row][col] = LEFT_ARROW
        self.current_move = 'left'
        self.update_length_moves


    def right(self):
        row, col = (self.current_position[0], self.current_position[1] + 1)
        if (col > self.columns-1) or (self.board[row,col] == BLOCK) or (self.board[row, col] == FINAL and np.count_nonzero(self.maze == ' ') > 0) or (self.length_move == self.last_length_move): 
                return None
        self.current_position = (row,col)
        self.board[row][col] = RIGHT_ARROW
        self.current_move = 'right'
        self.update_length_moves


    # def print_sequence(node:Maze):
        # if node is None:
        #     print('There is no solution')
        #     return
        # print("Steps:", len(node.move_history) - 1)
        # # prints the sequence of states
        # for maze in node.move_history:
        #     print(maze)
        #     print()