import pygame
from terrain import generate_random_terrain, start_fire, spread_fire
from actions import put_out_fire, remove_trees_right_click
from utils import draw_start_button

# PyGame Initialization
pygame.init()

# Window Settings
width, height = 800, 800
cell_size = 5  # Size of a single cell
rows, cols = width // cell_size, height // cell_size

# Colors
BROWN = (155, 103, 60)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)


def main():
    # Initializing the window
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Forest Fire Simulation')

    running = True
    tree_probability = 0.7
    radius = 5  # Extinguishing radius
    radius2 = 2
    simulation_started = False
    terrain = generate_random_terrain(rows, cols, tree_probability)
    start_fire(terrain)  # Initializing fire

    delay_time = 200  # Delay time in milliseconds (change value as needed)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                put_out_fire(terrain, pygame.mouse.get_pos(), radius)  # Extinguish fire with left click

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  # Handling right click
                remove_trees_right_click(terrain, pygame.mouse.get_pos(), radius2)  # Remove trees with right click

            if not simulation_started and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    simulation_started = True  # Start simulation upon pressing '1' key

        if simulation_started:
            spread_fire(terrain)
            pygame.time.delay(delay_time)  # Delay between simulation iterations

        window.fill(BLACK)  # Fill background

        draw_start_button(window)  # Draw start button

        for row in range(rows):
            for col in range(cols):
                terrain[row, col].draw(window)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
