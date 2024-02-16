class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"


class City:
    def __init__(self, name):
        self.name = name
        self.residents = []

    def add_resident(self, person):
        self.residents.append(person)

    def __str__(self):
        resident_names = ', '.join([resident.name for resident in self.residents])
        return f"City(name={self.name}, residents=[{resident_names}])"


person1 = Person("John", 30)
person2 = Person("Alice", 25)

city = City("New York")
city.add_resident(person1)
city.add_resident(person2)

print(city)
