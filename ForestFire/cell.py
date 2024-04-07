import pygame

class Cell:
    def __init__(self, x, y, state, humidity):
        self.x = x
        self.y = y
        self.state = state
        self.humidity = humidity

        self.colors = {
            1: (0, 128, 0),  # GREEN
            0: (155, 103, 60),  # BROWN
            2: (255, 0, 0),  # RED
            3: (0, 0, 0)  # BLACK
        }

    def draw(self, window):
        color = self.colors[self.state]
        pygame.draw.rect(window, color, (self.x * 5, self.y * 5, 5, 5))
