from flask import Flask
from flask_restx import Api

from config import Config
from dao.model.movie import Movie
from dao.model.director import Director
from dao.model.genre import Genre
from setup_db import db
from views.movies import movies_ns
from views.directors import directors_ns
from views.genres import genres_ns


# функция создания основного объекта app
def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movies_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)
    create_data(app, db)


# функция добавления данных в базу
def create_data(app, db):
    with app.app_context():
        db.create_all()

        directors = [
            Director(name='Louis Leterrier'),
            Director(name='Alex Proyas'),
            Director(name='John Lee Hancock'),
            Director(name='Rob Marshall'),
            Director(name='Christopher Nolan'),
            Director(name='Ridley Scott'),
            Director(name='Ken Kwapis'),
        ]

        genres = [
            Genre(name='Action & Adventure'),
            Genre(name='Sci-Fi & Fantasy'),
            Genre(name='Comedies'),
            Genre(name='Dramas'),
            Genre(name='Children & Family Movies'),
        ]

        movies = [
            Movie(title='Clash of the Titans', description='If he is to save the life of the beautiful Princess Andromeda, the valiant Perseus must battle a host of powerful, beastly enemies.', trailer='link on trailer', year=2010, rating='PG-13', genre_id=1, director_id=1),
            Movie(title='Knowing', description='An MIT astrophysics professor and his son unearth a string of numbers from a time capsule that seem to reveal a cataclysm that will wipe out humanity.', trailer='link on trailer', year=2009, rating='PG-13', genre_id=2, director_id=2),
            Movie(title='The Crow', description='One year after Eric Draven and his fiancée are murdered, Draven – watched over by a hypnotic crow – returns from the grave to exact revenge.', trailer='link on trailer', year=1994, rating='R', genre_id=1, director_id=2),
            Movie(title='Saving Mr. Banks', description='the book\'s author proves a tough nut to crack.', trailer='link on trailer', year=2013, rating='PG-13', genre_id=3, director_id=3),
            Movie(title='The Founder', description='"', trailer='link on trailer', year=2016, rating='PG-13', genre_id=4, director_id=3),
            Movie(title='The Highwaymen', description='"After a fateful encounter with the McDonald brothers, struggling salesman Ray Kroc becomes driven to change the way hamburgers are made and sold.', trailer='link on trailer', year=2019, rating='R', genre_id=4, director_id=3),
            Movie(title='Mary Poppins Returns', description='"', trailer='link on trailer', year=2018, rating='PG', genre_id=5, director_id=4),
            Movie(title='Inception', description='"Two steely former Texas Rangers are tasked with tracking and killing infamous criminals Bonnie and Clyde in this crime drama based on real events.', trailer='link on trailer', year=2010, rating='PG-13', genre_id=1, director_id=5),
            Movie(title='Black Hawk Down', description='"', trailer='link on trailer', year=2001, rating='R', genre_id=1, director_id=6),
            Movie(title='Big Miracle', description='In 1930s London, Michael Banks and his three children get some help turning their topsy-turvy world around when his magical childhood nanny reappears.', trailer='link on trailer', year=2012, rating='PG', genre_id=5, director_id=7),
        ]

        with db.session.begin():
            db.session.add_all(directors)
            db.session.add_all(genres)
            db.session.add_all(movies)


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=10001)
