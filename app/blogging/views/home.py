#blogging main function of nohdata
from flask import (
    Blueprint,
    request,
    render_template,
    session,
    jsonify)
import json
import bson


blogging = Blueprint("blogging", __name__)

@blogging.route('\home', methods = ["POST", "GET"])
def home():
    if request.method == "POST":
        return render_template("app/templates/home.html")
        
@blogging.route("\config", methods = ["POST", "GET"])
def config():
    if request.method == "POST":
        if request.values() == "config":
            return render_template("app/templates/configuration.html")
        elif request.values() == "back":
            return render_template("app/templates/home.html")
        return render_template("app/templates/home.html")
    