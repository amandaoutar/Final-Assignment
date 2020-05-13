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

@app.route('/edit/<int:actor_id>', methods=['POST'])
def form_update_post(actor_id):
    cursor = mysql.get_db().cursor()
    inputData = (
    request.form.get('Name'), request.form.get('Age'), request.form.get('Year'),
    request.form.get('Movie'), actor_id)
    sql_update_query = """UPDATE oscar_age_male t SET t.Name = %s, t.Age = %s, t.Year = %s, t.Movie = %s WHERE t.id = %s """
    cursor.execute(sql_update_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/actors/new', methods=['GET'])
def form_insert_get():
    return render_template('new.html', title='New Actors Form')
