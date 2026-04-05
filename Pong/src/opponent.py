import pygame

from settings import *

class Opponent:
    def __init__(self, ball: object):
        self.OPPONENT_WIDTH = 15
        self.OPPONENT_HEIGHT = 70
        
        self.y = HEIGHT // 2 - self.OPPONENT_HEIGHT // 2
        self.x = WIDTH - (50 + self.OPPONENT_WIDTH)

        self.ball = ball

        self.direction = None
        self.moving = False

        self.SPEED = 10

    def move(self) -> None:
        self.moving = False

        previous_y = self.y
        self.y = self.ball.get_y() - self.OPPONENT_HEIGHT // 2
        self.moving = self.y != previous_y

        if self.y < previous_y:
            self.direction = "up"
        elif self.y > previous_y:
            self.direction = "down"

        self.is_outside()

    def is_outside(self) -> None:
        if self.y < 0:
            self.y = 0
        
        elif self.y > HEIGHT - 70:
           self.y = HEIGHT - 70

    def get_width(self) -> int:
        return self.OPPONENT_WIDTH

    def get_height(self) -> int:
        return self.OPPONENT_HEIGHT

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def get_direction(self) -> str:
        return self.direction

    def is_moving(self) -> bool:
        return self.moving