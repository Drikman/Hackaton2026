from entities.entity import Entity
from tiles.tile import Tile
from utils import Position


class DesertTile(Tile):
    """Cette classe représente une tile de désert dans le monde de jeu."""
    def __init__(self, position: Position):
        super().__init__(position)

    def on(self, entity: Entity):
        return None
