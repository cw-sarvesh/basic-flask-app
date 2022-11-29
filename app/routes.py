from flask import Blueprint, render_template_string, render_template
import datetime
import logging
import os


logger = logging.getLogger(__name__)
mod_app = Blueprint('mod_app', __name__,
                    template_folder=os.path.abspath('templates'))

# TEMP_FOLDER='./templates/'
# api = Api(mod_app)


@mod_app.route("/")
def home():
    return render_template('index.html', utc_dt=datetime.datetime.now().astimezone())


@mod_app.route("/about")
def about():
    return render_template('about.html', utc_dt=datetime.datetime.now().astimezone())


@mod_app.route('/comments/')
def comments():
    comments = ['This is the first comment.',
                'This is the second comment.',
                'This is the third comment.',
                'This is the fourth comment.'
                ]

    return render_template('comments.html', comments=comments)
