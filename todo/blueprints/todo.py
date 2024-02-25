import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from todo.db import get_db


bp = Blueprint('todo', __name__, url_prefix='/todo')


@bp.route('/', methods=['GET'])
def todo():
    db = get_db()

    items = db.execute(
        "SELECT * FROM todo",
    ).fetchall()

    return render_template('todo.html', items=items)


@bp.route('/create', methods=['POST'])
def create():
    if request.method == 'POST':
        db = get_db()
        content = request.form['content']
        print(content)

        db.execute(
            "INSERT INTO todo (content) VALUES (?)",
            (content,)
        )
        db.commit()

        return redirect(url_for('todo.todo'))
    
    return redirect(url_for('todo.todo'))


@bp.route('/update')
def update():
    pass


@bp.route('/delete')
def delete():
    pass

