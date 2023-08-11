class Team:
    def __init__(self, name, race, total_wins, total_losses, total_fouls, id=None):
        self.name = name
        self.race = race
        self.total_wins = total_wins
        self.total_losses = total_losses
        self.total_fouls = total_fouls
        self.id = id


# A method to calculate the total points a team has accumulated when at the point of being called.

# The method will consist of an if statement to check to see if the values passed in as arguments
#  are either a string or an integer. This is to ensure the rest of the method will compute as the league table
# which this method will feed into will not be able to accept string values when sorting.

# if the passed in value string is true, the method will return 0 to ensure the

# if the method if statement is false for a string value, it will execute the following

# The method will determine total points by wins minus fouls, and return the total as an integer




    def total_points(self):
        if self.total_wins == None or self.total_fouls == None:
            return 0

        total_points = self.total_wins - self.total_fouls
        return total_points

    def get_team_name(self):
       return self.name

