from maze import Maze
from collections import deque
import time
import os


def depth_first_search(initial_maze:Maze):
    stack = deque([initial_maze]) 
    visited = set()
    while stack:
        maze = stack.pop() 
        if maze.is_complete():   
            return maze.print_final_maze()
        visited.add(maze)
        children = maze.children()
        for child in children:
            time.sleep(0.3)
            os.system('clear')
            print("Modo selecionado: DFS\n \n", child) 
            if child not in visited:
                stack.append(child)  
    return maze.print_all_moves(maze)


def breadth_first_search(initial_maze):
    queue = deque([initial_maze])  
    while queue:
        maze = queue.popleft()   
        if maze.is_complete():   
            return maze.print_final_maze()
        for child in maze.children():   
            queue.append(child)    
            time.sleep(0.3)
            os.system('clear')
            print("Modo selecionado: BFS\n\n", child)    
    return None



   