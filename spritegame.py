# Pygame sprite Example
import pygame
import random
import os

WIDTH = 800
HEIGHT = 600
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# set up assets folders
# Windows: "C:\Users\chris\Documents\img"
# Mac: "/Users/chris/Documents/img"
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "pics")

class Player(pygame.sprite.Sprite):
    # sprite for the Player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "ss.png")).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.y_speed = 5

    def moveLeft(self):
        if self.rect.x < WIDTH:
            self.rect.x -= 5

    def moveRight(self):
        if self.rect.x > 0:
            self.rect.x += 8

    def moveUp(self):
        if self.rect.y < WIDTH:
            self.rect.y -= 5

    def moveDown(self):
        if self.rect.y > 0:
            self.rect.y += 8

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
background = pygame.image.load(os.path.join(img_folder,"background.jpg")).convert()
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    if pygame.key.get_pressed()[pygame.K_LEFT]:
        player.moveLeft()
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        player.moveRight()

    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(BLUE)
    screen.blit(background,(0,0))
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
