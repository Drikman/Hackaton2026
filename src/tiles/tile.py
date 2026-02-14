from abc import ABC, abstractmethod
from utils import Position
from entities.entity import Entity

class Tile(ABC):
    """Classe de base pour les tiles dans le monde de jeu."""
    def __init__(self, position: Position):
        self.position = position

    @property
    def x(self):
        return self.position.x
    @property
    def y(self):
        return self.position.y

    @abstractmethod
    def on(self, entity: Entity):
        raise NotImplementedError(" ")
