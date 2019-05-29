from flask import Blueprint

muiscs_api = Blueprint('muiscs_api', __name__)
from . import views
