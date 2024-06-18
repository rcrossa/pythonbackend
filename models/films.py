from utils.db import db
class Films(db.Model):
         id = db.Column(db.Integer, primary_key=True)
         title = db.Column(db.String(100),nullable=False)
         director = db.Column(db.String(100), nullable=False)
         rating = db.Column(db.Float, nullable=False)
         releaseDate = db.Column(db.Date, nullable=False)

         def __init__(self, title, director, rating, release_date):
            self.title = title
            self.director = director
            self.rating = rating
            self.release_date = release_date
