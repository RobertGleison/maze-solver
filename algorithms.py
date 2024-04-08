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
    start_time = time.time()
    queue = deque([initial_maze])  
    while queue:
        maze = queue.popleft()   
        for child in maze.children():   
            queue.append(child)    
            # time.sleep(0.3)
            os.system('clear')
            print("Modo selecionado: BFS\n\n", child) 
    if maze.there_is_no_solution():
        os.system('clear')
        print("Modo selecionado: BFS\n\n") 
        maze.print_final_maze()      
        print("Não foi encontrado solução!")    
    if maze.is_complete():   
        os.system('clear')
        print("Modo selecionado: BFS\n\n") 
        maze.print_final_maze()
        print("Solução encontrada!")   
    print(f"Tempo execução: {time.time() - start_time:.4f} segundos")
    



   