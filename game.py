import os
from maze import Maze
import algorithms as a
import time
from interface import Interface
import interface


def main() -> None:
    game_mode = select_game_mode()
    rows = 6
    columns = 6
    block_positions = [(3,1),(3,2),(1,5)]
    maze = create_game(rows, columns, block_positions)
    maze = solve_maze(game_mode, maze)
    print(maze.position_record)
    print(maze.path_record)
    interface.create_interface(maze, rows, columns)


def create_game(rows, columns, block_positions) -> Maze:
    return Maze(rows, columns, block_positions)


def select_game_mode() -> int:
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


def solve_maze(game_mode: int, maze: Maze) -> Maze:
    response = None
    if game_mode == 1: maze = a.breadth_first_search(maze)
    if game_mode == 2: maze = a.depth_first_search(maze)
    # if game_mode == 3: maze = a.iterative(maze)
    # if game_mode == 4: maze = a.greedy(maze)
    # if game_mode == 5: maze = a.astar(maze)
    # if game_mode == 6: maze = a.w_astar(maze)
    return maze

if __name__ == "__main__":
    main()
