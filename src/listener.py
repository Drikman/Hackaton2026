from abc import ABC, abstractmethod


class Listener(ABC):
    """
    Classe de base pour les écouteurs d'événements dans le jeu. 
    Les classes qui héritent de Listener doivent implémenter la méthode notify pour recevoir les événements du jeu.
    """
    @abstractmethod
    def notify(self, event):
        raise NotImplementedError('')