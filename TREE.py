import random
import pygame 
from city_scroller_solution import Scroller 

pygame.init() 

RED=(255,0,0)
GREEN=(0,255,0)

SCREEN_WIDTH= 700
SCREEN_HEIGHT= 500
screen= pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
done=False 
clock = pygame.time.Clock() 


class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite. __init__(self)
        self.width = width
        self.height = height
        self.color = color 
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        pygame.display.update() 
    def move(self, x, y):
        self.shipRect.center[0] += x
        self.shipRect.center[1] += y

xy = pygame.mouse.get_pos()

sprite= Player(RED, 30, 20) 


all_sprites = pygame.sprite.Group()
all_sprites.add(sprite)

FRONT_SCROLLER_COLOR = (170,20,230)
MIDDLE_SCROLLER_COLOR = (148,0,211)
BACK_SCROLLER_COLOR = (216,191,216)
BACKGROUND_COLOR = (122,103,238)
front_scroller = Scroller(SCREEN_WIDTH, 0, SCREEN_HEIGHT - 400, FRONT_SCROLLER_COLOR, -3)
middle_scroller = Scroller(SCREEN_WIDTH, 50, SCREEN_HEIGHT - 200, MIDDLE_SCROLLER_COLOR, -2)
back_scroller = Scroller(SCREEN_WIDTH, 100, SCREEN_HEIGHT - 10, BACK_SCROLLER_COLOR, -1)



while not done:     
    for event in pygame.event.get():         
        if event.type == pygame.QUIT:             
            done = True


    if event.key == K_RIGHT:
        Player.x += 5
    if event.key == K_LEFT:
        Player.move(-5,0)
    if event.key == K_UP: 
        Player.move(0,5)
    if event.key == K_DOWN:
        Player.move(0,-5)



    screen.fill(BACKGROUND_COLOR)
    back_scroller.draw_buildings()
    back_scroller.move_buildings()
    middle_scroller.draw_buildings()
    middle_scroller.move_buildings()
    front_scroller.draw_buildings()
    front_scroller.move_buildings()
    all_sprites.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
exit()