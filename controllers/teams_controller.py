from flask import Blueprint, Flask, redirect, render_template, request

from models.team import Team
import repositories.team_repository as team_repository
import repositories.player_repository as player_repository

teams_blueprint = Blueprint("teams", __name__)

@teams_blueprint.route("/teams")
def teams():
    teams = team_repository.select_all()
    return render_template("teams/index.html", teams=teams)

@teams_blueprint.route("/teams", methods=["POST"])
def create_team():
    name = request.form["name"]
    race = request.form["race"]
    players = request.form["players"]
    star_player_id = request.form["star_player_id"]
    star_player = player_repository.select(star_player_id)
    total_wins = request.form["total_wins"]
    total_loses = request.form["total_loses"]
    total_fouls = request.form["total_fouls"]
    new_team = Team(name, race, players, star_player, total_wins, total_loses, total_fouls)
    team_repository.save(new_team)
    return redirect("/teams")

@teams_blueprint.route("/teams/<id>/edit")
def edit_team(id):
    team = team_repository.select(id)
    star_player = player_repository.select_all()
    return render_template('teams/edit.html', team=team, star_player=star_player)

@teams_blueprint.route("/teams/<id>", methods=["POST"])
def update_team(id):
    name = request.form["name"]
    race = request.form["race"]
    players = request.form["players"]
    star_player_id = request.form["star_player_id"]
    star_player = player_repository.select(star_player_id)
    total_wins = request.form["total_wins"]
    total_loses = request.form["total_loses"]
    total_fouls = request.form["total_fouls"]
    team = Team(name, race, players, star_player, total_wins, total_loses, total_fouls, id)
    team_repository.update(team)
    return redirect("/teams")

@teams_blueprint.route("/teams/<id>/delete", methods=["POST"])
def delete_team(id):
    team_repository.delete(id)
    return redirect("/teams")

@teams_blueprint.route("/teams/<id>")
def show_team(id):
    team = team_repository.select(id)
    players = team_repository.show_players(team)
    return render_template('teams/player.html', team=team, players=players)