# You will probably need more methods from flask but this one is a good start.
from flask import render_template, request, jsonify
from sqlalchemy import func
from random import randint
# Import things from Flask that we need.
from mtg import app, db

# Import our models
from models import Card, Edition

# Routing for the server.
@app.route("/")
def index():
    # You will need to serve something up here.
    return render_template('index.html')

@app.route('/search_cards/')
def search_cards():
    data = {"name": request.args.get('pyCardName')}
    card_string = ""
    card = db.session.query(Card).filter((Card.name).ilike("%" + data['name'] + "%")).all()

    for i in range(len(card)):
        if card[i].name not in card_string:
            card_string += card[i].name + "~"

    return card_string

@app.route('/get_card/')
def get_card():
    data = {"name": request.args.get('pyCardName')}
    card = db.session.query(Card).filter(func.lower(Card.name).ilike(func.lower("%" + data['name'] + "%"))).first()
    try:
        return jsonify(card.card_info())
    except AttributeError:
        return ""
        

@app.route('/get_random/')
def get_random():
    max = db.session.query(func.max(Card.id)).first()
    max = (max[0]) #get the first value from the tuple
    rand = randint(0, max)

    card = db.session.query(Card).filter(Card.id == rand).first()

    return jsonify(card.card_info())

@app.route('/cycle_editions/')
def cycle_editions():
    data = {"edition": request.args.get('pyEdition'),		
			"name": request.args.get('pyName')}

    card = db.session.query(Card).filter(Card.name == data['name']).filter(Card.edition_id > data['edition']).first()
    if card:
        return jsonify(card.card_info())
    else:
        card = db.session.query(Card).filter(Card.name == data['name']).first()
        return jsonify(card.card_info())

    
