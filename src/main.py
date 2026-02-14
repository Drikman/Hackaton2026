import eventmanager as evmgr
import game
import view
import controller
import math_utils

def run():
    print(f"Integration C++ OK : 10 + 20 = {math_utils.add(10, 20)}")
    ev_manager = evmgr.EventManager()
    gamemodel = game.GameEngine(ev_manager)
    keyboard = controller.Keyboard(ev_manager, gamemodel)
    graphics = view.GraphicalView(ev_manager, gamemodel)
    gamemodel.run()

if __name__ == '__main__':
    run()