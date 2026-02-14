import pygame
from views.tile_view import TileView
from tiles.colors import PURPLE

class TresorTileView(TileView):
    """Cette classe est responsable de l'affichage des tiles de trésor dans le monde de jeu."""
    def draw(self, screen: pygame.Surface, rect: tuple[int, int, int, int]):
        pygame.draw.rect(screen, PURPLE, rect)
