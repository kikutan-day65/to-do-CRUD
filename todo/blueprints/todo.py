import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from todo.db import get_db


bp = Blueprint('todo', __name__, url_prefix='/todo')


@bp.route('/')
def todo():
    return render_template('todo.html')


@bp.route('/create')
def create():
    pass


@bp.route('/update')
def update():
    pass


@bp.route('/delete')
def delete():
    pass

