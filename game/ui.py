import pygame

from game.constants import WHITE, BLACK


class HUD:
    def __init__(self):
        pygame.font.init()

        self.title_font = pygame.font.SysFont("arial", 24, bold=True)
        self.text_font = pygame.font.SysFont("arial", 20)

    def draw(self, screen, player):

        # Background panel
        pygame.draw.rect(screen, (235, 235, 235), (0, 0, 800, 70))
        pygame.draw.line(screen, BLACK, (0, 70), (800, 70), 2)

        labels = [
            f"Crew: {player.crew}",
            f"Treasure: {player.treasure}",
            f"Favor: {player.divine_favor}",
            f"Sacrifice: {'Yes' if player.has_sacrifice else 'No'}",
        ]

        x = 20

        for label in labels:
            text = self.text_font.render(label, True, BLACK)
            screen.blit(text, (x, 24))
            x += 180