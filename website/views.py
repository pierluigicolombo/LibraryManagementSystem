'''
general views
'''

import json
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Book
from . import db

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    '''
    home view
    '''
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('note is too short', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('note added', category='success')
    return render_template("home.html", user=current_user)
    

@views.route('/aggiungiLibro', methods=['GET','POST'])
@login_required
def aggiungiLibro():
    '''
    home view
    '''
    if request.method == 'POST':
        title = request.form.get("title")
        description = request.form.get("description")
        author = request.form.get("author")
        publicationYear = int(request.form.get("publicationYear"))   
        numberOfCopies = int(request.form.get("numberOfCopies"))

        if publicationYear<0:
            flash('valore impossibile come anno di pubblicazione', category='error')
        else:
            # add user
            new_book = Book(title=title, description=description,
                            author=author, year_of_publication=publicationYear,
                            number_of_copies=numberOfCopies)
            db.session.add(new_book)
            db.session.commit()
            flash("book added", category='success')
    return render_template("AddBook.html", user=current_user)

@views.route('/visualizzaLibri', methods=['GET'])
@login_required
def visualizzaLibri():
    '''
    home view
    '''
    return "visualizza i libri!"
    #return render_template("home.html", user=current_user)




@views.route('/delete-note', methods=['POST'])
@login_required
def delete_note():
    '''
    delete note
    '''

    note = json.loads(request.data)
    note_id = note["noteId"]
    note = Note.query.get(note_id)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
