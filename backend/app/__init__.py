import base64

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import select

from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)

from app.models import *

# with app.app_context():
#     print(db.session.execute(select(Status)).all())
# CORS(app, resources={r'/*': {'origins': '*'}})