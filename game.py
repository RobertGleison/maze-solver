import os
from maze import Maze
import algorithms as a
import time
from interface import Interface
import interface
from heuristics import manhattan_distance, euclidean_distance


def main() -> None:
    """Play maze"""
    game_mode = select_game_mode()
    rows = 6
    columns = 6
    block_positions = [(3,2),(3,1),(1,5)]
    maze = create_game(rows, columns, block_positions)
    maze = solve_maze(game_mode, maze)
    interface.create_interface(maze, rows, columns)


def create_game(rows, columns, block_positions) -> Maze:
    """Create initial board maze"""
    return Maze(rows, columns, block_positions)


def select_game_mode() -> int:
    """Print interface to choose game mode"""
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
    """Chose the algorithm to play"""
    response = None
    if game_mode == 1: maze = a.breadth_first_search(maze)
    if game_mode == 2: maze = a.depth_first_search(maze)
    if game_mode == 3: maze = a.iterative_deeppening_search(maze)
    if game_mode == 4: maze = a.greedy_search(maze, euclidean_distance, weight=0)
    if game_mode == 5: maze = a.greedy_search(maze, euclidean_distance ,cost=True)
    if game_mode == 6: maze = a.greedy_search(maze, euclidean_distance ,cost=True, weight=2)
    return maze


if __name__ == "__main__":
    main()
