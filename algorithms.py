from maze import Maze
from collections import deque
import time


def depth_first_search(initial_maze:Maze):
    stack = deque([initial_maze]) 
    visited = set()
    while stack:
        maze = stack.pop() #get the last element that came in
        if maze.is_complete():   
            return maze.print_all_moves(maze)
        visited.add(maze)
        children = maze.children()
        for child in children:
            print(child)
            # time.sleep(0.5)
            if child not in visited:
                stack.append(child)  
    return maze.print_all_moves(maze)


def breadth_first_search(initial_maze):
    queue = deque([initial_maze])  
    while queue:
        maze = queue.popleft()   #primeiro elemento da fila (por ordem de chegada - FIFO)
        if maze.is_complete():   # ver se ja esta completo
            return maze.print_all_moves()
        for child in maze.children():   # ver as children deste nó
            queue.append(child)        
            # time.sleep(0.5)
    return None


def chose_algorithm(game_mode: int, maze: Maze):
    maze = Maze(6,6, block_positions=[(5,0),(5,1),(5,2)])
    inicio = time.time()
    depth_first_search(maze)
    print('\n ' + str(time.time() - inicio) + '\n')
   