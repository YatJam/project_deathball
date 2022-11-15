from db.run_sql import run_sql
from models.game import Game
from repositories import player_repository, team_repository



def save(game):
    sql = """
    INSERT INTO games (home_team_id, home_team_score, away_team_id, away_team_score, location, date, winner_id) 
    VALUES (%s, %s, %s, %s, %s, %s, %s) 
    RETURNING id
    """
    values = [game.home_team.id, game.home_team_score, game.away_team.id, game.away_team_score, game.location, game.date, game.winner.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    game.id = id

def select_all():
    games = []
    sql = "SELECT * FROM games"
    results = run_sql(sql)
    
    for result in results:
        home_team_id = result['home_team_id']
        away_team_id = result['away_team_id']
        winner_id = result['winner_id']
        home_team = team_repository.select(home_team_id)
        away_team = team_repository.select(away_team_id)
        winner = team_repository.select(winner_id)
        game = Game(home_team, result["home_team_score"], away_team, result["away_team_score"], result["location"], result["date"], winner, result["id"])
        games.append(game)
    return games

def select(id):
    game = None
    sql = """
    SELECT * FROM games
    WHERE id = %s
    """
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        home_team_id = result['home_team_id']
        away_team_id = result['away_team_id']
        winner_id = result['winner_id']
        home_team = team_repository.select(home_team_id)
        away_team = team_repository.select(away_team_id)
        winner = team_repository.select(winner_id)
        game = Game(home_team, result["home_team_score"], away_team, result["away_team_score"], result["location"], result["date"], winner, result["id"])
    return game

def delete_all():
    sql= "DELETE FROM games"
    run_sql(sql)

def delete(id):
    sql = """
    DELETE FROM games
    WHERE id = %s
    """
    values = [id]
    run_sql(sql, values)

def update(game):
    sql = """
    UPDATE games SET (home_team_id, home_team_score, away_team_id, away_team_score, location, date, winner_id) = 
    (%s, %s, %s, %s, %s, %s, %s) 
    WHERE id = %s"""
    values = [game.home_team.id, game.home_team_score, game.away_team.id, game.away_team_score, game.location, game.date, game.winner.id]
    run_sql(sql, values)

def show_teams_players(game):
    teams = []
    sql = """SELECT players.id AS player_id
    FROM players
    INNER JOIN teams
    ON players.id = teams.player_id
    INNER JOIN games
    ON teams.id = games.teams_id WHERE teams.id = %s"""
    values = [game.id]
    results = run_sql(sql, values)
    for result in results:
        team = team_repository.select(result["team_id"])
        teams.append(team)
    return teams   