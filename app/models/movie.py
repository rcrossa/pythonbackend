from utils.db import get_db

"""
Modelo de la tabla movies
"""

class Movie:

    #constuctor
    def __init__(self,id_movie=None,title=None,director=None,release_date=None,rating=None,banner=None):
        self.id_movie=id_movie
        self.title=title
        self.director=director
        self.rating=rating
        self.release_date=release_date
        self.banner=banner

    def serialize(self):
        return {
            'id_movie': self.id_movie,
            'title': self.title,
            'director': self.director,
            'rating': self.rating,
            'release_date': self.release_date,
            'banner': self.banner
        }
    
    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM movies"
        cursor.execute(query)
        rows = cursor.fetchall() #Me devuelve un lista de tuplas

        movies = [Movie(id_movie=row[0], title=row[1], director=row[2],rating=row[3], release_date=row[4], banner=row[5]) for row in rows]

        # movies = []
        # for row in rows:
        #     new_movie = Movie(id_movie=row[0], title=row[1], director=row[2], release_date=row[3], banner=row[4])
        #     movies.append(new_movie)

        cursor.close()
        return movies
        

    @staticmethod
    def get_by_id(movie_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM movies WHERE id_movie = %s", (movie_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Movie(id_movie=row[0], title=row[1], director=row[2],rating=[3], release_date=row[4], banner=row[5])
        return None
    
    """
    Insertar un registro si no existe el atributo id_movie
    """
    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id_movie:
            cursor.execute("""
                UPDATE movies SET title = %s, director = %s, rating = %s, release_date = %s, banner = %s
                WHERE id_movie = %s
            """, (self.title, self.director, self.rating, self.release_date, self.banner, self.id_movie))
        else:
            cursor.execute("""
                INSERT INTO movies (title, director,rating, release_date, banner) VALUES (%s, %s, %s, %s)
            """, (self.title, self.director,self.rating, self.release_date, self.banner))
            self.id_movie = cursor.lastrowid
        db.commit()
        cursor.close()

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM movies WHERE id_movie = %s", (self.id_movie,))
        db.commit()
        cursor.close()