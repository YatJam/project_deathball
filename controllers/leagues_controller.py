from flask import Blueprint, Flask, redirect, render_template, request

from models.game import Game
import repositories.game_repository as game_repository
import repositories.team_repository as team_repository
import repositories.player_repository as player_repository

leagues_blueprint = Blueprint("league", __name__)

@leagues_blueprint.route("/leagues")
def leagues():
    teams = team_repository.select_all()
    players = player_repository.select_all()
    games = game_repository.select_all()
    return render_template("leagues/index.html", teams=teams, players=players, games=games)