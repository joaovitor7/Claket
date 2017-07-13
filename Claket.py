from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/mydb'

db = SQLAlchemy(app)

from Controllers import *

if __name__ == '__main__':
    app.run(host='0.0.0.0')