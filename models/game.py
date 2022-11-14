class Game:
    def __init__(self, team_1, team_1_score, team_2, team_2_score, location, date, winner, id=None):
        self.team_1 = team_1
        self.team_1_score = team_1_score
        self.team_2 = team_2
        self.team_2_score = team_2_score
        self.location = location
        self.date = date
        self.winner = winner
        self.id = id
