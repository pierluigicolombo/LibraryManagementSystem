'''
create the app flask
'''


from flask import Flask
import os


def create_app():
    '''
    create the app flask
    '''
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv("FLASK_APP_SECRET_KEY") # ENCRYPT AND SECURE THE

    return app


app = create_app()
if __name__ == '__main__':
    app.run(debug=True)