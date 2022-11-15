class Game:
    def __init__(self, home_team, home_team_score, away_team, away_team_score, location, date, id=None):
        self.home_team = home_team
        self.home_team_score = home_team_score
        self.away_team = away_team
        self.away_team_score = away_team_score
        self.location = location
        self.date = date
        self.id = id
