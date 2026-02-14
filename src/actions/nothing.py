from dataclasses import dataclass

from actions.action import Action


@dataclass
class Nothing(Action):
    pass
