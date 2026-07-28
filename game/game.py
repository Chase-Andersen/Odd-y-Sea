import pygame

from game.board import Board
from game.player import Player
from game.ui import HUD
from game.turn_manager import TurnManager
from game.constants import (
    BLUE,
    RED,
    GREEN,
    GOLD,
    OCEAN,
    FPS,
)


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()

        # UI
        self.hud = HUD()

        # Game objects
        self.board = Board()

        self.players = [
            Player("Odysseus", BLUE, 0, 0),
            Player("Helena", RED, 7, 7),
            Player("Leo", GREEN, 0, 7),
            Player("Nikos", GOLD, 7, 0),
        ]

        self.turn_manager = TurnManager(self.players)

        self.running = True

    def handle_events(self):
        """Handle keyboard and window events."""

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:

                player = self.turn_manager.active_player

                if event.key == pygame.K_w:
                    player.move(-1, 0)

                elif event.key == pygame.K_s:
                    player.move(1, 0)

                elif event.key == pygame.K_a:
                    player.move(0, -1)

                elif event.key == pygame.K_d:
                    player.move(0, 1)

                elif event.key == pygame.K_SPACE:
                    self.turn_manager.next_turn()

    def update(self):
        """Update the game state."""
        pass

    def draw(self):
        """Draw everything."""

        self.screen.fill(OCEAN)

        self.board.draw(self.screen)

        # Draw every player
        for player in self.players:
            player.draw(
                self.screen,
                active=(player == self.turn_manager.active_player)
            )

        # Draw the HUD
        self.hud.draw(
            self.screen,
            self.turn_manager.active_player
        )

        pygame.display.flip()

    def run(self):
        """Main game loop."""

        while self.running:
            self.handle_events()
            self.update()
            self.draw()

            self.clock.tick(FPS)