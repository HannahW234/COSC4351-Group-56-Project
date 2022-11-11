from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/table.html', methods = ['POST', 'GET'])
def table(): 
    if request.method == 'POST': 
        return render_template('table.html')

@app.route('/reservation.html', methods = ['POST', 'GET'])
def reservation(): 
    if request.method == 'GET':
        return render_template('reservation.html')

@app.route('/login.html', methods = ['POST', 'GET'])
def login(): 
    if request.method == 'GET':
        return render_template('login.html')

'''def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn'''