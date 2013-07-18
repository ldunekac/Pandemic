import pygame
from pygame.locals import *

class BoardView:

    def __init__(self):
        """Initializes the Board View"""
        self.boardImage = pygame.image.load('View/GUI/Pictures/world_map.jpg')
        self.boardSurface = surface = pygame.Surface((500,500))

    def draw(self):
        """ Draws the board"""
        transformedBoardImage = pygame.transform.scale(self.boardImage,(500,500))
        return transformedBoardImage
