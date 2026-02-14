from entities.entity import Entity
from tiles.tile import Tile
from utils import Position
from eventmanager import EventManager,QuitEvent

class ExitTile(Tile):
    """Cette classe représente une tile de trésor dans le monde de jeu."""
    def __init__(self, position: Position,ev : EventManager):
        super().__init__(position)
        self.ev = ev

    def on(self, entity: Entity):

        self.ev.post(QuitEvent())
        return "trésor"