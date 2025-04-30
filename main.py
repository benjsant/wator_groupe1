from entity.fish import Fish
from entity.shark import Shark
from planet import Planet
import random

""" SETTINGS """

number_of_fishes = 25
number_of_sharks = 15

rows = 10
columns = 10


""" GENERATE """

test_world = Planet(columns, rows)
test_world_display = test_world.init_grid()


for shark in range(number_of_sharks):
    shark = Shark(x=random.randrange(1, columns-1), y=random.randrange(1, rows-1))
    test_world.new_shark(shark=shark)
    test_world_display[shark.x][shark.y]=shark.img


for fish in range(number_of_fishes):
    fish = Fish(x=random.randrange(1, columns-1), y=random.randrange(1, rows-1))
    test_world.new_fish(fish=fish)
    test_world_display[fish.x][fish.y]=fish.emoji_fish

print(test_world_display)