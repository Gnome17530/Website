#This is the apperent way to download flask
from flask import Flask,g, render_template, request, redirect

import sqlite3

app = Flask(__name__)

DATABASE = 'list.db'


def get_db():
    db = getattr(g, '_list', None)
    if db is None:
        db = g._list = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_list', None)
    if db is not None:
        db.close()
    
@app.route("/")
def home():
    cursor = get_db().cursor()
    sql = "SELECT * FROM Contents"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template("contents.html", results=results)


@app.route('/add' , methods=["GET","POST"])
def add():
    if request.method == "POST":
        cursor = get_db().cursor()
        new_name = request.form["item_name"]
        new_definition = request.form["item_definition"]
        sql = "INSERT INTO Contents(name, definition) VALUES (?,?)"
        cursor.execute(sql,(new_name,new_definition))
        get_db().commit()
    return redirect('/')

@app.route('/delete', methods=["GET", "POST"])
def delete():
    if request.method == "POST":
        #get the item and deleting it from the database
        cursor = get_db().cursor()
        id = int(request.form["item_name"])
        sql = "DELETE FROM contents WHERE id=?"
        cursor.execute(sql, (id,))
        get_db().commit()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)