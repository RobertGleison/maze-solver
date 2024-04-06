import os
import random
from maze import Maze
from collections import deque
import time

# def main():
#     # game_mode = select_game_mode()
#     maze = create_game()
#     print(maze)

# def create_game():
#     rows = 6
#     columns = 6
#     return Maze(rows, columns, block_positions = [(4,4),(2,2),(3,2)])


# if __name__ == "__main__":
#     main()

# def breadth_first_search(initial_maze):
#     queue = deque([initial_maze])
#     visited = set()  # Set to store visited positions or states
    
#     while queue:
#         maze = queue.popleft()   # Primeiro elemento da fila (por ordem de chegada - FIFO)
        
#         # Check if the maze is complete
#         if maze.is_complete():
#             print("is complete")
#             return maze.print_all_moves(maze)
        
#         # Mark the current maze state as visited
#         visited.add(tuple(maze.current_position))
        
#         # Get children and enqueue unvisited children
#         for child in maze.children():
#             if tuple(child.current_position) not in visited:
#                 queue.append(child)
#                 print(child)
#                 time.sleep(1)

#                 visited.add(tuple(child.current_position))
                
#     return None

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

# def breadth_first_search(initial_maze):
#     queue = deque([initial_maze])  
#     while queue:
#         maze = queue.popleft()   #primeiro elemento da fila (por ordem de chegada - FIFO)
#         if maze.is_complete():   # ver se ja esta completo
#             return maze.print_all_moves()
        
#         for child in maze.children():   # ver as children deste nó
#             print(child)
#             queue.append(child)        
#             # time.sleep(0.5)
#     return None

maze = Maze(4,4, block_positions=[(0,3)])
inicio = time.time()
depth_first_search(maze)
print('\n ' + str(time.time() - inicio) + '\n')
print('------------------------')

# def select_game_mode():
#     game_modes = {1: "BFS", 2: "DFS", 3: "Greedy", 4: "A*", 5: "Iterative DFS" }
#     while True:
#         os.system('clear')
#         print("Escolha um modo de resolução:")
#         for mode, description in game_modes.items():
#             print(f"{mode}- {description}")
#         game_mode = input("\nDigite o número correspondente ao modo desejado: ")
#         if game_mode.isdigit(): 
#             game_mode = int(game_mode)
#             if game_mode in game_modes: break
#         print("Por favor, digite um número correspondente a um modo de resolução válido.\n")
#     print(f"Modo selecionado: {game_modes[game_mode]}\n\n") 
