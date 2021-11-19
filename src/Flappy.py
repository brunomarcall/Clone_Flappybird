import pygame
from pygame.locals import *

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 10
GRAVITY = 1

class Bird(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images = [pygame.image.load('assets/sprites/bluebird-upflap.png').convert_alpha(),
                      pygame.image.load('assets/sprites/bluebird-midflap.png').convert_alpha(),
                      pygame.image.load('assets/sprites/bluebird-downflap.png').convert_alpha()]

        self.speed = SPEED
        
        self.current_image = 0

        
        self.image = pygame.image.load('assets/sprites/bluebird-upflap.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = SCREEN_WIDTH / 2
        self.rect[1] = SCREEN_HEIGHT / 2
        

    def update(self):
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images [ self.current_image ]

        self.speed += GRAVITY

        # Update na altura
        self.rect[1] += self.speed
    
    def bump(self):
        self.speed = -SPEED



pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BACKGROUND = pygame.image.load('assets/sprites/background-day.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))

bird_group = pygame.sprite.Group()
bird = Bird()
bird_group.add(bird)

clock = pygame.time.Clock()



while True:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
           if event.key == K_SPACE or event.key == K_UP:
               bird.bump()     

    screen.blit(BACKGROUND, (0, 0))

    bird_group.update()

    bird_group.draw(screen)

    pygame.display.update()