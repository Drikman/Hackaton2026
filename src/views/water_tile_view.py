import pygame
from views.tile_view import TileView
from tiles.colors import BLUE
from utils import CELL_SIZE, GRID_SIZE
class WaterTileView(TileView):
    """Cette classe est responsable de l'affichage des tiles d'eau dans le monde de jeu."""
    def draw(self, screen: pygame.Surface, rect: tuple[int, int, int, int]):
        image_path = "assets/tiles/water/tile_0_0.png"
        personnage_img = pygame.image.load(image_path).convert_alpha()
        personnage_img = pygame.transform.scale(personnage_img, (CELL_SIZE, CELL_SIZE))
        # DESSIN DU JOUEUR (Toujours au centre de l'écran)
        screen_center = (
            ((GRID_SIZE // 2) * CELL_SIZE + CELL_SIZE // 2 )-CELL_SIZE//2,
            ((GRID_SIZE // 2) * CELL_SIZE + CELL_SIZE // 2)-CELL_SIZE//2
        )
        screen.blit(personnage_img,rect)
