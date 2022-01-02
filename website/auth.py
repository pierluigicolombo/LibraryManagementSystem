from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "loggato"

@auth.route('/logout')
def logout():
    return "sei uscito"

@auth.route("/sign-up")
def sign_up():
    return "sei entrato"
