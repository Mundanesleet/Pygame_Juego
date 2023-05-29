import pygame, sys

ventana = pygame.display.set_mode((800, 600))

#Variables
game_over = False

while not game_over:
    for event in pygame.even.get():

        if event.type == pygame.QUIT:
            sys.exit()
