from flask import Flask
from flask_pymongo import PyMongo

# Initialize Flask app
app = Flask(__name__)
app.config["SECRET_KEY"] = "db24c608640f5034b30b8e1e1eb5618ed0ffdbf5"
app.config["MONGO_URI"] = "mongodb+srv://zaidaanshiraz2004:zaidaanshiraz2004@cluster0.8stpo.mongodb.net/todo_database?retryWrites=true&w=majority"

# MongoDB initialization
mongodb_client = PyMongo(app)
db = mongodb_client.db

# Ensure routes are imported after app and db initialization
from application import routes
