from View.Console.controller import Controller
from View.Console.Level.Player.player_move_to_card_view import PlayerMoveToCardView

class PlayerMoveToCardController(Controller):
    """ Controller for a *** """
    
    def __init__(self, player, playerDeck):
        """ Initialize the *** Controller """
        Controller.__init__(self, PlayerMoveToCardView(player))
        self.player = player
        self.playerDeck = playerDeck
        self.actionCompleted = False
        
        self.addCommand(ord('0'), self.moveToCityZero)
        self.addCommand(ord('1'), self.moveToCityOne)
        self.addCommand(ord('2'), self.moveToCityTwo)
        self.addCommand(ord('3'), self.moveToCityThree)
        self.addCommand(ord('4'), self.moveToCityFour)
        self.addCommand(ord('5'), self.moveToCityFive)
        self.addCommand(ord('6'), self.moveToCitySix)
        self.addCommand(ord('7'), self.moveToCitySeven)
        self.addCommand(ord('8'), self.moveToCityEight)
        self.addCommand(ord('9'), self.moveToCityNine)
        
    def moveToCityZero(self):
        """ View the selected city """
        self.moveToCity(0)
        
    def moveToCityOne(self):
        """ View the selected city """
        self.moveToCity(1)
        
    def moveToCityTwo(self):
        """ View the selected city """
        self.moveToCity(2)
        
    def moveToCityThree(self):
        """ View the selected city """
        self.moveToCity(3)
        
    def moveToCityFour(self):
        """ View the selected city """
        self.moveToCity(4)
        
    def moveToCityFive(self):
        """ View the selected city """
        self.moveToCity(5)
        
    def moveToCitySix(self):
        """ View the selected city """
        self.moveToCity(6)
        
    def moveToCitySeven(self):
        """ View the selected city """
        self.moveToCity(7)
        
    def moveToCityEight(self):
        """ View the selected city """
        self.moveToCity(8)
        
    def moveToCityNine(self):
        """ View the selected city """
        self.moveToCity(9)
        
    def moveToCity(self, index):
        """ View the selected city """
        card = self.screen.getCard(index)
        if card is not None:
            self.player.moveTo(card.city)
            self.player.removeCardFromHand(card)
            self.playerDeck.discard(card)
            self.actionCompleted = True
            self.stopRunning()