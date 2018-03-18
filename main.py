#The first game made by Ali, Hussein, and Yousof
import pygame
from settings import *
from sprites import *

################################################################################
                                    #INIT#
################################################################################
def main():
    #Initilize pygame
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Super Box Crate")

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()


    #Main game loop

    while True:
        game = Game()
        while game.gameOver == False:
            if game.gameExit == True:
                break
            game.Run(screen)
            clock.tick(60)
        if game.gameExit == True:
            break


################################################################################
                                    #GAME#
################################################################################
class Game():
    def __init__(self):
        self.score = 0
        self.gameOver = False
        self.gameExit = False
        self.gravity = 0

        self.player = Player()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)
    def Run(self,screen):
        self.gameInput()
        self.player.updatePos()
        if(self.gameOver == True):
            self.gameOverScreen(screen)
        else:
            self.gameDraw(screen)

    def gameInput(self):
        for input in pygame.event.get():
            if input.type == pygame.QUIT:
                self.gameExit = True
                print("AlLAHUAKBSR")

        keys = pygame.key.get_pressed()
        if   keys[pygame.K_w]:
            self.player.direction = UP
        elif keys[pygame.K_s]:
            self.player.direction = DOWN
        elif keys[pygame.K_a]:
            self.player.direction = LEFT
        elif keys[pygame.K_d]:
            self.player.direction = RIGHT
        elif keys[pygame.K_x]:
            self.gameOver = True
        else:
            self.player.direction = 0

    def Update():
        self.player.updatePos()
    def gameOverScreen(self,screen):
        screen.fill(WHITE)
        font = pygame.font.SysFont("serif", 25)
        text = font.render("Game Over, click to restart", True, BLACK)
        x = (WIDTH // 2) - (text.get_width() // 2)
        y = (HEIGHT // 2) - (text.get_height() // 2)
        screen.blit(text, [x, y])
        print("OVERRRRRRRRRRRRR")

    def gameDraw(self, screen):
        # Creating background, background should be a part of level class
        background = Background("Assets/blue_background.png")
        screen.blit(background.image, background.location)
        #Eventually a new function to draw all sprites should be added
        self.player.Draw(screen)

        pygame.display.update()
################################################################################
                                    #LEVEL#
################################################################################
class Level():
    def __init__():
        pass
    def draw():
        pass

main()
