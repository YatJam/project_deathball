from flask import Blueprint, Flask, redirect, render_template, request

from models.game import Game
from models.team import Team
import repositories.game_repository as game_repository
import repositories.team_repository as team_repository
import repositories.player_repository as player_repository

leagues_blueprint = Blueprint("league", __name__)

@leagues_blueprint.route("/leagues")
def leagues():
    teams = team_repository.select_all()[1:]
    players = player_repository.select_all()
    games = game_repository.select_all()
    teams.sort(key=Team.total_points, reverse=True)
    return render_template("leagues/index.html", teams=teams, players=players, games=games)