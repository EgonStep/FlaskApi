from my_app import db


# Database creation
class Console(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    year = db.Column(db.Integer)
    price = db.Column(db.Float(asdecimal=True))
    total_games = db.Column(db.Integer)
    is_active = db.Column(db.Boolean)

    def __init__(self, name, year, price, total_games, is_active):
        self.name = name
        self.year = year
        self.price = price
        self.total_games = total_games
        self.is_active = is_active

    # Return the console ID
    def __repr__(self):
        return 'Console {0}'.format(self.id)
