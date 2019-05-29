from flask import request, json, jsonify
from app import db
from app.models import User
from . import get_open_id
from . import wx_login_api


def cat_user(open_id):
    result = User.query.filter_by(open_id=open_id).first()
    if result is None:
        return True


def append_user(open_id):
    user = User(open_id=open_id)
    db.session.add(user)
    db.session.commit()


@wx_login_api.route('/api/wx/login', methods=['POST', 'GET'])
def wx_api():
    if request.method == 'POST':
        data = request.get_data()
        dic = json.loads(data.decode('utf-8'))
        code = dic['code']
        result = get_open_id.get_oid(code)
        if cat_user(result["openid"]):
            append_user(result["openid"])
        return jsonify(result)
