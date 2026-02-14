import pygame
from utils import CELL_SIZE, GRID_SIZE
from tiles.colors import BLACK, GREY,GREEN

class PlayerView:
    """Cette classe est responsable de l'affichage du joueur dans le monde de jeu."""
    def draw(self, screen):
        # DESSIN DU JOUEUR (Toujours au centre de l'écran)
        screen_center = (
            (GRID_SIZE // 2) * CELL_SIZE + CELL_SIZE // 2,
            (GRID_SIZE // 2) * CELL_SIZE + CELL_SIZE // 2
        )
        pygame.draw.circle(screen, BLACK, screen_center, CELL_SIZE // 3)
    
    def draw_endurance_bar(self, screen, current, max_amount, x, y, length, height):
        ratio = current / max_amount
        # Draw the background (grey) bar
        pygame.draw.rect(screen, GREY, (x, y, length, height))
        # Draw the foreground (green) bar based on the current health
        pygame.draw.rect(screen, GREEN, (x, y, length * ratio, height))
        # Draw a black border around the health bar for clarity
        pygame.draw.rect(screen, BLACK, (x, y, length, height), 2)