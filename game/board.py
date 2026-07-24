import pygame

GRID_SIZE = 8
CELL_SIZE = 80

BOARD_WIDTH = GRID_SIZE * CELL_SIZE
BOARD_HEIGHT = GRID_SIZE * CELL_SIZE

BOARD_X = 80
BOARD_Y = 80


def draw_board(screen):
    """Draw the 8x8 game board."""

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):

            rect = pygame.Rect(
                BOARD_X + col * CELL_SIZE,
                BOARD_Y + row * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE,
            )

            pygame.draw.rect(screen, (70, 150, 220), rect)
            pygame.draw.rect(screen, (255, 255, 255), rect, 2)