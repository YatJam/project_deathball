from db.run_sql import run_sql

from models.player import Player

def save(player):
    sql = "INSERT INTO players (name, position, special_ability, status) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [player.name, player.position, player.special_ability, player.status]
    results = run_sql(sql, values)
    id = results[0]['id']
    player.id = id


def select_all():
    players = []
    sql = "SELECT * FROM players"
    results = run_sql(sql)
    for result in results:
        player = Player(result["name"], result["position"], result["special_ability"], result["status"], result["id"])
        players.append(player)
    return players


def select(id):
    player = None 
    sql = "SELECT * FROM players WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        player = Player(result["name"], result["position"], result["special_ability"], result["status"], result["id"])
    return player


def delete_all():
    sql = "DELETE FROM players"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM players WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(player):
    sql = "UPDATE players SET (name, position, special_ability, status) = (%s, %s, %s, %s) WHERE id = %s"
    values = [player.name, player.position, player.special_ability, player.status, player.id]
    run_sql(sql, values)