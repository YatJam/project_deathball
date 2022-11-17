import pdb

from models.player import Player
import repositories.player_repository as player_repository
from models.team import Team
import repositories.team_repository as team_repository
from models.game import Game
import repositories.game_repository as game_repository

player_repository.delete_all()
game_repository.delete_all()
team_repository.delete_all()

team_0 = Team("Bench Warmers", None, None, None, None)
team_repository.save(team_0)

team_1 = Team("Buckland Buccaneers", "Halflings", 32, 6, 14)
team_repository.save(team_1)

team_2 = Team("Dugrund's Iron Miners", "Dwarves", 42, 3, 29)
team_repository.save(team_2)

team_3 = Team("Imperial Marauders", "Humans", 28, 8, 13)
team_repository.save(team_3)

team_4 = Team("Snotgut's Sneeky Nosepickers", "Goblins", 14, 22, 57)
team_repository.save(team_4)

team_5 = Team("Transylvanian Nightmares", "Undead", 23, 14, 13)
team_repository.save(team_5)

team_6 = Team("Valinor Lightfoorts", "Elves", 35, 15, 2)
team_repository.save(team_6)

team_7 = Team("Zog's Krumperz", "Orcs", 39, 3, 48)
team_repository.save(team_7)

team_8 = Team("&@*(!@$(!£^(^09213@£!", "Daemons", 60, 1, 1)
team_repository.save(team_8)

player_1 = Player("Zogdush Smasha", "Orc", team_7, "Blocker", "healthy", "blocks")
player_repository.save(player_1)

player_2 = Player("Badrukk Stompa", "Orc", team_7, "Blitzer", "healthy", "fast")
player_repository.save(player_2)

player_3 = Player("Snizzgit", "Goblin", team_4, "Thrower", "healthy", "can throw")
player_repository.save(player_3)

player_4 = Player("Baghead", "Goblin", team_4, "Lineman", "healthy", "can stand there")
player_repository.save(player_4)

player_5 = Player("Rocknose", "Troll", team_4, "Star Player", "healthy", "can smash")
player_repository.save(player_5)

player_6 = Player("Throfil Ironboots", "Dwarf", team_2, "Blocker", "healthy", "can throw")
player_repository.save(player_6)

player_7 = Player("Bommin Redbeard", "Dwarf", team_2, "Star Player", "healthy", "Exellent attacker")
player_repository.save(player_7)

player_8 = Player("Countess Van de Lyon", "Human", team_3, "Star Player", "healthy", "Great alrounder")
player_repository.save(player_8)

player_9 = Player("Prince Wyne-Cooparrd", "Human", team_3, "Catcher", "healthy", "aloof")
player_repository.save(player_9)

player_10 = Player("Headless Harold", "Undead", team_5, "Blocker", "Dead", "Poor perception")
player_repository.save(player_10)

player_11 = Player("Pumpkin Head", "Undead", team_5, "lineman", "Dead", "Outstanding in his field")
player_repository.save(player_11)

player_12 = Player("Elizabeth Von Transylvania", "Undead", team_5, "Star Player", "healthy", "Vampire Overlord")
player_repository.save(player_12)

player_13 = Player("Frodo 'the dodger' Baggins", "Halfling", team_1, "Blitzer", "Healthy", "Got one of them secret rings")
player_repository.save(player_13)

player_14 = Player("Gandalf the Grey", "Human", team_1, "Coach", "Healthy", "Exceptionally wise")
player_repository.save(player_14)

player_15 = Player("Oakmund", "Treeman", team_1, "Star Player", "Healthy", "Balances the odds")
player_repository.save(player_15)

player_16 = Player("Baraborn", "Elf", team_6, "Blitzer", "Healthy", "Has pointy ears")
player_repository.save(player_16)

player_17 = Player("Noldorin", "Elf", team_6, "Star Player", "Healthy", "Exceptionally agile")
player_repository.save(player_17)

player_18 = Player("Galrandir", "Elf", team_6, "Thrower", "Healthy", "Can do some odd moves")
player_repository.save(player_18)

player_19 = Player("*&^&@%£!^%$^*", "Daemon", team_8, "Blitzer", "Healthy", "Not sure")
player_repository.save(player_19)

player_20 = Player("*@£%@*£@*%&", "Daemon", team_8, "Lineman", "Healthy", "No idea")
player_repository.save(player_20)

player_21 = Player("@£%$££££!", "Daemon", team_8, "Star Player", "Healthy", "is made of fire")
player_repository.save(player_21)

game_1 = Game(team_1, 21, team_3, 17, "Farmer Maggot's spare field", "2493-11-16")
game_repository.save(game_1)

game_2 = Game(team_1, 33, team_2, 44, "Pitch No.4", "2493-11-14")
game_repository.save(game_2)

game_3 = Game(team_2, 12, team_3, 28, "Dugrund's AstroTurf Palace", "2493-11-12")
game_repository.save(game_3)

game_4 = Game(team_2, 32, team_3, 29, "Dugrund's AstroTurf Palace", "2493-11-12")
game_repository.save(game_4)

game_5 = Game(team_6, 16, team_7, 21, "The Imperial Arena", "2493-11-11")
game_repository.save(game_5)

game_6 = Game(team_4, 8, team_8, 52, "Abyssal Plain", "2493-11-07")
game_repository.save(game_6)

pdb.set_trace()
