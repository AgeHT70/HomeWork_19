from app.dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(Movie).get(uid)

    def get_all(self):
        return self.session.query(Movie).all()

    def get_by_director_id(self, value):
        return self.session.query(Movie).filter(
            Movie.director_id == value).all()

    def get_by_genre_id(self, value):
        return self.session.query(Movie).filter(
            Movie.genre_id == value).all()

    def get_by_year(self, value):
        return self.session.query(Movie).filter(
            Movie.year == value).all()

    def create(self, movie_d):
        new_movie = Movie(**movie_d)
        self.session.add(new_movie)
        self.session.commit()
        return new_movie

    def update(self, movie_d):
        movie = self.get_one(movie_d.get("id"))
        movie.title = movie_d.get("title")
        movie.description = movie_d.get("description")
        movie.trailer = movie_d.get("trailer")
        movie.year = movie_d.get("year")
        movie.rating = movie_d.get("rating")
        movie.genre_id = movie_d.get("genre_id")
        movie.director_id = movie_d.get("director_id")

        self.session.add(movie)
        self.session.commit()

    def delete(self, uid):
        movie = self.get_one(uid)
        self.session.delete(movie)
        self.session.commit()
