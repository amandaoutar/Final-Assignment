from typing import List, Dict
import simplejson as json
from flask import Flask, request, Response, redirect
from flask import render_template
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

app = Flask(__name__)
mysql = MySQL(cursorclass=DictCursor)

app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_DB'] = 'oscarmaleData'
mysql.init_app(app)


@app.route('/', methods=['GET'])
def index():
    user = {'username': 'Oscar Actors Project'}
    cursor = mysql.connect().cursor()
    cursor.execute('SELECT * FROM oscar_age_male')
    result = cursor.fetchall()
    return render_template('index.html', title='Home', user=user, actors=result)

@app.route('/view/<int:actor_id>', methods=['GET'])
def record_view(actor_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM oscar_age_male WHERE id=%s', actor_id)
    result = cursor.fetchall()
    return render_template('view.html', title='View Form', actor=result[0])


@app.route('/edit/<int:actor_id>', methods=['GET'])
def form_edit_get(actor_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM oscar_age_male WHERE id=%s', actor_id)
    result = cursor.fetchall()
    return render_template('edit.html', title='Edit Form', actor=result[0])
