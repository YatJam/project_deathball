import pdb

from models.player import Player
import repositories.player_repository as player_repository
from models.team import Team
import repositories.team_repository as team_repository
from models.game import Game
import repositories.game_repository as game_repository

game_repository.delete_all()
team_repository.delete_all()
player_repository.delete_all()

player_1 = Player("Brian", "Human", "Blocker", "blocks", "healthy")
player_repository.save(player_1)

player_2 = Player("Steve", "Elf", "Blitzer", "fast", "healthy")
player_repository.save(player_2)

player_3 = Player("Alice", "Dwarf", "Thrower", "can throw", "healthy")
player_repository.save(player_3)

team_1 = Team("Ork orkers", "Orks", player_1, 4, 2, 14)
team_repository.save(team_1)

team_2 = Team("Dwarf Dwarves", "Dwarves", player_2, 6, 3, 8)
team_repository.save(team_2)

team_3 = Team("Dead deads", "Undead", player_3, 2, 4, 2)
team_repository.save(team_3)

game_1 = Game(team_1, 21, team_3, 17, "Black Castle", "23.05.3019", team_2)
game_repository.save(game_1)

game_2 = Game(team_1, 33, team_2, 44, "Pitch No.4", "28.05.3019", team_2)
game_repository.save(game_2)

game_3 = Game(team_2, 12, team_3, 28, "Playgound", "02.06.3019", team_3)
game_repository.save(game_3)

pdb.set_trace()
