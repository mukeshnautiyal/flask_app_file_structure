from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from db import db

#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:''@localhost/sqlalchemy_database"
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db = SQLAlchemy(app)

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"
    
if __name__ == "__main__":
    app.run()
    
app.run(host='localhost', port=5000)