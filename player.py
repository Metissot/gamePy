# -*- coding: utf-8 -*-

import pygame

class PJ(pygame.sprite.Sprite):
    def __init__(self, position):
        self.sheet = pygame.image.load('PJ.png')
        self.sheet.set_clip(pygame.Rect(0, 140, 60, 60))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.left_states = {0: (20, 580, 20, 60), 1: (80, 580, 20, 60), 2: (147, 580, 20, 60), 3: (212, 580, 20, 60), 4: (276, 580, 20, 60), 5: (338, 580, 20, 60), 6: (405, 580, 20, 60), 7: (471, 580, 20, 60), 8: (535, 580, 20, 60)}
        self.right_states = {0: (19, 705, 25, 60), 1: (83, 705, 25, 60), 2: (147, 705, 25, 60), 3: (209, 705, 25, 60), 4: (272, 705, 25, 60), 5: (334, 705, 25, 60), 6: (400, 705, 25, 60), 7: (465, 705, 25, 60), 8: (530, 705, 25, 60)}
        self.up_states = {0: (0, 45, 25, 45), 1: (25, 45, 25, 45), 2: (50, 45, 25, 45)}
        self.down_states = {0: (0, 0, 25, 45), 1: (25, 0, 25,45 ), 2: (50, 0, 25, 45)}

    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def update(self, direction):
        if direction == 'left':
            self.clip(self.left_states)
            self.rect.x -= 0
        if direction == 'right':
            self.clip(self.right_states)
            self.rect.x += 0
        if direction == 'up':
            self.clip(self.up_states)
            self.rect.y -= 5
        if direction == 'down':
            self.clip(self.down_states)
            self.rect.y += 5

        if direction == 'stand_left':
            self.clip(self.left_states[0])
        if direction == 'stand_right':
            self.clip(self.right_states[0])
        if direction == 'stand_up':
            self.clip(self.up_states[0])
        if direction == 'stand_down':
            self.clip(self.down_states[0])

        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                self.update('left')
            if event.key == pygame.K_RIGHT:
                self.update('right')
            if event.key == pygame.K_UP:
                self.update('up')
            if event.key == pygame.K_DOWN:
                self.update('down')

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                self.update('stand_left')
            if event.key == pygame.K_RIGHT:
                self.update('stand_right')
            if event.key == pygame.K_UP:
                self.update('stand_up')
            if event.key == pygame.K_DOWN:
                self.update('stand_down')
