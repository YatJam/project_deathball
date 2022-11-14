class Player:
    def __init__(self, name, race, position, special_ability, status, id=None):
        self.name = name
        self.race = race
        self.position = position
        self.special_ability = special_ability
        self.status = status
        self.id = id