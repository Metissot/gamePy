# -*- coding: utf-8 -*-

import pygame

class PJ(pygame.sprite.Sprite):
    def __init__(self, position):
        self.sheet = pygame.image.load('PJ.png')
        self.sheet.set_clip(pygame.Rect(14, 640, 30, 60))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.left_states = {0: (20, 576, 30, 50), 1: (81, 576, 30, 50), 2: (147, 576, 30, 60), 3: (211, 576, 30, 60), 4: (275, 576, 30, 60), 5: (337, 576, 30, 60), 6: (404, 576, 30, 60), 7: (467, 576, 30, 60), 8: (531, 576, 30, 60)}
        self.right_states = {0: (14, 705, 30, 60), 1: (83, 705, 30, 60), 2: (147, 705, 30, 60), 3: (209, 705, 30, 60), 4: (272, 705, 30, 60), 5: (334, 705, 30, 60), 6: (400, 705, 30, 60), 7: (465, 705, 30, 60), 8: (530, 705, 30, 60)}
        self.up_states = {0: (14, 512, 30, 60), 1: (78, 512, 30, 60), 2: (142, 512, 30, 60), 3: (206, 512, 30, 60), 4: (270, 512, 30, 60), 5: (334, 512, 30, 60), 6: (398, 512, 30, 60), 7: (463, 512, 30, 60), 8: (526, 512, 30, 60)}
        self.down_states = {0: (14, 640, 30, 60), 1: (78, 640, 30, 60), 2: (142, 640, 30, 60), 3: (206, 640, 30, 60), 4: (270, 640, 30, 60), 5: (334, 640, 30, 60), 6: (398, 640, 30, 60), 7: (463, 640, 30, 60), 8: (526, 640, 30, 60)}

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
            self.rect.x -= 5
        if direction == 'right':
            self.clip(self.right_states)
            self.rect.x += 5
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
