import pygame

#Intialize the pygame
pygame.init()
#create the screen
screen = pygame.display.set_mode((800,600))

#Title and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

#Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #RGB - RED,GREEN,BLUE
    screen.fill((100,0,0))
    pygame.display.update()
