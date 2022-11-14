from flask import Blueprint, Flask, redirect, render_template, request

from models.game import Game
import repositories.game_repository as game_repository

games_blueprint = Blueprint("game", __name__)