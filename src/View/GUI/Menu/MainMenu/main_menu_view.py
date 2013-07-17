import pygame
from pygame.locals import *


class MainMenuView:

    def __init__(self, mainMenuControler):
        pygame.init()
        imagePath = '../../Pictures/MainMenuPictures/pandemic_menu_picture.jpg'
        self.screenSize = (500,500)
        self.menuPicture = pygame.image.load(imagePath)
        menuPictureSize = self.menuPicture.get_size()
        self.screen = pygame.display.set_mode(menuPictureSize)
        self.menuPicture = self.menuPicture.convert()
        
    def display(self):
        """ Displays the Start Menu """
        self.screen.blit(self.menuPicture,(0,0))
        pygame.display.flip()


view = MainMenuView(4)
view.display()


for i in range(1,50000):
    view.display()
