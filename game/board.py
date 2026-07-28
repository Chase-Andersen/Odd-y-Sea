import pygame

from game.constants import (
    BOARD_TILE,
    GRID_SIZE,
    CELL_SIZE,
    BOARD_X,
    BOARD_Y,
    WHITE,
)


class Board:
    def __init__(self):
        pass

    def draw(self, screen):
        """Draw the 8x8 game board."""

        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):

                rect = pygame.Rect(
                    BOARD_X + col * CELL_SIZE,
                    BOARD_Y + row * CELL_SIZE,
                    CELL_SIZE,
                    CELL_SIZE,
                )

                pygame.draw.rect(screen, BOARD_TILE, rect)
                pygame.draw.rect(screen, WHITE, rect, 2)