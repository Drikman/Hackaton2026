import pygame
from utils import CELL_SIZE, GRID_SIZE
from tiles.colors import BLACK, GREY,GREEN

class PlayerView:
    """Cette classe est responsable de l'affichage du joueur dans le monde de jeu."""
    def draw(self, screen):
        image_path = "assets/characters/basic/char_shielded_static_down.png"
        personnage_img = pygame.image.load(image_path).convert_alpha()
        personnage_img = pygame.transform.scale(personnage_img, (CELL_SIZE, CELL_SIZE))
        # DESSIN DU JOUEUR (Toujours au centre de l'écran)
        screen_center = (
            ((GRID_SIZE // 2) * CELL_SIZE + CELL_SIZE // 2 )-CELL_SIZE//2,
            ((GRID_SIZE // 2) * CELL_SIZE + CELL_SIZE // 2)-CELL_SIZE//2
        )
        screen.blit(personnage_img,screen_center)
    
    def draw_endurance_bar(self, screen, current, max_amount, x, y, length, height):
        ratio = current / max_amount
        # Draw the background (grey) bar
        pygame.draw.rect(screen, GREY, (x, y, length, height))
        # Draw the foreground (green) bar based on the current health
        pygame.draw.rect(screen, GREEN, (x, y, length * ratio, height))
        # Draw a black border around the health bar for clarity
        pygame.draw.rect(screen, BLACK, (x, y, length, height), 2)
    
    def Score(self, screen, current,x,y,length,height):
        font = pygame.font.SysFont(None, 30)  # Police de taille 30
        text = font.render(f"Score : {current}", True, BLACK)
        screen.blit(text, (500, 10))  # Position en haut à droite