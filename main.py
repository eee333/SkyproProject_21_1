from game_controller import GameController
from config import cell_mapping_1

with open("level.txt", "r", encoding="utf-8") as read_file:
    level_1 = read_file.read()


game = GameController(cell_mapping_1, level_1)

game.play()
