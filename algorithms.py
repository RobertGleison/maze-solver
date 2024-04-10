from maze import Maze
import maze as m
from collections import deque
import time
import os


def depth_first_search(initial_maze:Maze):
    start_time = time.time()
    n_path_percurred = 0
    stack = deque([initial_maze]) 
    best_maze = initial_maze
    max_size_stack = 0
    visited = set()
    while stack:
        if len(stack) > max_size_stack: max_size_stack = len(stack)
        maze = stack.pop() 
        if len(maze.path_record) > len(best_maze.path_record): best_maze = maze
        visited.add(maze)
        for child in maze.children():
            n_path_percurred+=1
            # time.sleep(0.3)
            # os.system('clear')
            print("Modo selecionado: DFS\n \n", child) 
            if child not in visited:
                stack.append(child)  
    if maze.there_is_no_solution():
        os.system('clear')
        print("Modo selecionado: BFS\n\n") 
        m.print_final_maze(best_maze)      
        print("Não foi encontrado solução!")    
    if maze.is_complete():   
        os.system('clear')
        print("Modo selecionado: BFS\n\n") 
        m.print_final_maze(best_maze)
        print("Solução encontrada!")   
    print(f"Tempo execução: {time.time() - start_time:.4f} segundos")
    print(f"Nós máximos na memória: {max_size_stack}")
    print(f"Caminhos diferentes explorados: {n_path_percurred}")
    return best_maze


def breadth_first_search(initial_maze):
    start_time = time.time()
    n_path_percurred = 0
    queue = deque([initial_maze])  
    best_maze = initial_maze
    max_size_queue = 0
    while queue:
        if len(queue) > max_size_queue: max_size_queue = len(queue)
        maze = queue.popleft()   
        if len(maze.path_record) > len(best_maze.path_record): best_maze = maze
        for child in maze.children():   
            n_path_percurred+=1
            os.system('clear')
            print("Modo selecionado: BFS\n\n", child) 
            queue.append(child)    
            time.sleep(0.3)
    if maze.there_is_no_solution():
        os.system('clear')
        print("Modo selecionado: BFS\n\n") 
        m.print_final_maze(best_maze)      
        print("Não foi encontrado solução!")    
    if maze.is_complete():   
        os.system('clear')
        print("Modo selecionado: BFS\n\n") 
        m.print_final_maze(best_maze)
        print("Solução encontrada!")   
    print(f"Tempo execução: {time.time() - start_time:.4f} segundos")
    print(f"Nós máximos na memória: {max_size_queue}")
    print(f"Caminhos diferentes explorados: {n_path_percurred}")
    return best_maze

    



   