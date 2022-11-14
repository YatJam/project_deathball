from flask import Blueprint, Flask, redirect, render_template, request

from models.game import Game
import repositories.game_repository as game_repository
import repositories.team_repository as team_repository
import repositories.player_repository as player_repository

games_blueprint = Blueprint("game", __name__)

@games_blueprint.route("/games")
def games():
    games = game_repository.select_all()
    return render_template("games/index.html", games=games)

@games_blueprint.route("/games", methods=["POST"])
def create_game():
    home_team_id = request.form['home_team_id']
    home_team = team_repository.select(home_team_id)
    home_team_score = None
    away_team_id = request.form['away_team_id']
    away_team = team_repository.select(away_team_id)
    away_team_score = None
    location = request.form['location']
    date = request.form['date']
    winner = None
    new_game = Game(home_team, home_team_score, away_team, away_team_score, location, date, winner)
    game_repository.save(new_game)
    return redirect("/games")

@games_blueprint.route("/games/<id>/edit")
def edit_game(id):
    game = game_repository.select(id)
    home_team = team_repository.select()
    away_team = team_repository.select_all()
    return render_template('games/edit.html', game=game, home_team=home_team, away_team=away_team)

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
    winner = request.form['winner']
    game = Game(home_team, home_team_score, away_team, away_team_score, location, date, winner, id)
    game_repository.update(game)
    return redirect("/games")

@games_blueprint.route("/games/<id>/delete", methods=["POST"])
def delete_game(id):
    game_repository.delete(id)
    return redirect("/game")

@games_blueprint.route("/games/<id>")
def show_teams_players(id):
    game = game_repository.select(id)
    home_team = team_repository.show_teams_players(game)
    away_team = team_repository.show_teams_players(game)
    return render_template('games/teams.html', game=game, home_team=home_team, away_team=away_team)