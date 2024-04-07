import pygame

def draw_start_button(window):
    start_button_width, start_button_height = 200, 50
    start_button_x, start_button_y = 50, 700

    pygame.draw.rect(window, (0, 128, 0), (start_button_x, start_button_y, start_button_width, start_button_height))
    font = pygame.font.Font(None, 36)
    text = font.render("Start Simulation", True, (155, 103, 60))
    text_rect = text.get_rect(center=(start_button_x + start_button_width / 2, start_button_y + start_button_height / 2))
    window.blit(text, text_rect)
