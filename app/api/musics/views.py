from flask import request, json, jsonify
from . import muiscs_api
from app import db
from app.models import Music


@muiscs_api.route('/api/musics/all', methods=['POST', 'GET'])
def musics_api():
    if request.method == 'POST':
        musics = Music.query.all()
        s = list()
        # class_name, teacher_name, rating, classes_num, students_num, description
        for music in musics:
            temp = dict()
            temp['music_id'] = music.id
            temp['music_name'] = music.music_name
            temp['singer_name'] = music.singer_name
            temp['music_url'] = music.music_url
            s.append(temp)
        return jsonify(s)
