from mtg import db
from tools import clean_cost, clean_abilities
from sqlalchemy import func
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()

class Card(DeclarativeBase):
    __tablename__ = 'cards'

    __table_args__ = {}

    #column definitions
    abilities = db.Column(u'abilities', db.VARCHAR(length=128))
    converted_cost = db.Column(u'converted_cost', db.INTEGER())
    cost = db.Column(u'cost', db.VARCHAR(length=32))
    edition_id = db.Column(u'edition_id', db.INTEGER(), db.ForeignKey('editions.id'), nullable=False)
    flavor_text = db.Column(u'flavor_text', db.VARCHAR(length=512))
    id = db.Column(u'id', db.INTEGER(), primary_key=True, nullable=False)
    illustrator = db.Column(u'illustrator', db.VARCHAR(length=128))
    image_url = db.Column(u'image_url', db.VARCHAR(length=256))
    legalities = db.Column(u'legalities', db.TEXT())
    mci_id = db.Column(u'mci_id', db.VARCHAR(length=36))
    name = db.Column(u'name', db.VARCHAR(length=256), nullable=False)
    oracle_text = db.Column(u'oracle_text', db.VARCHAR(length=512))
    other_side = db.Column(u'other_side', db.VARCHAR(length=36))
    power = db.Column(u'power', db.VARCHAR(length=16))
    rarity = db.Column(u'rarity', db.VARCHAR(length=32))
    rulings = db.Column(u'rulings', db.TEXT())
    sub_types = db.Column(u'sub_types', db.VARCHAR(length=64))
    toughness = db.Column(u'toughness', db.VARCHAR(length=16))
    type = db.Column(u'type', db.VARCHAR(length=32))
    url = db.Column(u'url', db.VARCHAR(length=256))

    #relation definitions
    editions = db.relation('Edition', primaryjoin='Card.edition_id==Edition.id')

    def card_info(self):
        max_editions = db.session.query(func.count(Card.edition_id)).filter(Card.name == self.name).first()
        info = {
            "name": self.name,
            "graphic": self.image_url,
            "flavor": self.flavor_text,
            "illustrator": self.illustrator,
            "edition_id": self.edition_id,
            "max_editions": max_editions,
            "power": self.power,
            "type": self.type,
            "cost": clean_cost(self.cost),
            "abilities": clean_abilities(self.abilities)
        }
        return info


class Edition(DeclarativeBase):
    __tablename__ = 'editions'

    __table_args__ = {}

    #db.Column definitions
    category = db.Column(u'category', db.VARCHAR(length=128), nullable=False)
    id = db.Column(u'id', db.INTEGER(), primary_key=True, nullable=False)
    include = db.Column(u'include', db.BOOLEAN(), nullable=False)
    name = db.Column(u'name', db.VARCHAR(length=64), nullable=False)
    url = db.Column(u'url', db.VARCHAR(length=128), nullable=False)
