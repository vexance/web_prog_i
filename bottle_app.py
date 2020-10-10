# Simple web programming class example app
import os
import sqlite3

from bottle import get, post, request, response, template, redirect

ON_PYTHONANYWHERE = "PYTHONANYWHERE_DOMAIN" in os.environ.keys()

if ON_PYTHONANYWHERE:
    from bottle import default_app
else:
    from bottle import run, debug


@get('/')
def get_show_list():
    # Fetch database records
    connection = sqlite3.connect("spaghetti.db")
    cursor = connection.cursor()
    cursor.execute("select * from spaghetti")
    result = cursor.fetchall()
    cursor.close()

    # Now check the cookie for pasta favorites
    fav_pasta = str(request.cookies.get('fav_pasta', -1))
    return template("show_list", rows=result, fav=fav_pasta)

@get('/favorite/<id:int>/')
def get_favorite(id):
    # Update or remove favorite pasta
    current = request.cookies.get('fav_pasta', None)
    if current == id:
        response.set_cookie('fav_pasta', "")
    else:
        response.set_cookie('fav_pasta', str(id))
    redirect('/')

@get('/set_status/<id:int>/<rating:int>/')
def get_set_rating(id, value):
    connection = sqlite3.connect("spaghetti.db")
    cursor = connection.cursor()
    cursor.execute("update spaghetti set rating=? where id=?", (rating, id,))
    connection.commit()
    cursor.close()
    redirect('/')


@get('/new_item')
def get_new_item():
    return template("new_item")


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


@get('/update_item/<id:int>')
def get_update_item(id):
    connection = sqlite3.connect("spaghetti.db")
    cursor = connection.cursor()
    cursor.execute("select * from spaghetti where id=?", (id,))
    result = cursor.fetchall()
    cursor.close()
    return template("update_item", row=result[0])


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

@get('/delete_item/<id:int>')
def get_delete_item(id):
    print("we want to delete #" + str(id))
    connection = sqlite3.connect("spaghetti.db")
    cursor = connection.cursor()
    cursor.execute("delete from spaghetti where id=?", (id,))
    connection.commit()
    cursor.close()
    redirect('/')

if ON_PYTHONANYWHERE:
    application = default_app()
else:
    debug(True)
    run(host="localhost", port=80)


