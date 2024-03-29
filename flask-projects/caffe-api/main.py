from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    return render_template("index.html")

## HTTP GET - Read Record
@app.route("/random")
def random_cafe():
    all_cafes = db.session.query(Cafe).all() 
    cafe = random.choice(all_cafes)
    cafe_json = jsonify(
                            can_take_calls=cafe.can_take_calls,
                            coffee_price=cafe.coffee_price,
                            has_sockets=cafe.has_sockets,
                            has_toilet=cafe.has_toilet,
                            has_wifi=cafe.has_wifi,
                            id=cafe.id,
                            img_url=cafe.img_url,
                            location=cafe.location,
                            map_url=cafe.map_url,
                            name=cafe.name,
                            seats=cafe.seats)
    return jsonify(cafe=cafe_json.json)

## HTTP GET - Read Record
@app.route("/all")
def all_cafe():
    all_cafes = db.session.query(Cafe).all() 
    list = []
    for cafe  in all_cafes:
        cafe_json = jsonify(
                            can_take_calls=cafe.can_take_calls,
                            coffee_price=cafe.coffee_price,
                            has_sockets=cafe.has_sockets,
                            has_toilet=cafe.has_toilet,
                            has_wifi=cafe.has_wifi,
                            id=cafe.id,
                            img_url=cafe.img_url,
                            location=cafe.location,
                            map_url=cafe.map_url,
                            name=cafe.name,
                            seats=cafe.seats)
        list.append(cafe_json.json)
    resp = {"cafes": list}
    return resp

## HTTP GET - Read Record
@app.route("/search")
def search():
    location = request.args.get('loc').title()
    cafe = Cafe.query.filter(Cafe.location.like(f"%{location}%")).first()
    if not cafe:
        resp = { "error": {
            "Not Found": "Sorry, we don't have a cafe at that location"
            }
        }
        return resp, 404
    cafe = jsonify(
                            can_take_calls=cafe.can_take_calls,
                            coffee_price=cafe.coffee_price,
                            has_sockets=cafe.has_sockets,
                            has_toilet=cafe.has_toilet,
                            has_wifi=cafe.has_wifi,
                            id=cafe.id,
                            img_url=cafe.img_url,
                            location=cafe.location,
                            map_url=cafe.map_url,
                            name=cafe.name,
                            seats=cafe.seats)
    return jsonify(your_cafe=cafe.json)

## HTTP POST - Create Record   
@app.route("/add", methods=["POST"])
def add():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:id>", methods=["PATCH"])
def update_price(id):
    cafe = db.get_or_404(Cafe, id)
    price = request.args.get("new_price")
    if cafe:
        cafe.coffee_price = f"£{float(price)}"
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."})
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    
## HTTP DELETE - Delete Record
@app.route("/report-closed/<int:id>", methods=["DELETE"])
def delete_cafe(id):
    cafe = db.get_or_404(Cafe, id)
    key = request.args.get("api-key")
    if key == "TopSecretKey":
        if cafe:
            db.session.delete(cafe)
            db.session.commit() 
            return jsonify(response={"success": "Successfully deleted the cafe."})
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error="Access denied, wrong api key."), 403


if __name__ == '__main__':
    app.run(debug=True)
