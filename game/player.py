import pygame
from game.board import BOARD_X, BOARD_Y, CELL_SIZE


class Player:
    def __init__(self, row=0, col=0):
        self.row = row
        self.col = col

        # Resources
        self.crew = 50
        self.treasure = 3
        self.divine_favor = 0
        self.has_sacrifice = True

    def draw(self, screen):
        """Draw the player's ship."""

        center_x = BOARD_X + self.col * CELL_SIZE + CELL_SIZE // 2
        center_y = BOARD_Y + self.row * CELL_SIZE + CELL_SIZE // 2

        pygame.draw.circle(
            screen,
            (40, 80, 255),
            (center_x, center_y),
            CELL_SIZE // 3,
        )
    def move(self, d_row, d_col):
        """Move the player one space if it's inside the board."""

        new_row = self.row + d_row
        new_col = self.col + d_col

        # Stay inside the 8x8 board
        if 0 <= new_row < 8:
            self.row = new_row

        if 0 <= new_col < 8:
            self.col = new_col
    

