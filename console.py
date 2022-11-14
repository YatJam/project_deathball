import pdb

from models.player import Player
import repositories.player_repository as player_repository

from models.team import Team
import repositories.team_repository as team_repository

from models.game import Game
import repositories.game_repository as game_repository

from models.league import Leauge
import repositories.league_repository as league_repository

player_repository.delete_all()
team_repository.delete_all()
game_repository.delete_all()
league_repository.delete_all()

player_1 = Player("Brian", "Blocker", "blocks", "healthy")
player_repository.save(player_1)

player_2 = Player("Steve", "Blitzer", "fast", "healthy")
player_repository.save(player_2)

player_3 = Player("Alice", "Thrower", "can throw", "healthy")
player_repository.save(player_3)

team_1 = Team("Ork orkers", "Orks", "Steve", 4, 2, 14)
team_repository.save(team_1)

team_2 = Team("Dwarf Dwarves", "Dwarves", "Brian", 6, 3, 8)
team_repository.save(team_2)

team_3 = Team("Dead deads", "Undead", "Alice", 2, 4, 2)
team_repository.save(team_3)

pdb.set_trace()
