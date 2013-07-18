
"""
Takes a Level for input
Initializes the 3 Screens (Board, playerHand, taskMenu)
"""

from View.GUI.window import window
from Level.level import level

class gameController:

    def __init__(self):
        """ Initializes the game gameController"""
        self.level = Level()
        self.clock = pygame.time.Clock()
        self.running = True
        self.gameView = GameView(self.level)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_q:
                        self.running = False
            window.draw(self.gameView.draw())



