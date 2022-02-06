import os
from datetime import datetime
from flask import flash, url_for, redirect, render_template, current_app
from app import db
from app.documentation import bp
from flask_login import current_user, login_required

@bp.route('/index')
def index():
    return( render_template( 'documentation/index.html' ))
