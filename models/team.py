class Team:
    def __init__(self, name, race, total_wins, total_losses, total_fouls, id=None):
        self.name = name
        self.race = race
        self.total_wins = total_wins
        self.total_losses = total_losses
        self.total_fouls = total_fouls
        self.id = id