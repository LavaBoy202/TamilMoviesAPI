from backend.schemas.person import Person

class Movie:
    def __init__(self, genre, rating, year, duration, image, budget, summary, villain, hero, heroine, director, cast):
        self.genre = genre
        self.rating = rating
        self.year = year
        self.duration = duration
        self.image = image
        self.budget = budget
        self.summary = summary
        self.villain = villain
        self.hero = hero
        self.heroine = heroine
        self.director = director
        self.cast = cast

    ##This is for when you want to write to the database
    def to_dict(self):
        return {
            "genre": self.genre,
            "rating": self.rating,
            "year": self.year,
            "duration": self.duration,
            "image": self.image,
            "budget": self.budget,
            "summary": self.summary,
            "villain": self.villain.to_dict(),
            "hero": self.hero.to_dict(),
            "heroine": self.heroine.to_dict(),
            "director": self.director.to_dict(),
            "cast": [actor.to_dict() for actor in self.cast]
        }
    ##This is for when you want to read from the database
    @classmethod
    def from_dict(cls, data):
        return cls(
            genre=data.get('genre'),
            rating=data.get('rating'),
            year=data.get('year'),
            duration=data.get('duration'),
            image=data.get('image'),
            budget=data.get('budget'),
            summary=data.get('summary'),
            villain=Person.from_dict(data.get('villain')),
            hero=Person.from_dict(data.get('hero')),
            heroine=Person.from_dict(data.get('heroine')),
            director=Person.from_dict(data.get('director')),
            cast=[Person.from_dict(actor_data) for actor_data in data.get('cast')]
        )