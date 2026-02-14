from actions.action import Action
from actions.nothing import Nothing
from entities.entity import Entity
from utils import Position, Move


class Player(Entity):
    """
    Cette classe représente le joueur dans le monde de jeu. 
    Le joueur peut se déplacer dans les quatre directions cardinales, mais ne peut pas traverser les tiles d'eau.
    """
    def __init__(self, position: Position):
        super().__init__(position)
        self.color = (0, 0, 0)

    def move(self, direction: Move):
        self.pos.move(direction)

    def effect_on(self, effect: Action):
        if type(effect) != type(Nothing):
            pass
        return None
