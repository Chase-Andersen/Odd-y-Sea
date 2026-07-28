import pygame

from game.board import Board
from game.player import Player
from game.constants import OCEAN, FPS
from game.ui import HUD


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.hud = HUD()
        self.clock = pygame.time.Clock()

        # Game objects
        self.board = Board()
        self.captain = Player(row=0, col=0)

        self.running = True

    def handle_events(self):
        """Handle keyboard and window events."""

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_w:
                    self.captain.move(-1, 0)

                elif event.key == pygame.K_s:
                    self.captain.move(1, 0)

                elif event.key == pygame.K_a:
                    self.captain.move(0, -1)

                elif event.key == pygame.K_d:
                    self.captain.move(0, 1)

    def update(self):
        """Update the game state."""
        pass

    def draw(self):
        """Draw everything."""

        self.screen.fill(OCEAN)

        self.board.draw(self.screen)
        self.captain.draw(self.screen)

        self.hud.draw(self.screen, self.captain)

        pygame.display.flip()

    def run(self):
        """Main game loop."""

        while self.running:
            self.handle_events()
            self.update()
            self.draw()

            self.clock.tick(FPS)