import json
from flask import request, jsonify
from app import db
from app.models import Class
from . import chapters_api


@chapters_api.route('/api/chapters/all', methods=['POST', 'GET'])
def chapters_api():
    if request.method == 'POST':
        data = request.get_data()
        dic = json.loads(data.decode('utf-8'))
        class_id = dic['class_id']
        cls = Class.query.filter(Class.id == class_id).first()
        result = list()
        if cls is None:
            return jsonify(result)
        chapters = cls.chapters
        for chapter in chapters:

            lis = list()
            for i in  range(2):
                temp = dict()
                temp["chapter_name"] = chapter.chapter_name
                temp["time_length"] = str(chapter.time_length)
                temp["vedio_url"] = chapter.vedio_url
                lis.append(temp)
            result.append(lis)
        return jsonify(result)
