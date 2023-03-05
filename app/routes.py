from flask import Blueprint, render_template, request
import datetime
import logging
import os

logger = logging.getLogger(__name__)
mod_app = Blueprint('mod_app', __name__,
                    static_folder='static',
                    template_folder=os.path.abspath('templates'))

@mod_app.route("/")
def home():
    return render_template('index.html', utc_dt=datetime.datetime.now().astimezone())

@mod_app.route("/about",  methods=["GET", "POST"])
def about():
    if request.method == "GET":
        return render_template('about.html', utc_dt=datetime.datetime.now().astimezone())
    else:
        print(request.form)

@mod_app.route('/comments/')
def comments():
    comments = ['This is the first comment.',
                'This is the second comment.',
                'This is the third comment.',
                'This is the fourth comment.'
                ]

    return render_template('comments.html', comments=comments)
