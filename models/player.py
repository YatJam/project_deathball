class Player:
    def __init__(self, name, race, team, position, status, special, id=None):
        self.name = name
        self.race = race
        self.team = team
        self.position = position
        self.status = status
        self.special = special
        self.id = id