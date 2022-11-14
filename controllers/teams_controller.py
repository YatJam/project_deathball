from flask import Blueprint, Flask, redirect, render_template, request

from models.team import Team

teams_blueprint = Blueprint("team", __name__)

# INDEX
@teams_blueprint.route("/teams")
def teams():
    teams = team_repository.select_all()
    return render_template("teams/index.html", teams=teams)