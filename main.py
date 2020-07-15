# -*- coding: utf-8 -*-

import pygame
import player

pygame.init()

# Definimos algunas variables que usaremos en nuestro código

ancho_ventana = 1024
alto_ventana = 720
screen = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption("ARGENTUM ONLINE")
clock = pygame.time.Clock()

player = player.PJ((ancho_ventana/2, alto_ventana/2))
game_over = False

while game_over == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    player.handle_event(event)
    screen.fill(pygame.Color('black'))
    screen.blit(player.image, player.rect)

    pygame.display.flip()
    clock.tick(20)

pygame.quit ()
