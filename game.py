import os
from maze import Maze
import algorithms as a
import time


def main():
    game_mode = select_game_mode()
    maze = create_game(game_mode)
    solve_maze(game_mode, maze)


def create_game(game_mode):
    return Maze(3, 3, block_positions = [])


def select_game_mode():
    game_modes = {1: "BFS", 2: "DFS", 3: "Iterative DFS", 4: "Greedy" , 5: "A*", 6: "Weighted A*"}
    while True:
        os.system('clear')
        print("Escolha um modo de resolução:")
        for mode, description in game_modes.items():
            print(f"{mode}- {description}")
        game_mode = int(input("\nDigite o número correspondente ao modo desejado: "))
        if game_mode in game_modes: 
            return game_mode            
        print("Por favor, digite um número correspondente a um modo de resolução válido.\n")


def solve_maze(game_mode: int, maze: Maze):
    if game_mode == 1: a.breadth_first_search(maze)
    if game_mode == 2: a.depth_first_search(maze)
    # if game_mode == 3: a.iterative(maze)
    # if game_mode == 4: a.greedy(maze)
    # if game_mode == 5: a.astar(maze)
    # if game_mode == 6: a.w_astar(maze)
    # else: return

if __name__ == "__main__":
    main()
