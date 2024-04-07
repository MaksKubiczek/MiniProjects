import numpy as np
import random
from cell import Cell

def generate_random_terrain(rows, cols, tree_probability):
    grid = np.empty((rows, cols), dtype=object)
    for row in range(rows):
        for col in range(cols):
            tree_state = random.choices([0, 1], weights=[1 - tree_probability, tree_probability])[0]
            grid[row, col] = Cell(col, row, tree_state, random.randint(0, 100))
    return grid

def start_fire(terrain):
    valid_start = False
    while not valid_start:
        random_row = random.randint(0, len(terrain) - 1)
        random_col = random.randint(0, len(terrain[0]) - 1)
        cell = terrain[random_row, random_col]
        if cell.state == 1:
            cell.state = 2
            valid_start = True

def spread_fire(terrain):
    for row in range(len(terrain)):
        for col in range(len(terrain[0])):
            cell = terrain[row, col]
            if cell.state == 2:
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if 0 <= row + i < len(terrain) and 0 <= col + j < len(terrain[0]):
                            neighbor = terrain[row + i, col + j]
                            if neighbor.state == 1:
                                probability = random.randint(0, 100)
                                if probability < 70 - neighbor.humidity:
                                    neighbor.state = 2
