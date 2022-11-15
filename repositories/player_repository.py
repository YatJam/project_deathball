from db.run_sql import run_sql

from models.player import Player
from models.team import Team
import repositories.team_repository as team_repository

def save(player):
    sql = "INSERT INTO players (name, race, team_id, position, status, special) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [player.name, player.race, player.team.id, player.position, player.status, player.special]
    results = run_sql(sql, values)
    id = results[0]['id']
    player.id = id


def select_all():
    players = []
    sql = "SELECT * FROM players"
    results = run_sql(sql)
    for result in results:
        team_id = result['team_id']
        team = team_repository.select(team_id)
        player = Player(result["name"], result["race"], team, result["position"], result["status"], result["special"], result["id"])
        players.append(player)
    return players


def select(id):
    player = None 
    sql = "SELECT * FROM players WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        team_id = result['team_id']
        team = team_repository.select(team_id)
        player = Player(result["name"], result["race"], team, result["position"], result["status"], result["special"], result["id"])
    return player


def delete_all():
    sql = "DELETE FROM players"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM players WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(player):
    sql = "UPDATE players SET (name, race, team_id, position, status, special) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [player.name, player.race, player.team.id, player.position, player.status, player.special, player.id]
    run_sql(sql, values)