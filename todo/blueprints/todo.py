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


@bp.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    db = get_db()

    if request.method == 'POST':
        new_item = request.form['content']
        db.execute(
            "UPDATE todo SET content = ? WHERE id = ?",
            (new_item, id)
        )
        db.commit()
        return redirect(url_for('todo.todo'))

    item = db.execute(
        "SELECT * FROM todo WHERE id = ?",
        (id,)
    ).fetchone()

    return render_template('update_form.html', item=item)


@bp.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    db = get_db()

    if request.method == 'POST':
        db.execute(
            "DELETE FROM todo WHERE id = ?",
            (id,)
        )
        db.commit()
        return redirect(url_for('todo.todo'))

    item = db.execute(
        "SELECT * FROM todo WHERE id = ?",
        (id,)
    ).fetchone()

    return render_template('delete_form.html', item=item)
