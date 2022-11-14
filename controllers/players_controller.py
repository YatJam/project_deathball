from flask import Blueprint, Flask, redirect, render_template, request

from models.player import Player
import repositories.player_repository as player_repository

players_blueprint = Blueprint("player", __name__)

@players_blueprint.route("/players")
def players():
    players = player_repository.select_all()
    return render_template("players/index.html", players=players)

@players_blueprint.route("/players/new")
def new_player():
    return render_template("players/new.html")

@players_blueprint.route("/players", methods=["POST"])
def create_player():
    name = request.form["name"]
    position = request.form["position"]
    special_ability = request.form["special_ability"]
    status = request.form["status"]
    new_player = Player(name, position, special_ability, status)
    player_repository.save(new_player)
    return redirect("/players")

@players_blueprint.route("/players/<id>/edit")
def edit_player(id):
    player = player_repository.select(id)
    return render_template('players/edit.html', player=player)

@players_blueprint.route("/players/<id>", methods=["POST"])
def update_player(id):
    name = request.form["name"]

    player = Player(name, id)
    player_repository.update(player)
    return redirect("/players")

@players_blueprint.route("/players/<id>/delete", methods=["POST"])
def delete_player(id):
    player_repository.delete(id)
    return redirect("/players")
