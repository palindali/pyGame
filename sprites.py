import pygame
from settings import *
################################################################################
                                    #BACKGROUND#
################################################################################
class Background(pygame.sprite.Sprite):
    def __init__(self,image_file):
        super().__init__()
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.location = (0,0)

################################################################################
                                    #PLAYER#
################################################################################
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.posx = 0
        self.posy = 0
        self.width = 32
        self.height = 32
        self.health = 0
        self.velocity = 4
        self.direction = 0
        self.images = [pygame.image.load("Assets/playerStill.png")]
        self.imageDir = 0
        self.imageCur = 0
    def Draw(self,screen):
        screen.blit(self.images[self.imageDir],(self.posx,self.posy),
            (self.imageCur*self.width,0,self.width,self.height))
        self.updateAnime()

    def updateAnime(self):
        self.imageCur = (self.imageCur + 1)%16

    def updatePos(self):
        if(self.direction == UP):
            x = 0 #TEMPORARY
        elif(self.direction == DOWN):
            x = 0 #TEMPORARY
        elif(self.direction == LEFT):
            self.posx -= self.velocity
        elif(self.direction == RIGHT):
            self.posx += self.velocity
        else:
            self.posy+=0 #GRAVITY
