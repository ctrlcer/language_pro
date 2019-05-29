from . import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    open_id = db.Column(db.String(255), unique=True, nullable=False)

    def __init__(self, open_id):
        self.open_id = open_id

    def __repr__(self):
        return '<open_id %r>' % self.open_id


class Class(db.Model):
    __tablename__ = 'class'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    class_name = db.Column(db.String(255), unique=True, nullable=False)
    teacher_name = db.Column(db.String(30), nullable=False)
    rating = db.Column(db.Float(), default=0)
    classes_num = db.Column(db.Integer, default=0)
    students_num = db.Column(db.Integer, default=0)
    description = db.Column(db.Text)
    chapters = db.relationship('Chapter')
    progress = db.Column(db.Float)

    def __init__(self, class_name, teacher_name, rating, classes_num, students_num, description):
        self.class_name = class_name
        self.teacher_name = teacher_name
        self.rating = rating
        self.classes_num = classes_num
        self.students_num = students_num
        self.description = description

    def __repr__(self):
        return '<class_name %r>' % self.class_name


class Chapter(db.Model):
    __tablename__ = 'chapter'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time_length = db.Column(db.Time)
    chapter_name = db.Column(db.String(225))
    vedio_url = db.Column(db.String(255))
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'))

    def __init__(self, time_length, class_id):
        self.time_length = time_length
        self.class_id = class_id

    def __repr__(self):
        return '<Chapter %r>' % self.chapter_name


class Music(db.Model):
    __tablename__ = 'music'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    music_name = db.Column(db.String(225))
    singer_name = db.Column(db.String(225))
    music_url = db.Column(db.String(255))


class Vedio(db.Model):
    __tablename__ = 'vedio'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    vedio_name = db.Column(db.String(225))
    vedio_url = db.Column(db.String(225))
    director_name = db.Column(db.String(225))
