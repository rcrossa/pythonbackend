
class Films(db.Model):
         Id = db.Column(db.Integer, primary_key=True)
         Title = db.Column(db.String(100),nullable=False)
         Director = db.Column(db.String(100), nullable=False)
         Rating = db.Column(db.Float, nullable=False)
         ReleaseDate = db.Column(db.Date, nullable=False)