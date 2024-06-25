from utils.db import db
class Films(db.Model):
         id = db.Column(db.Integer, primary_key=True)
         title = db.Column(db.String(100),nullable=False)
         director = db.Column(db.String(100), nullable=False)
         rating = db.Column(db.Float, nullable=False)
         release_date = db.Column(db.Date, nullable=False)

         def __init__(self, title, director, rating, release_date):
            self.title = title
            self.director = director
            self.rating = rating
            self.release_date = release_date
         
         def serialize(self):
            return {
                'id': self.id,
                'title': self.title,
                'director': self.director,
                'rating': self.rating,
                'release_date': self.release_date.isoformat()
            }
