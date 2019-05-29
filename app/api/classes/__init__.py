from flask import Blueprint

classes_api = Blueprint('classes_api', __name__)
from . import views
