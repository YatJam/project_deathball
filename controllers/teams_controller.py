from flask import Blueprint, Flask, redirect, render_template, request

from models.team import Team
import repositories.team_repository as team_repository
import repositories.player_repository as player_repository

teams_blueprint = Blueprint("teams", __name__)

@teams_blueprint.route("/teams")
def teams():
    teams = team_repository.select_all()
    players = player_repository.select_all()
    return render_template("teams/index.html", teams=teams, players=players)

@teams_blueprint.route("/teams", methods=["POST"])
def create_team():
    name = request.form["name"]
    race = request.form["race"]
    total_wins = 0
    total_losses = 0
    total_fouls = 0
    new_team = Team(name, race, total_wins, total_losses, total_fouls)
    team_repository.save(new_team)
    return redirect("/teams")

@teams_blueprint.route("/teams/<id>/edit")
def edit_team(id):
    team = team_repository.select(id)
    return render_template('teams/edit.html', team=team)

@teams_blueprint.route("/teams/<id>", methods=["POST"])
def update_team(id):
    name = request.form["name"]
    race = request.form["race"]
    total_wins = request.form["total_wins"]
    total_losses = request.form["total_losses"]
    total_fouls = request.form["total_fouls"]
    team = Team(name, race, total_wins, total_losses, total_fouls, id)
    team_repository.update(team)
    return redirect("/teams")

@teams_blueprint.route("/teams/<id>/delete", methods=["POST"])
def delete_team(id):
    team_repository.delete(id)
    return redirect("/teams")

@teams_blueprint.route("/teams/<id>/players")
def show_team(id):
    team = team_repository.select(id)
    players = team_repository.show_players(team)

    return render_template('teams/players.html', team=team, players=players)