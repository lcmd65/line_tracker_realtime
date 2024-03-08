#blogging main function of nohdata
from flask import (
    Blueprint,
    request,
    render_template,
    session,
    jsonify)
import json
import bson


api_blueprint = Blueprint("api_blueprint", __name__)

@api_blueprint.route('\home_click', method = ["POST", "GET"])
def home_click():
    if request.method == "POST":
        return render_template("app/templates/home.html")
        
        
        
    