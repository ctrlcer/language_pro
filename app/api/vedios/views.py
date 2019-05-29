from flask import request, json, jsonify
from . import vedios_api
from app import db
from app.models import Vedio


@vedios_api.route('/api/vedios/all', methods=['POST', 'GET'])
def musics_api():
    if request.method == 'POST':
        vedios = Vedio.query.all()
        s = list()
        # class_name, teacher_name, rating, classes_num, students_num, description
        for vedio in vedios:
            temp = dict()
            temp['vedio_id'] = vedio.id
            temp['vedio_name'] = vedio.vedio_name
            temp['vedio_url'] = vedio.vedio_url
            temp['director_name'] = vedio.director_name
            s.append(temp)
        return jsonify(s)
