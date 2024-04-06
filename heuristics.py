def calculate_cost(self, initial_position):
    board_costs = [[0 for _ in range(len(self.board[0]))] for _ in range(len(self.board))]
    for i in range(len(self.board)):
        for j in range(len(self.board[0])):
            board_costs[i][j] = abs(i - initial_position[0]) + abs(j - initial_position[1])
    return board_costs


def euclidean_distance(initial_position, final_position):
    x1, y1 = initial_position
    x2, y2 = final_position
    return (x2 - x1)**2 + (y2 - y1)**2


def calculate_euclidean_cost(initial_position, final_position):
    return euclidean_distance(initial_position, final_position)


def manhattan_distance(initial_position, final_position):
    x1, y1 = initial_position
    x2, y2 = final_position
    return abs(x2 - x1) + abs(y2 - y1)


def calculate_manhattan_cost(initial_position, final_position):
    return manhattan_distance(initial_position, final_position)

# def min_distance_from_zeros(maze:Maze) -> int:
#     sum=0
#     for i in range(maze.lines):
#         for j in range(maze.columns):
#             if maze.maze[i, j] == None: #celulas ainda nao visitadas
#                     sum += abs(maze.target_line - i) + abs(maze.target_col - j)
#     return sum
