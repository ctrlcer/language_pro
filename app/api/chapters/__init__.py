from flask import Blueprint

chapters_api = Blueprint('chapters_api', __name__)
from . import views
