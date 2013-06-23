from View.Console.controller import Controller
from View.Console.player_draw_view import PlayerDrawView

class PlayerDrawController(Controller):
    """ Controller for the Player Drawing """
    
    def __init__(self, player, card):
        """ Initialize the Player Draw Controller """
        Controller.__init__(self, PlayerDrawView(card))
        self.player = player
        self.card = card
        self.addedToHand = False
        
        self.commands = {}
        self.addCommand(ENDL, self.stopRunning)
        
    def performGameCycle(self):
        """ Perform a Game Cycle Event """
        if not self.addedToHand:
            self.player.addCardToHand(self.card)
            self.addedToHand = True