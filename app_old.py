'''
create the app flask
'''

from os import path, getenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from website.views import views
from website.auth import auth
from website.models import User


db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    '''
    create the app flask
    '''
    app = Flask(__name__)
    app.config['SECRET_KEY'] = getenv("FLASK_APP_SECRET_KEY") # ENCRYPT AND SECURE THE
    # COOKIE AND SESSION DATA
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    '''
    create database if not exists
    '''
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print("created database")


app = create_app()
if __name__ == '__main__':
    app.run(debug=True)