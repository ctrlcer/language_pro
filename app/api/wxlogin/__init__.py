from flask import Blueprint

wx_login_api = Blueprint('wx_login_api', __name__)
from . import views
