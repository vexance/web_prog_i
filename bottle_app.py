# Simple web programming class example app
import datetime
import time
import os
import random
import sqlite3
import uuid
import dataset
import json
from tinydb import TinyDB, Query
from bottle import get, post, request, response, template, redirect, static_file

db = TinyDB("sessions.json")
static_pasta_data = dataset.connect('sqlite:///spaghetti.db')
query = Query()
random.seed()

ON_PYTHONANYWHERE = "PYTHONANYWHERE_DOMAIN" in os.environ.keys()
if ON_PYTHONANYWHERE:
    from bottle import default_app
else:
    from bottle import run, debug

#========== Homepage / Index Page ==========#
@get('/')
def get_show_list():
    #========== Session check portion  ==========#
    session_id = request.cookies.get("session_id",None)
    if session_id == None or session_id == "LoggedOut":
        print(session_id)
        redirect('/login')
    else:   # had a cookie with an id, look up the session
        result = db.search(query.session_id == session_id)
        if len(result) == 0:    # the session isn't found, start a new one
            redirect('/login')
        else:   # the session is found, use it
            session_id = result[0]

    #========== Favorite Pasta Check ==========#
    fav_pasta = request.cookies.get('fav_pasta', None)
    if fav_pasta == None:
        response.set_cookie("fav_pasta", "-1", path="/")

    #========== Fetch Pasta Records ==========#
    connection = sqlite3.connect("spaghetti.db")
    cursor = connection.cursor()
    cursor.execute("select * from spaghetti")
    result = cursor.fetchall()
    cursor.close()
    return template("show_list", rows = result, session = session_id, fav = fav_pasta)

#========== Example Jacascript Page ==========#
@get('/sandbox')
def get_sandbox():
    return template("sandbox")

#========== Example Ajax Page ==========#
@get('/ajaxdemo')
def get_ajaxdemo():
    return template("ajaxdemo")

#========== Example jQuery Page ==========#
@get('/jquerydemo')
def get_jquerydemo():
    return template("jquerydemo")

#========== Navigation to Login Page ==========#
@get('/login')
def get_login():
    return template("login", csrf_token="331ed6fa-7eab-4aec-9134-8644d22a82fd")

#========== Login Attempt Handler ==========#
@post('/login')
def post_login():
    csrf_token = request.forms.get("csrf_token").strip()
    if csrf_token != "331ed6fa-7eab-4aec-9134-8644d22a82fd":
        print("CSRF Token Missing!")
        redirect('/login_error')
        return
    username = request.forms.get("username").strip()
    password = request.forms.get("password").strip()
    if password != "mysecretpassword":
        print("Incorrect Password!")
        redirect('/login_error')
        return
    session_id = request.cookies.get("session_id",str(uuid.uuid4()))
    result = db.search(query.session_id == session_id)
    if len(result) == 0:
        db.insert({'session_id':session_id, 'username':username})
    elif session_id == "LoggedOut":
        session_id = str(uuid.uuid4)
        db.insert({'session_id':session_id, 'username':username})
    else:
        session = result[0]
        db.update({'username':username},query.session_id == session_id)
    
    print("Updating cookie?")
    response.set_cookie("session_id",session_id, path="/")
    redirect('/')

#========== Logout Handler ==========#
@get('/logout')
def get_logout():
    session_id = request.cookies.get("session_id",str(uuid.uuid4()))
    result = db.search(query.session_id == session_id)
    if len(result) == 0:
        db.insert({'session_id':session_id, 'username':"Unknown"})
    else:
        db.update({'username':"Unknown"},query.session_id == session_id)
    response.set_cookie("session_id", "LoggedOut", path="/")
    redirect('/')

#========== Invalid Login Handler ==========#
@get('/login_error')
def get_login_error():
    return template("login_error")

#========== Pasta Rating Updater ==========#
@get('/set_status/<id:int>/<rating:int>/')
def get_set_rating(id, value):
    connection = sqlite3.connect("spaghetti.db")
    cursor = connection.cursor()
    cursor.execute("update spaghetti set rating=? where id=?", (rating, id,))
    connection.commit()
    cursor.close()
    redirect('/')

