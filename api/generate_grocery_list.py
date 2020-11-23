#generate grocery list
#input: selected meals
#ingredient aggregation

import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)


bp = Blueprint('grocery-list', __name__, url_prefix='/grocery-list')

@bp.route('/display')
#display list
def display_grocery_list():

    return render_template('function/grocery_list.html')

