from my_app import db


class Series(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    genre = db.Column(db.String(100))
    seasons = db.Column(db.Integer)
    score = db.Column(db.Float(asdecimal=True))
    is_active = db.Column(db.Boolean)

    def __init__(self, title, genre, seasons, score, is_active):
        self.title = title
        self.genre = genre
        self.seasons = seasons
        self.score = score
        self.is_active = is_active

    def __repr__(self):
        return 'Series {0}'.format(self.id)
