from app import create_app, db
from flask_migrate import Migrate
from app.models import User

app = create_app()
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run('0.0.0.0')