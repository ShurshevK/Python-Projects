from flask import Blueprint, render_template, request, jsonify, redirect, url_for
#create blueprint url views
views = Blueprint(__name__, "views")

#make route to url with slash called view
@views.route("/")
# return in view html file index
def home():
    return render_template("index.html", name="Kir", age=26)

# create profile to make website more dinamic   
@views.route("/profile")
def profile():
    # args = request.args
    # name = args.get("name")
    # return render_template("index.html", name=name)
    return render_template("profile.html")

#return json
@views.route("/json")
def get_json():
    return jsonify({"name": "kir", "coolness": 10})

#recieve data in json format
@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)    

#redirect
@views.route("/go-to")
def go_to():
    return redirect(url_for("views.get_json"))

