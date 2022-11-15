from flask import Blueprint, Flask, redirect, render_template, request

from models.game import Game
import repositories.game_repository as game_repository
import repositories.team_repository as team_repository
import repositories.player_repository as player_repository

games_blueprint = Blueprint("game", __name__)

@games_blueprint.route("/games")
def games():
    games = game_repository.select_all()
    teams = team_repository.select_all()
    return render_template("games/index.html", games=games, teams=teams)

@games_blueprint.route("/games", methods=["POST"])
def create_game():
    home_team_id = request.form['home_team_id']
    home_team = team_repository.select(home_team_id)
    home_team_score = 0
    away_team_id = request.form['away_team_id']
    away_team = team_repository.select(away_team_id)
    away_team_score = 0
    location = request.form['location']
    date = request.form['date']
    new_game = Game(home_team, home_team_score, away_team, away_team_score, location, date)
    game_repository.save(new_game)
    return redirect("/games")

@games_blueprint.route("/games/<id>/edit")
def edit_game(id):
    game = game_repository.select(id)
    home_team = team_repository.select(game.home_team.id)
    away_team = team_repository.select(game.away_team.id)
    teams = team_repository.select_all()[1:]
    return render_template('games/edit.html', game=game, home_team=home_team, away_team=away_team, teams=teams)

@games_blueprint.route("/games/<id>", methods=["POST"])
def update_game(id):
    home_team_id = request.form['home_team_id']
    home_team = team_repository.select(home_team_id)
    home_team_score = request.form['home_team_score']
    away_team_id = request.form['away_team_id']
    away_team = team_repository.select(away_team_id)
    away_team_score = request.form['away_team_score']
    location = request.form['location']
    date = request.form['date']
    game = Game(home_team, home_team_score, away_team, away_team_score, location, date, id)
    game_repository.update(game)
    return redirect("/games")

@games_blueprint.route("/games/<id>/delete", methods=["POST"])
def delete_game(id):
    game_repository.delete(id)
    return redirect("/game")

@games_blueprint.route("/games/<id>/teams")
def show_teams_players(id):
    game = game_repository.select(id)
    home_team_players = team_repository.show_players(game.home_team)
    away_team_players = team_repository.show_players(game.away_team)
    return render_template('games/teams.html', game=game, home_team_players=home_team_players, away_team_players=away_team_players)