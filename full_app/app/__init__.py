from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os

# Define the app
app = Flask(__name__)

# Define the database
USE_IN_MEMORY_FLAG = os.getenv("FLASK_DB_IN_MEMORY_FLAG", "True")
USE_IN_MEMORY = USE_IN_MEMORY_FLAG == "True"
if USE_IN_MEMORY:
    DATABASE_URI = "/"
else:
    DATABASE_URI = os.getenv("FLASK_DATABASE_URI", "/")


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + DATABASE_URI
print "Database uri in use is " + str(app.config["SQLALCHEMY_DATABASE_URI"])

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)