import random

from settings import *
from player import Player

class Ball:
    def __init__(self, player: object):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2

        self.BALL_HEIGHT = 10

        self.y_speed = random.choice([-2, -1, 1, 2])

        self.player = player

        self.direction = random.choice(["left", "right"])

        self.can_collide = True

        self.SPEED = 5

    def move(self):
        if self.direction == "left":
            self.x -= self.SPEED
        else:
            self.x += self.SPEED

        self.y += self.y_speed

    def check_player_collision(self):
        player_rightside_x = self.player.get_x() + self.player.get_width()
        player_bottom_y = self.player.get_y() + self.player.get_height()

        # Checking if ball has passed players x and if can collide
        if self.can_collide and self.x <= player_rightside_x:
            # Checking if balls Y is in Players Y
            if self.y >= self.player.get_y() and self.y <= player_bottom_y:

                self.x = player_rightside_x
                self.direction = "right"
                self.can_collide = False
                self.paddle_reflect("player")

        # Reset it once the ball has moved away
        if self.x > player_rightside_x + self.BALL_HEIGHT:
            self.can_collide = True

    def check_opponent_collision(self):
        opponent_bottom_y = self.opponent.get_y() + self.opponent.get_height()

        # Checking if ball has passed opponents x and if can collide
        if self.can_collide and self.x >= self.opponent.get_x():
            # Checking if balls Y is in Opponents Y
            if self.y >= self.opponent.get_y() and self.y <= opponent_bottom_y:

                self.x = self.opponent.get_x()
                self.direction = "left"
                self.can_collide = False
                self.paddle_reflect("opponent")

        # Reset it once the ball has moved away
        if self.x + self.BALL_HEIGHT < self.opponent.get_x():
            self.can_collide = True

    def paddle_reflect(self, hitter):
        # Player Hit
        if hitter == "player":
            if self.player.is_moving():
                if self.player.get_direction() == "up":
                    self.y_speed = -self.SPEED

                elif self.player.get_direction() == "down":
                    self.y_speed = self.SPEED
            else:
                self.y_speed = random.choice([-2, -1, 1, 2])

        # Opponent Hit
        if hitter == "opponent":
            if self.opponent.is_moving():
                if self.opponent.get_direction() == "up":
                    self.y_speed = -self.SPEED

                elif self.opponent.get_direction() == "down":
                    self.y_speed = self.SPEED
            else:
                self.y_speed = random.choice([-2, -1, 1, 2])

    def surface_reflect(self):
        if self.y < 0 or self.y > (HEIGHT - self.BALL_HEIGHT):
            self.y_speed = -self.y_speed
    
    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def get_height(self) -> int:
        return self.BALL_HEIGHT