from flask import blueprints
import app


api_blueprint = blueprints(app,"Blueprint")

@api_blueprint.route('\home_click', method = "POST")
def home_click():
    if request.method == "POST":
        
        
    