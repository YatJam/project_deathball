from flask import Blueprint, Flask, redirect, render_template, request

from models.player import Player
import repositories.player_repository as player_repository
from models.team import Team
import repositories.team_repository as team_repository

players_blueprint = Blueprint("player", __name__)

@players_blueprint.route("/players")
def players():
    players = player_repository.select_all()
    return render_template("players/index.html", players=players)

@players_blueprint.route("/players/<id>/player")
def player(id):
    player = player_repository.select(id)
    return render_template("players/player.html", player=player)

@players_blueprint.route("/players/new")
def new_player():
    return render_template("players/new.html")

@players_blueprint.route("/players", methods=["POST"])
def create_player():
    name = request.form["name"]
    race = request.form["race"]

    team = team_repository.select(id=1) # By default, we assign a player to the Substitutions Team
    if "team_id" in request.form.keys():
        team_id = request.form['team_id']
        team = team_repository.select(team_id)
    
    position = request.form["position"]
    status = "Healthy"
    special = request.form["special"]
    new_player = Player(name, race, team, position, status, special)
    player_repository.save(new_player)
    return redirect("/players")

@players_blueprint.route("/players/<id>/edit")
def edit_player(id):
    player = player_repository.select(id)
    teams = team_repository.select_all()
    return render_template('players/edit.html', player=player, teams=teams)

@players_blueprint.route("/players/<id>", methods=["POST"])
def update_player(id):
    name = request.form["name"]
    race = request.form["race"]
    team_id = request.form['team_id']
    position = request.form["position"]
    status = request.form["status"]
    special = request.form["special"]
    team = team_repository.select(team_id)
    player = Player(name, race, team, position, status, special, id)

    player_repository.update(player)
    return redirect("/players")

@players_blueprint.route("/players/<id>/delete", methods=["POST"])
def delete_player(id):
    player_repository.delete(id)
    return redirect("/players")
