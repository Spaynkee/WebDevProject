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
	
@app.route('/getCard/')
def getCard():
	data = {"name": request.args.get('pyCardName')}
	
	card = db.session.query(Card.name).filter(Card.name == data['name']).first()
	graphic = db.session.query(Card.image_url).filter(Card.name == data['name']).first()
	flavor = db.session.query(Card.flavor_text).filter(Card.name == data['name']).first()
	illustrator = db.session.query(Card.illustrator).filter(Card.name == data['name']).first()
	power = db.session.query(Card.power).filter(Card.name == data['name']).first()
	type = db.session.query(Card.type).filter(Card.name == data['name']).first()
	cost = db.session.query(Card.cost).filter(Card.name == data['name']).first()
	abilities = db.session.query(Card.abilities).filter(Card.name == data['name']).first()

	cardInfo = {"name": card, 
				"graphic": graphic,
				"flavor": flavor,
				"illustrator": illustrator,
				"power": power,
				"type": type,
				"cost": cleanCost(cost),
				"abilities": cleanAbilities(abilities)}
	return jsonify(cardInfo)
	
@app.route('/getRandom/')
def getRandom():
	max = db.session.query(func.max(Card.id)).first()
	max = (max[0])	#get the first value from the tuple
	rand = randint(0, max)
	
	card = db.session.query('name').filter(Card.id == rand).first()
	graphic = db.session.query('image_url').filter(Card.id == rand).first()
	flavor = db.session.query('flavor_text').filter(Card.id == rand).first()
	illustrator = db.session.query('illustrator').filter(Card.id == rand).first()
	power = db.session.query('power').filter(Card.id == rand).first()
	type = db.session.query('type').filter(Card.id == rand).first()
	cost = db.session.query('cost').filter(Card.id == rand).first()
	abilities = db.session.query('abilities').filter(Card.id == rand).first()
	
	cardInfo = {"name": card, 
				"graphic": graphic,
				"flavor": flavor,
				"illustrator": illustrator,
				"power": power,
				"type": type,
				"cost": cleanCost(cost),
				"abilities": cleanAbilities(abilities)}
				
	return jsonify(cardInfo)
	
def cleanAbilities(abils):
	abilString = abils[0]
	
	abilString = abilString.replace("{T}", "<img class='symbol' src='/static/img/tap.png'></img>")
	abilString = abilString.replace("['", "")
	abilString = abilString.replace('["', "")
	abilString = abilString.replace("', '", "<br />")
	#HERE abilString = abilString.replace("""', """", "<br />")
	abilString = abilString.replace("']", "")
	abilString = abilString.replace('"]', "")
	abilString = abilString.replace("'{", "{")
	
	#Firestorm Phoenix
	
	return abilString
	
def cleanCost(cost):
	print "THIS IS THE COST"
	print cost[0]
	if cost[0] is not None:
		costString = cost[0]
		print costString
		costString = costString.replace("W", "<img class='symbol' src='/static/img/White.png'></img>")
		costString = costString.replace("R", "<img class='symbol' src='/static/img/Red.png'></img>")
		costString = costString.replace("G", "<img class='symbol' src='/static/img/Green.png'></img>")
		costString = costString.replace("B", "<img class='symbol' src='/static/img/Black.png'></img>")
		costString = costString.replace("U", "<img class='symbol' src='/static/img/Blue.png'></img>")
		return costString