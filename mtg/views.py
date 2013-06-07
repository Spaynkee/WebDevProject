# You will probably need more methods from flask but this one is a good start.
from flask import render_template, request, jsonify

# Import things from Flask that we need.
from mtg import app, db

# Import our models
from models import Card, Edition

# Routing for the server.
@app.route("/")
def index():
    # You will need to serve something up here.
    return render_template('index.html')
	
@app.route('/getCard/')
def getCard():
	data = {"name": request.args.get('pyCardName')}
	
	card = db.session.query('name').filter(Card.name == data['name']).first()
	graphic = db.session.query('image_url').filter(Card.name == data['name']).first()
	flavor = db.session.query('flavor_text').filter(Card.name == data['name']).first()
	illustrator = db.session.query('illustrator').filter(Card.name == data['name']).first()
	power = db.session.query('power').filter(Card.name == data['name']).first()
	type = db.session.query('type').filter(Card.name == data['name']).first()
	cost = db.session.query('cost').filter(Card.name == data['name']).first()
	abilities = db.session.query('abilities').filter(Card.name == data['name']).first()
	
	cardInfo = {"name": card, 
				"graphic": graphic,
				"flavor": flavor,
				"illustrator": illustrator,
				"power": power,
				"type": type,
				"cost": cost,
				"abilities": abilities}
	return jsonify(cardInfo)