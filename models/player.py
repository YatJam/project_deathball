class Player:
    def __init__(self, name, position, special_ability, status, id=None):
        self.name = name
        self.position = position
        self.special_ability = special_ability
        self.status = status
        self.id = id