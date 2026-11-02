from dataclasses import dataclass

"search about decorators in python (Trust me it's worth it)"
@dataclass
class Person:
    name: str
    age: int
    city: str = "Unknown"


"""
    python generated equivalent code:

    def __init__(self, name: str, age: int, city: str = "Unknown"):
        self.name = name
        self.age = age
        self.city = city
        
    def __repr__(self): (for print)
        return f"Person(name={self.name}, age={self.age}, city={self.city})"
"""
person = Person("Belal", 25)
print(person)  