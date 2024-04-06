import os
from maze import Maze

def main():
    game_mode = select_game_mode()
    maze = create_game()
    print(maze)

def create_game():
    rows = 6
    columns = 6
    return Maze(rows, columns, block_positions = [(4,4),(2,2),(3,2)])


def select_game_mode():
    game_modes = {1: "BFS", 2: "DFS", 3: "Greedy", 4: "A*", 5: "Iterative DFS" }
    while True:
        os.system('clear')
        print("Escolha um modo de resolução:")
        for mode, description in game_modes.items():
            print(f"{mode}- {description}")
        game_mode = input("\nDigite o número correspondente ao modo desejado: ")
        if game_mode.isdigit(): 
            game_mode = int(game_mode)
            if game_mode in game_modes: break
        print("Por favor, digite um número correspondente a um modo de resolução válido.\n")
    print(f"Modo selecionado: {game_modes[game_mode]}\n\n") 


if __name__ == "__main__":
    main()
