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


def manhattan_distance(initial_position, final_position):
    x1, y1 = initial_position
    x2, y2 = final_position
    return abs(x2 - x1) + abs(y2 - y1)

