import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from todo.db import get_db


bp = Blueprint('todo', __name__, url_prefix='/todo')

