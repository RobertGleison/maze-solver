from maze import Maze
import maze as m
from collections import deque
import time
import os
from heapq import heappop, heappush

def print_statistics(best_maze, maze, start_time, max_size_stack, n_path_percurred, mode):
    if maze.there_is_no_solution():
        os.system('clear')
        print(f"Modo selecionado: {mode}\n\n") 
        m.print_final_maze(best_maze)      
        print("Não foi encontrado solução!")    
    if maze.is_complete():   
        os.system('clear')
        print(f"Modo selecionado: {mode}\n\n") 
        m.print_final_maze(best_maze)
        print("Solução encontrada!")   
    print("\nMovimentos feitos:", len(best_maze.position_record))
    print(f"Tempo execução: {time.time() - start_time:.4f} segundos")
    print(f"Nós máximos na memória: {max_size_stack}")
    print(f"Nós filhos explorados: {n_path_percurred}")
    

def depth_first_search(initial_maze: Maze):
    start_time = time.time()
    n_path_percurred = 0
    stack = deque([initial_maze]) 
    best_maze = initial_maze
    max_size_stack = 0
    visited = set()
    while stack:
        if len(stack) > max_size_stack: max_size_stack = len(stack)
        maze = stack.pop() 
        if len(maze.position_record) > len(best_maze.position_record): best_maze = maze
        visited.add(maze)
        for child in maze.children():
            n_path_percurred+=1
            # os.system("clear")
            # print("Modo selecionado: DFS\n \n", child)
            if child not in visited:
                stack.append(child)  
        print_statistics(best_maze, maze, start_time, max_size_stack, n_path_percurred, 'DFS')
    return best_maze



def iterative_deeppening_search(initial_maze):
    start_time = time.time()
    n_path_percurred = 0
    depth = 0
    solution_found = False
    best_maze = initial_maze

    while not solution_found:
        best_maze, solution_found = depth_limited_search(initial_maze, depth)
        depth += 1
        # Assuming `children` method increments `n_path_percurred`
        n_path_percurred += sum(1 for _ in best_maze.children())  

        if solution_found:
            os.system('clear')
            print("Modo selecionado: IDS\n\n")
            # Assuming `print_final_maze` is a method to visualize the maze
            m.print_final_maze(best_maze)
            print("Solução encontrada!")
        print_statistics(best_maze, maze, start_time, max_size_stack, n_path_percurred, 'IFS')
    return best_maze


def depth_limited_search(maze, limit):
    n_path_percurred = 0
    start_time = time.time()
    stack = deque([[maze]])  # Stack to store paths instead of states
    best_maze = maze
    while stack:
        maze = stack.pop()
        if len(maze.position_record) > len(best_maze.position_record):
            best_maze = maze
        if len(path) - 1 < limit:  # Check if current depth is less than limit
            for child in maze.children():
                if child.is_complete():
                    return child, True
                stack.append(path + [child])
    return best_maze, False

    
    stack = deque([initial_maze]) 
    best_maze = initial_maze
    max_size_stack = 0
    visited = set()
    while stack:
        if len(stack) > max_size_stack: max_size_stack = len(stack)
        maze = stack.pop() 
        if len(maze.position_record) > len(best_maze.position_record): best_maze = maze
        visited.add(maze)
        for child in maze.children():
            n_path_percurred+=1
            # os.system("clear")
            # print("Modo selecionado: DFS\n \n", child)
            if child not in visited:
                stack.append(child)  
        print_statistics(best_maze, maze, start_time, max_size_stack, n_path_percurred, 'DFS')


# def greedy_search(initial_maze, heuristic):
#     start_time = time.time()
#     n_path_percurred = 0
#     priority_queue = []
#     heappush(priority_queue, (heuristic(initial_maze), 0, initial_maze))
#     visited = set()
#     best_maze = initial_maze
#     id_counter = 1
#     max_size_queue = 0
#     nodes_visited = 0

#     while priority_queue:
#         if len(priority_queue) > max_size_queue: max_size_queue = len(priority_queue)
#         _, _, maze = heappop(priority_queue)
#         nodes_visited += 1  # Incrementa o número de nós visitados
#         if len(maze.path_record) > len(best_maze.path_record): best_maze = maze
#         if maze.is_complete():
#             break  # Sai do loop quando encontrar a solução
#         visited.add(maze)
#         for child in maze.children():
#             n_path_percurred += 1
#             if child not in visited:
#                 heappush(priority_queue, (heuristic(child), id_counter, child))
#                 id_counter += 1

#     print("Modo selecionado: Greedy Search\n\n")

#     if best_maze.is_complete():
#         print("Solução encontrada!")
#         m.print_final_maze(best_maze)
#     else:
#         print("Não foi encontrado solução!")

#     print(f"Tempo de execução: {time.time() - start_time:.4f} segundos")
#     print(f"Nós máximos na memória: {max_size_queue}")
#     print(f"Caminhos diferentes explorados: {n_path_percurred}")
#     print(f"Nós visitados: {nodes_visited}")

#     return best_maze





# """def greedy_search(initial_maze, heuristic):
#     start_time = time.time()
#     solution_found = False
#     priority_queue = []
#     heappush(priority_queue, (heuristic(initial_maze), 0, initial_maze))  # Inclui um contador como segundo elemento
#     visited = set()
#     id_counter = 1  # Inicia o contador para garantir unicidade

#     while priority_queue:
#         _, _, maze = heappop(priority_queue)
#         if maze.is_complete():
#             return maze
#         visited.add(maze)
#         for child in maze.children():
#             if child not in visited:
#                 heappush(priority_queue, (heuristic(child), id_counter, child))
#                 id_counter += 1  # Incrementa o contador a cada inserção
#         if solution_found

#     return None"""




# """def greedy_search(initial_maze:Maze, heuristic):
#     '''
#     Implementa busca gulosa para encontrar um caminho em um labirinto.

#     :param initial_maze: Instância inicial do labirinto.
#     :param heuristic: Função heurística para orientar a busca.
#     :return: O labirinto com o caminho encontrado.
#     '''
 
#     # Inicializa a fila de prioridades com o labirinto inicial e sua heurística como prioridade.
#     priority_queue = [(heuristic(initial_maze), initial_maze)]
#     visited = set()  # Conjunto para armazenar os estados visitados

#     while priority_queue:
#         # Obtém o labirinto com a menor heurística.
#         _, maze = heappop(priority_queue)

#         # Verifica se o estado atual é o objetivo.
#         if maze.is_complete():
#             return maze

#         # Marca o estado atual como visitado.
#         visited.add(maze)

#         # Explora os filhos do estado atual.
#         for child in maze.children():
#             if child not in visited:
#                 # Adiciona cada filho na fila de prioridades com sua heurística.
#                 heappush(priority_queue, (heuristic(child), child))

#     # Retorna None se não encontrar solução.
#     return None

# # A função heurística será definida fora para permitir customização.
# # Aqui estamos assumindo que a Maze class possui métodos/atributos para acessar a posição atual e a posição do objetivo.
# """
   