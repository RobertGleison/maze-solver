class Maze:
    def __init__(self, rows, columns, block_positions) -> None:
        self.rows = rows
        self.columns = columns
        self.board = self.make_board(block_positions)
        self.current_row = 0
        self.curren_column = 0
        self.path = 0
        self.last_move = 0
        self.current_move = 0


    def print_board(self):
        horizontal_border = '+---' * self.columns + '+'
        for row in reversed(self.board):
            print(horizontal_border)
            print('| ' + ' | '.join(row) + ' |')
        print(horizontal_border)
    
    
    def add_final_position(self, board):
        board[self.rows - 1][self.columns - 1] = 'F'
    
    def add_initial_position(self, board):
        board[0][0] = 'S'
    
    def add_block_positions(self, board, block_positions):
        for pos in block_positions:
            board[pos[0]][pos[1]] = '□' 

    def make_board(self, block_positions):
        board = [[' ' for _ in range(self.columns)] for _ in range(self.rows)]
        self.add_initial_position(board)
        self.add_final_position(board)
        self.add_block_positions(board, block_positions)
        return board
 
 
    def add_path(self, path):
        for i in range(1, len(path)):
            current_pos = path[i]
            previous_pos = path[i - 1]
            if not (0 <= current_pos[0] < self.rows and 0 <= current_pos[1] < self.columns):
                raise IndexError("Caminho fora do tabuleiro")
            symbol = '|' if current_pos[1] == previous_pos[1] else '―'
            self.board[current_pos[0]][current_pos[1]] = symbol