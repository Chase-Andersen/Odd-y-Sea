import pygame
import sys

from game.board import draw_board
from game.player import Player

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
FPS = 60

# Create window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Odd-y-Sea")

clock = pygame.time.Clock()
captain = Player(row=0, col=0)

# Main game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_w:
                captain.move(-1, 0)

            elif event.key == pygame.K_s:
                captain.move(1, 0)

            elif event.key == pygame.K_a:
                captain.move(0, -1)

            elif event.key == pygame.K_d:
                captain.move(0, 1)
        

    # Background color (Ocean Blue)
    screen.fill((15, 70, 130))
    draw_board(screen)
    captain.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()
sys.exit()