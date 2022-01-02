'''
create the app flask
'''


from flask import Flask
import os

from flask.helpers import url_for

from website.views import views
from website.auth import auth

def create_app():
    '''
    create the app flask
    '''
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv("FLASK_APP_SECRET_KEY") # ENCRYPT AND SECURE THE

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app


app = create_app()
if __name__ == '__main__':
    app.run(debug=True)