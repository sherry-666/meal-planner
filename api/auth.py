#authentication validation
#input: username & password


import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)


bp = Blueprint('login', __name__, url_prefix='/grocery-list')

@bp.route('/display')
#display list
def display_grocery_list():

    return render_template('function/grocery_list.html')

