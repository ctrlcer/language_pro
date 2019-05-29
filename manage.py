from app import db, create_app
from app.models import User, Class
from flask_script import Manager
from sqlalchemy import or_

app = create_app()
manage = Manager(app)


@manage.command
def init_database():
    db.drop_all()
    db.create_all()


@manage.command
def append_users():
    for i in range(100):
        user = User(open_id=str(i))
        db.session.add(user)

    db.session.commit()


@manage.command
def cat_user():
    # print(Image.query.order_by(Image.id.desc()).limit(10).all())
    print(User.query.all())


@manage.command
def cat_chapter():
    print(Class.query.filter(Class.id == 2).first().chapters)


if __name__ == '__main__':
    manage.run()
