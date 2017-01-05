# """
# Flask Documentation:     http://flask.pocoo.org/docs/
# Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
# Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
#
# This file creates your application.
# """

import os
import pg
from flask import Flask, render_template, request, redirect, url_for
from tdmpfflClass import *
import sys

reload(sys)
sys.setdefaultencoding('utf8')

app = Flask("MyApp")

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')

DBUSER=os.environ.get('DBUSER', True)
DBPASS=os.environ.get('DBPASS', True)
DBHOST=os.environ.get('DBHOST', True)
DBNAME=os.environ.get('DBNAME', True)

###
# Routing for your application.
###

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html",title="HOW IT ALL BEGAN...") \

@app.route("/champions")
def champions():
    return render_template("champions.html",title="PAST CHAMPIONS")\

@app.route("/chickenbowl")
def chickenbowl():
    return render_template("chickenbowl.html",title="CHICKENS")

@app.route("/standings")
def standings():
    return render_template("standings.html",title="Standings")

@app.route("/members")
def members():
    result_list = Owners.getOwners()
    return render_template("owners.html",result_list=result_list,title="Members of TDMPFFL")

@app.route("/<idowners>/teamnames")
def teamnames(idowners):
    idowners = idowners
    result_list = Teams.get_team_list(idowners)
    return render_template("teamnames.html",team_names=result_list,title="All Teams for")

@app.route("/alltime")
def alltime():
    result_list = Owners.alltime()
    return render_template("alltime.html",result_list=result_list,title="All time stats")

# @app.route("/<idowners>/owneryears")
# def alltime(idowners):
#     idowners = idowners
#     result_list = Owners.owneryears(idowners)
#     return render_template("owneryears.html",result_list=result_list,title="Owner by years")


if __name__=="__main__":
    app.run(debug=True)











# @app.route('/')
# def home():
#     """Render website's home page."""
#     db=pg.DB(host=DBHOST, user=DBUSER, passwd=DBPASS, dbname=DBNAME)
#     query=db.query("select * from album")
#     result_list = query.namedresult()
#     return render_template('home.html',result_list=result_list)
#
#
# @app.route('/about/')
# def about():
#     """Render the website's about page."""
#     return render_template('about.html')


###
# The functions below should be applicable to all Flask apps.
###

# @app.route('/<file_name>.txt')
# def send_text_file(file_name):
#     """Send your static text file."""
#     file_dot_text = file_name + '.txt'
#     return app.send_static_file(file_dot_text)
#
#
# @app.after_request
# def add_header(response):
#     """
#     Add headers to both force latest IE rendering engine or Chrome Frame,
#     and also to cache the rendered page for 10 minutes.
#     """
#     response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
#     response.headers['Cache-Control'] = 'public, max-age=600'
#     return response
#
#
# @app.errorhandler(404)
# def page_not_found(error):
#     """Custom 404 page."""
#     return render_template('404.html'), 404
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
