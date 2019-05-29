from flask import Blueprint

vedios_api = Blueprint('vedios_api', __name__)
from . import views
