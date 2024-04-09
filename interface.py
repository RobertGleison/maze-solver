import pygame
import sys
import time

CELL_SIZE = 100
BOARD_WIDTH = 10
BOARD_HEIGHT = 10
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (124, 252, 0)
GRAY = (200, 200, 200)

class Interface:
    def __init__(self, maze):
        self.initial_position = maze.initial_position
        self.final_position = maze.final_position
        self.rows = maze.rows
        self.columns = maze.columns
        self.positions = maze.position_record + [(self.rows-1, self.columns-1)]
        self.block_positions = maze.block_positions
        global SCREEN_HEIGHT, SCREEN_WIDTH
        SCREEN_HEIGHT = CELL_SIZE * self.rows
        SCREEN_WIDTH = CELL_SIZE * self.columns

def create_interface(maze):
    pygame.init()
    interface = Interface(maze)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Unequal Length Maze")

    board = [[0] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]

    old_tuple = interface.initial_position
    positions_visited = [old_tuple]
    for pos in interface.positions:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Check for collision with obstacles
        if pos != interface.final_position and board[pos[1]][pos[0]] == 2:
            # Leave a trail behind the player block
            board[old_tuple[1]][old_tuple[0]] = 1
        board[pos[1]][pos[0]] = 2
        draw_board(board, screen)
        draw_blocks(screen, interface.block_positions)
        positions_visited.append(pos)
        draw_trajectory(screen, positions_visited)
        draw_initial_position(screen, interface.initial_position)
        draw_final_position(screen, interface.final_position)

        pygame.display.flip()
        time.sleep(0.5)

        old_tuple = pos
    time.sleep(3)
    pygame.quit()
    sys.exit()

def draw_blocks(screen, block_positions):
    for pos in block_positions:
        x, y = pos
        rect = pygame.Rect(x * CELL_SIZE + CELL_SIZE // 4, y * CELL_SIZE + CELL_SIZE // 4, CELL_SIZE // 2, CELL_SIZE // 2)
        draw_rectangle_with_x(screen, rect)

def draw_rectangle_with_x(surface, rect):
    pygame.draw.rect(surface, RED, rect)
    pygame.draw.line(surface, WHITE, rect.topleft, rect.bottomright, 6)
    pygame.draw.line(surface, WHITE, rect.topright, rect.bottomleft, 6)

def draw_board(board, screen):
    for y in range(BOARD_HEIGHT):
        for x in range(BOARD_WIDTH):
            if board[y][x] == 0:
                center_x = x * CELL_SIZE + CELL_SIZE // 2
                center_y = y * CELL_SIZE + CELL_SIZE // 2
                pygame.draw.rect(screen, WHITE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
                

def draw_initial_position(screen, pos):
    x, y = pos
    rect = pygame.Rect(x * CELL_SIZE + CELL_SIZE // 4, y * CELL_SIZE + CELL_SIZE // 4, CELL_SIZE // 2, CELL_SIZE // 2)
    pygame.draw.rect(screen, GREEN, rect)

def draw_final_position(screen, pos):
    x, y = pos
    rect = pygame.Rect(x * CELL_SIZE + CELL_SIZE // 4, y * CELL_SIZE + CELL_SIZE // 4, CELL_SIZE // 2, CELL_SIZE // 2)
    pygame.draw.rect(screen, GREEN, rect)

def draw_trajectory(screen, positions):
    if len(positions) > 1:
        # Define the thickness of the line
        thickness = 21
        
        # Draw the line segments
        for i in range(len(positions) - 1):
            print(len(positions))
            start_point = (positions[i][0] * CELL_SIZE + CELL_SIZE // 2, positions[i][1] * CELL_SIZE + CELL_SIZE // 2)
            end_point = (positions[i + 1][0] * CELL_SIZE + CELL_SIZE // 2, positions[i + 1][1] * CELL_SIZE + CELL_SIZE // 2)
            pygame.draw.line(screen, BLACK, start_point, end_point, thickness)
            
            # Draw rectangles at the corners to simulate thickness
            rect_start = (start_point[0] - thickness // 2, start_point[1] - thickness // 2, thickness, thickness)
            rect_end = (end_point[0] - thickness // 2, end_point[1] - thickness // 2, thickness, thickness)
            pygame.draw.rect(screen, BLACK, rect_start)
            pygame.draw.rect(screen, BLACK, rect_end)

