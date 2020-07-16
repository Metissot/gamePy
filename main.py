# -*- coding: utf-8 -*-

import pygame, sys
import player
from pygame.locals import *
fondoBg = pygame.image.load('mapa.png')
pygame.init()

# Definimos algunas variables que usaremos en nuestro código
colorBg = pygame.Color('white')
ancho_ventana = 636
alto_ventana = 470
screen = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption("MiJueguito")
clock = pygame.time.Clock()

player = player.PJ((ancho_ventana/2, alto_ventana/2))
game_over = False

while game_over == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    player.handle_event(event)
    screen.fill(colorBg)
    screen.blit(fondoBg,(0,0))
    screen.blit(player.image, player.rect)

    pygame.display.flip()
    clock.tick(20)

pygame.quit ()
