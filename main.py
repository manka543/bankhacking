import pygame
import random


class Game:
    def __init__(self):
        # First
        pygame.init()
        # order doesn't care
        self.running = True
        # Last
        self.game_loop()

    def game_loop(self):
        while self.running:
            pass


game = Game()
