from settings import *
import pygame

class Game:
    def __init__(self):
        
        # general
        self.surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.display_surface = pygame.display.get_surface()
    
    def draw_grid(self):
        for col in range(1, COLUMNS):
            x = col * CELL_SIZE
            pygame.draw.line(self.surface, LINE_COLOR, (x, 0), (x, self.surface.get_height()), 1) #(surface, color, start_pos, end_pos, width)
        for row in range(1, ROWS):
            y = row * CELL_SIZE
            pygame.draw.line(self)
       
    def run(self):
        self.draw_grid()
        self.display_surface.blit(self.surface, (PADDING, PADDING))
        