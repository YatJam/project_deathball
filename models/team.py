class Team:
    def __init__(self, name, race, total_wins, total_losses, total_fouls, id=None):
        self.name = name
        self.race = race
        self.total_wins = total_wins
        self.total_losses = total_losses
        self.total_fouls = total_fouls
        self.id = id

    def total_points(self):
        if self.total_wins == None or self.total_fouls == None:
            return 0

        total_points = self.total_wins - self.total_fouls
        return total_points

