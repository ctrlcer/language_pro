from flask import request, json, jsonify
from . import classes_api
from app import db
from app.models import Class
@classes_api.route('/api/classes/all', methods=['POST', 'GET'])
def classes_api():
    if request.method == 'POST':
        clsses = Class.query.all()
        s = list()
        # class_name, teacher_name, rating, classes_num, students_num, description
        for cls in clsses:
            temp = dict()
            temp['class_id'] = cls.id
            temp['class_name'] = cls.class_name
            temp['teacher_name'] = cls.teacher_name
            temp['rating'] = cls.rating
            temp['classes_num'] = cls.classes_num
            temp['students_num'] = cls.students_num
            temp['description'] = cls.description
            s.append(temp)
        return jsonify(s)
