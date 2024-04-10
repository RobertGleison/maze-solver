import pygame
import sys
import time

CELL_SIZE = 100
BOARD_WIDTH = 100
BOARD_HEIGHT = 100
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (124, 252, 0)
GRAY = (200, 200, 200)
BLUE = (0,0,255)

class Interface:
    def __init__(self, maze, rows, columns):
        self.rows = columns # pygame interface is inverted
        self.columns = rows # pygame interface is inverted
        self.initial_position = (maze.rows-1,0)
        self.final_position = (0,maze.columns-1)
        self.positions = maze.position_record  
        self.block_positions = maze.block_positions
        self.is_solved = maze.is_complete()
        self.screen_height = CELL_SIZE * rows
        self.screen_width = CELL_SIZE * columns


def create_interface(maze, rows, columns):
    pygame.init()
    interface = Interface(maze, rows, columns)
    screen = pygame.display.set_mode((interface.screen_height,interface.screen_width))
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
        if pos != interface.final_position and board[pos[0]][pos[1]] == 2:
            # Leave a trail behind the player block
            board[old_tuple[0]][old_tuple[1]] = 1
        board[pos[0]][pos[1]] = 2
        draw_board(board, screen)
        draw_blocks(screen, interface.block_positions)
        positions_visited.append(pos)
        draw_trajectory(screen, positions_visited)
        draw_initial_position(screen, interface.initial_position)
        draw_final_position(screen, interface.final_position)
        # rotated_screen = pygame.transform.flip(screen,True, False)
        # rotated_screen = pygame.transform.rotate(screen,-90)
        # rotated_screen = pygame.transform.flip(screen,True, True)
        # rotated_screen = pygame.transform.flip(screen,True, False)
        # rotated_screen = pygame.transform.rotate(screen,30)
        # screen.blit(rotated_screen, (0, 0))
        pygame.display.flip()
        time.sleep(0.5)

        old_tuple = pos
    if interface.is_solved:
        positions_visited += [interface.final_position]
        draw_trajectory(screen, positions_visited) 
        draw_initial_position(screen, interface.initial_position)
        draw_final_position(screen, interface.final_position)
        pygame.display.flip()
    time.sleep(4)
    pygame.quit()
    sys.exit()

def draw_blocks(screen, block_positions):
    for pos in block_positions:
        x, y = pos
        rect = pygame.Rect(x * CELL_SIZE + CELL_SIZE // 4, y * CELL_SIZE + CELL_SIZE // 4, CELL_SIZE // 2, CELL_SIZE // 2)
        draw_block(screen, rect)

def draw_block(surface, rect):
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
    pygame.draw.rect(screen, BLUE, rect)

def draw_final_position(screen, pos):
    x, y = pos
    rect = pygame.Rect(x * CELL_SIZE + CELL_SIZE // 4, y * CELL_SIZE + CELL_SIZE // 4, CELL_SIZE // 2, CELL_SIZE // 2)
    pygame.draw.rect(screen, GREEN, rect)

def draw_trajectory(screen, positions):
    if len(positions) > 1:
        # Define the thickness of the line
        thickness = 21
        
        # Draw the line segments
        for i in range(len(positions)-1):
            start_point = (positions[i][0] * CELL_SIZE + CELL_SIZE // 2, positions[i][1] * CELL_SIZE + CELL_SIZE // 2)
            end_point = (positions[i + 1][0] * CELL_SIZE + CELL_SIZE // 2, positions[i + 1][1] * CELL_SIZE + CELL_SIZE // 2)
            pygame.draw.line(screen, BLACK, start_point, end_point, thickness)
            
            # Draw rectangles at the corners to simulate thickness
            rect_start = (start_point[0] - thickness // 2, start_point[1] - thickness // 2, thickness, thickness)
            rect_end = (end_point[0] - thickness // 2, end_point[1] - thickness // 2, thickness, thickness)
            pygame.draw.rect(screen, BLACK, rect_start)
            pygame.draw.rect(screen, BLACK, rect_end)

          

