import pygame
import sys

from game.constants import WINDOW_WIDTH, WINDOW_HEIGHT
from game.game import Game

pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Odd-y-Sea")

game = Game(screen)
game.run()

pygame.quit()
sys.exit()