class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get('name'),
            age=data.get('age')
        )
