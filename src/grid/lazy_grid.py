import random
from tiles.colors import *
from tiles.desert_tile import DesertTile
from tiles.tile import Tile
from tiles.water_tile import WaterTile
from tiles.lava_Tile import LavaTile
from tiles.Tresure_tile import TresureTile
from utils import Position
from tiles.exit_tile import ExitTile
from eventmanager import EventManager


class LazyGrid:
    """Génération procédurale infinie et déterministe."""
    def __init__(self, seed: int,evmanager : EventManager):
        self.seed = seed
        self._cache = {}
        self.evmanager = evmanager

    def get_tile(self, x: int, y: int) -> Tile:
        # 1. Vérifier le cache (modifications joueur)
        if (x, y) in self._cache:
            return self._cache[(x, y)]
        
        # 2. Sécurité pour le point de départ
        if x == 1000 and y == 1000:
            return DesertTile(Position(x, y)) 
        if x == 1005 and y == 1005:
            ev = self.evmanager
            return ExitTile(Position(x,y),ev)
        # 3. Génération basée sur la seed et les coordonnées
        rng = random.Random(f"{self.seed}_{x}_{y}")
        rand = rng.random()
        
        if rand > 0.4:   return  DesertTile(Position(x, y))  # Majorité de tuiles désertiques
        elif 0.4 >=rand > 0.2:             return WaterTile(Position(x, y))   # Quelques tuiles d'eau
        elif 0.2 >= rand > 0.07 :            return  LavaTile(Position(x,y))
        else:                                return TresureTile(Position(x,y))

    def set_tile(self, x: int, y: int, tile: Tile):
        self._cache[(x, y)] = tile