import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html', utc_dt=datetime.datetime.now().astimezone())

@app.route("/about")
def about():
    return render_template('about.html', utc_dt=datetime.datetime.now().astimezone())


@app.route('/comments/')
def comments():
    comments = ['This is the first comment.',
                'This is the second comment.',
                'This is the third comment.',
                'This is the fourth comment.'
                ]

    return render_template('comments.html', comments=comments)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5001)
