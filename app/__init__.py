from flask import Flask
from app.routes import mod_app


app = Flask(__name__)

app.register_blueprint(mod_app)