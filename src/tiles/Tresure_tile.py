from entities.entity import Entity
from entities.player import Player
from tiles.tile import Tile
from utils import Position
from tiles.desert_tile import DesertTile


class TresureTile(Tile):
    """
    Cette classe représente une tile d'eau dans le monde de jeu.
    Les tiles d'eau sont des obstacles que le joueur ne peut pas traverser.
    """
    def __init__(self, position: Position):
        super().__init__(position)

    def on(self, entity: Entity):
        if isinstance(entity, Player):
            entity.score+=1
            

        return "trésor"
