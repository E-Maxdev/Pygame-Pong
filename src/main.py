import pygame

from player import Player
from ball import Ball
from opponent import Opponent

from colors import *
from settings import *

class Main:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Pong")

        self.player = Player()
        self.ball = Ball(self.player)
        self.opponent = Opponent(self.ball)
        self.ball.opponent = self.opponent

        self.running = True

    def run(self):
        while self.running:
            self.player.move()
            self.opponent.move()
            
            self.ball.move()
            self.ball.check_player_collision()
            self.ball.check_opponent_collision()
            self.ball.surface_reflect()

            self.draw()
            self.events()

    def draw(self):
        self.screen.fill((BLACK))

        # Player
        player_rect = pygame.Rect(self.player.get_x(), self.player.get_y(),  self.player.get_width(), self.player.get_height())
        pygame.draw.rect(self.screen, WHITE, player_rect)

        # Opponent
        opponent_rect = pygame.Rect(self.opponent.get_x(), self.opponent.get_y(),  self.opponent.get_width(), self.opponent.get_height())
        pygame.draw.rect(self.screen, WHITE, opponent_rect)

        # Ball
        ball_rect = pygame.Rect(self.ball.get_x(), self.ball.get_y(), self.ball.get_height(), self.ball.get_height())
        pygame.draw.rect(self.screen, WHITE, ball_rect)

        pygame.display.flip()
        self.clock.tick(60)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        


main = Main()
main.run()