#========== Favorite Pasta Toggle ==========#
@get('/favorite/<id:int>/')
def get_favorite(id):
    # Update or remove favorite pasta
    current = request.cookies.get('fav_pasta', None)
    print("Current favorite: ", current)
    if current == str(id):
        response.set_cookie('fav_pasta', "-1", path="/")
        print("New Fav: " "-1")
    else:
        response.set_cookie('fav_pasta', str(id), path="/")
        print("New Fav: ", str(id))
    redirect('/')

#========== New Item Landing Page ==========#
@get('/new_item')
def get_new_item():
    return template("new_item")

#========== New Item Submission Handler ==========#
@post('/new_item')
def post_new_item():
    noodle = request.forms.get("noodle").strip()
    sauce = request.forms.get('sauce').strip()
    rating = request.forms.get('rating').strip()
    connection = sqlite3.connect("spaghetti.db")
    cursor = connection.cursor()
    cursor.execute("insert into spaghetti (noodle, sauce, rating) values (?,?,?)", (noodle, sauce, rating))
    connection.commit()
    cursor.close()
    redirect('/')

#========== Update Item Landing Page ==========#
@get('/update_item/<id:int>')
def get_update_item(id):
    connection = sqlite3.connect("spaghetti.db")
    cursor = connection.cursor()
    cursor.execute("select * from spaghetti where id=?", (id,))
    result = cursor.fetchall()
    cursor.close()
    return template("update_item", row=result[0])

#========== Update Item Submission Handler ==========#
@post('/update_item')
def post_update_item():
    id = int(request.forms.get("id").strip())
    noodle = request.forms.get("noodle").strip()
    sauce = request.forms.get("sauce").strip()
    rating = request.forms.get("rating").strip()
    connection = sqlite3.connect("spaghetti.db")
    cursor = connection.cursor()
    cursor.execute("update spaghetti set noodle=?, sauce=?, rating=? where id=?", (noodle, sauce, rating, id,))
    connection.commit()
    cursor.close()
    redirect('/')

#========== Pasta Rating Deletion ==========#
@get('/delete_item/<id:int>')
def get_delete_item(id):
    print("we want to delete #" + str(id))
    connection = sqlite3.connect("spaghetti.db")
    cursor = connection.cursor()
    cursor.execute("delete from spaghetti where id=?", (id,))
    connection.commit()
    cursor.close()
    redirect('/')

#========== Example CSS Animation Page ==========#
@get("/picture")
def get_picture():
    return template("picture")

#========== Static File Handler ==========#
@get("/static/<filename>")
def get_static(filename):
    print("searching for file...",filename)
    return static_file(filename, root='./static')

@get('/get_pastas_json')
def get_static_pastas():
    session_id = request.cookies.get("session_id",None)
    if session_id == None or session_id == "LoggedOut":
        print(session_id)
        redirect('/login')
    else:   # had a cookie with an id, look up the session
        result = db.search(query.session_id == session_id)
        if len(result) == 0:    # the session isn't found, start a new one
            redirect('/login')
        else:   # the session is found, use it
            response.content_type = 'application/json'
            result = static_pasta_data['spaghetti'].all()
            tasks= [dict(r) for r in result]
            text = json.dumps(tasks)
            return text

@get('/show_list_ajax')
def get_show_list_ajax():
    session_id = request.cookies.get("session_id",None)
    if session_id == None or session_id == "LoggedOut":
        print(session_id)
        redirect('/login')
    else:   # had a cookie with an id, look up the session
        result = db.search(query.session_id == session_id)
        if len(result) == 0:    # the session isn't found, start a new one
            redirect('/login')
        else:   # the session is found, use it
            session_id = result[0]

    return template("show_list_ajax", session=session_id)

#========== Run on Port 80 localy, or with PythonAnywhere defaults if hosted on PythonAnywhere.com ==========#
if ON_PYTHONANYWHERE:
    application = default_app()
else:
    debug(True)
    run(host="localhost", port=80)