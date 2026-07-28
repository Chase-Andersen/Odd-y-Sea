class TurnManager:
    def __init__(self, players):
        self.players = players
        self.current_player = 0

    @property
    def active_player(self):
        return self.players[self.current_player]

    def next_turn(self):
        self.current_player = (self.current_player + 1) % len(self.players)