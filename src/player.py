import pygame

from settings import *

class Player:
    def __init__(self):
        self.PLAYER_WIDTH = 15
        self.PLAYER_HEIGHT = 70
        
        self.y = HEIGHT // 2 - self.PLAYER_HEIGHT // 2
        self.x = 50

        self.direction = None
        self.moving = False

        self.SPEED = 10

    def move(self) -> None:
        keys = pygame.key.get_pressed()

        self.moving = False

        if keys[pygame.K_w]:
            self.y -= self.SPEED
            self.direction = "up"
            self.moving = True
        
        if keys[pygame.K_s]:
            self.y += self.SPEED
            self.direction = "down"
            self.moving = True

        self.is_outside()

    def is_outside(self) -> None:
        if self.y < 0:
            self.y = 0
        
        elif self.y > HEIGHT - 70:
           self.y = HEIGHT - 70

    def get_width(self) -> int:
        return self.PLAYER_WIDTH

    def get_height(self) -> int:
        return self.PLAYER_HEIGHT

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def get_direction(self) -> str:
        return self.direction

    def is_moving(self) -> bool:
        return self.moving