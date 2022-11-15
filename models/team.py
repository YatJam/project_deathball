class Team:
    def __init__(self, name, race, total_wins, total_loses, total_fouls, id=None):
        self.name = name
        self.race = race
        self.total_wins = total_wins
        self.total_loses = total_loses
        self.total_fouls = total_fouls
        self.id = id