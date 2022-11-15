from db.run_sql import run_sql
from models.player import Player
from models.team import Team
import repositories.player_repository as player_repository

def save(team):
    sql = """INSERT INTO teams 
    (name, race, total_wins, total_loses, total_fouls) 
    VALUES (%s, %s, %s, %s, %s) RETURNING id"""
    values = [team.name, team.race, team.total_wins, team.total_loses, team.total_fouls]
    results = run_sql(sql, values)
    id = results[0]['id']
    team.id = id


def select_all():
    teams = []
    sql = "SELECT * FROM teams"
    results = run_sql(sql)
    for result in results:
        team = Team(result["name"], result["race"], result["total_wins"], result["total_loses"], result["total_fouls"], result["id"])
        teams.append(team)
    return teams


def select(id):
    sql = "SELECT * FROM teams WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        team = Team(result["name"], result["race"], result["total_wins"], result["total_loses"], result["total_fouls"], result["id"])
    return team

def delete_all():
    sql = "DELETE FROM teams"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM teams WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(team):
    sql = """UPDATE teams SET 
    (name, race, total_wins, total_loses, total_fouls) = 
    (%s, %s, %s, %s, %s) WHERE id = %s"""
    values = [team.name, team.race, team.total_wins, team.total_loses, team.total_fouls, team.id]
    run_sql(sql, values)

def show_players(team):
    players = []
    sql = """SELECT players.id AS player_id
    FROM players
    INNER JOIN teams
    ON teams.id = teams.player_id WHERE team.id = %s"""
    values = [team.id]
    results = run_sql(sql, values)
    for result in results:
        player = player_repository.select(result["player_id"])
        players.append(player)
    return players
