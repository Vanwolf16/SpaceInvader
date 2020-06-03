import pygame
import random

# Intialize the pygame
pygame.init()
# create the screen
screen = pygame.display.set_mode((800, 600))

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('ufo.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 20
enemyY_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Title and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# Game Loop
running = True
while running:
    # RGB - RED,GREEN,BLUE
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # if key is pressed check
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -5.3
        if event.key == pygame.K_RIGHT:
            playerX_change = 5.3
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0
    # Player added and movement
    playerX += playerX_change
    # Boundary for the player
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    #Enemy Movement
    enemyX += enemyX_change

    if playerX <= 0:
        enemyX = 20
        enemyY += enemyY_change
    elif playerX >= 736:
        enemyX = -20
        enemyY += enemyY_change

    player(playerX, playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()
