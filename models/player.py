class Player:
    def __init__(self, name, race, team, position, special_ability, status, id=None):
        self.name = name
        self.race = race
        self.team = team
        self.position = position
        self.special_ability = special_ability
        self.status = status
        self.id = id