from db.run_sql import run_sql
from models.game import Game
from repositories import player_repository, team_repository



def save(game):
    sql = """
    INSERT INTO games (team_1_id, team_1_score, team_2_id, team_2_score, location, date, winner) 
    VALUES (%s, %s, %s, %s, %s, %s, %s) 
    RETURNING id
    """
    values = [game.team_1.id, game.team_1_score, game.team_2.id, game.team_2_score, game.location, game.date, game.winner]
    results = run_sql(sql, values)
    id = results[0]['id']
    game.id = id

def select_all():
    games = []
    sql = "SELECT * FROM games"
    results = run_sql(sql)
    
    for result in results:
        team_1_id = result['team_1_id']
        team_2_id = result['team_2_id']
        team_1 = team_repository.select(team_1_id)
        team_2 = team_repository.select(team_2_id)
        game = Game(team_1, result["team_1_score"], team_2, result['id'], result["team_2_score"], result["location"], result["date"], result["winner"])
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
        team_1_id = result['team_1_id']
        team_2_id = result['team_2_id']
        team_1 = team_repository.select(team_1_id)
        team_2 = team_repository.select(team_2_id)
        game = Game(team_1, result["team_1_score"], team_2, result['id'], result["team_2_score"], result["location"], result["date"], result["winner"])
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
    UPDATE games SET (team_1_id, team_1_score, team_2_id, team_2_score, location, date, winner) = 
    (%s, %s, %s, %s, %s, %s, %s) 
    WHERE id = %s
    """
    values = [game.team_1.id, game.team_1_score, game.team_2.id, game.team_2_score, game.location, game.date, game.winner]
    run_sql(sql, values)