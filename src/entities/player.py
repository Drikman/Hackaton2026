from actions.action import Action
from actions.nothing import Nothing
from entities.entity import Entity
from utils import Position, Move
from threading import Thread
import time

class Player(Entity):
    """
    Cette classe représente le joueur dans le monde de jeu. 
    Le joueur peut se déplacer dans les quatre directions cardinales, mais ne peut pas traverser les tiles d'eau.
    """
    
    def __init__(self, position: Position):
        super().__init__(position)
        self.color = (0, 0, 0)
        self.endurance = 5
        rest_thread = Thread(target=self.rest)
        self.score = 0
        self.temp_passe=0

        rest_thread.start()

    def move(self, direction: Move):
        print(self.pos)
        if self.endurance == 0:
            print("\033[31mVous êtes épuisé ! Reposez-vous au moins une seconde avant de continuer.\033[0m")
        else:
            self.pos.move(direction)
            self.endurance -= 1
        
    def rest(self):
        print("APPELE")
        while(True):
            time.sleep(1)
            self.temp_passe+= 1
            if(self.endurance < 5):
                self.endurance += 1

    def effect_on(self, effect: Action):
        if type(effect) != type(Nothing):
            pass
        return None

